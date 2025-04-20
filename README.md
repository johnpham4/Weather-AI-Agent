# 🌦️ AI Weather Agent

An intelligent weather assistant powered by **LLaMA-based LLM** and real-time APIs. The agent detects user location via IP and provides accurate, real-world weather data through dynamic tool-calling.

---

## ⚙️ Features

- 🔍 **Location Detection**: Uses IP geolocation to determine the user's city and coordinates.
- 🌤️ **Weather Retrieval**: Calls OpenWeather API for current weather information.
- 🧠 **LLM Integration**: Uses Fireworks.ai (LLaMA-v3) with function calling to reason and invoke tools.
- 💬 **Natural Language Interface**: Ask anything like *"What's the weather like now?"* and get contextual answers.
- ⚡ **Built with FastAPI + HTML/CSS/JS** for a clean frontend-backend architecture.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-weather-agent.git
cd ai-weather-agent
```

### 2️⃣ Install Python dependencies (Backend)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables

Create a `.env` file in the `backend/` directory and add:

```env
FIREWORKS_API_KEY=your_fireworks_api_key
WEATHER_API_KEY=your_openweather_api_key
```

---

## 🚀 Running the App

### 🔥 Start the Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

### 🎨 Start the Frontend (Live Server)

Open `frontend/index.html` with [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in VS Code or serve via any static file server.

---

## 🌐 API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| POST   | `/chat`    | Accepts user query input |

---

## 🖼️ Sample UI

<p align="center">
  <img src="images/start.jpg" width="250" style="margin-right: 10px;" />
  <img src="images/question.jpg" width="250" style="margin-right: 10px;" />
  <img src="images/movies.jpg" width="250" />
</p>

---

## 🧰 Tech Stack

- **Backend**: Python, FastAPI, OpenAI API (Fireworks.ai)
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenWeather, IP Geolocation
- **Others**: dotenv, REST, Function Calling

---

## 🧠 Prompting Method

This project uses **ReAct-style prompting** by combining LLM reasoning with dynamic tool execution (function calling) to answer questions like:

> “What’s the weather in my current location?”

---

## 📄 License

This project is for educational and demo purposes.
