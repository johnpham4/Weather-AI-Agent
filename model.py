import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
from typing import Dict, Any
from utils import get_location, get_current_weather, tools
from pydantic import BaseModel

load_dotenv()

class QueryInput(BaseModel):
    query: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.getenv("FIREWORKS_API_KEY"),
)

# Available functions mapping
available_functions = {
    "get_current_weather": get_current_weather,
    "get_location": get_location,
}

def agent(query: str) -> Dict[str, Any]:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI agent. Give highly specific answers based on the information you're provided. Prefer to gather information with the tools provided to you rather than giving basic, generic answers."
        },
        {"role": "user", "content": query}
    ]
    
    MAX_ITERATIONS = 5
    
    for i in range(MAX_ITERATIONS):
        print(f"Iteration {i+1}")
        
        try:
            response = client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3p1-405b-instruct",
                messages=messages,
                tools=tools,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"API call failed: {str(e)}")
        
        message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason
        tool_calls = message.tool_calls
        
        messages.append(message)

        if finish_reason == "tool_calls" and tool_calls:
            for call in tool_calls:
                function_name = call.function.name
                function_args = json.loads(call.function.arguments)
                print(f"Function name: {function_name}, Arguments: {function_args}")
                
                if function_name not in available_functions:
                    raise HTTPException(status_code=400, detail=f"Function {function_name} not found")
                
                try:
                    function_response = available_functions[function_name](**function_args)
                    messages.append({
                        "tool_call_id": call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": str(function_response)
                    })
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Function {function_name} failed: {str(e)}")
                    
        elif finish_reason == "stop":
            return {"response": message.content}
    
    return {"response": "No answer found for limited rates."}

@app.post("/chat")
async def handle_query(data: QueryInput):
    try:
        print(data.query)
        result = agent(data.query)
        print(f"Final result: {result}")
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)