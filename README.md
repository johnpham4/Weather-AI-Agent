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

cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

FIREWORKS_API_KEY=your_fireworks_api_key
WEATHER_API_KEY=your_openweather_api_key

