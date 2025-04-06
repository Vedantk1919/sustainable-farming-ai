# 🌱 Sustainable Farming AI Web Application

An AI-powered, multi-agent web application that assists farmers in making data-driven decisions for sustainable agriculture using environmental analysis, market research, and multilingual AI interaction.

---

## 🚀 Features

- ✅ Crop recommendation system
- 🤖 AI Chatbot (powered by Hugging Face + LangChain)
- 🗣️ Bilingual Voice Assistant
- 📈 Market profitability analysis
- 🌿 Soil and environmental evaluation
- 💾 Local data storage using SQLite
- 📊 Visual insights with Chart.js

---

## 🧠 AI Agents Architecture

1. **Farmer Advisor Agent**  
   → Analyzes soil and environmental inputs.

2. **Market Researcher Agent**  
   → Determines crop profitability from market trends.

3. **AI Chatbot & Voice Assistant**  
   → Communicates results using Mistral-7B (via Hugging Face) and supports bilingual (English & Hindi) voice commands.

4. **SQLite Memory Layer**  
   → Stores and retrieves recommendations and analysis history.

---

## 💻 Technologies Used

### 🔹 Backend
- Python
- Flask (REST API)
- SQLite (for local storage)

### 🔹 AI & NLP
- Custom ML logic for crop and market analysis
- Hugging Face `Mistral-7B-Instruct` via LangChain
- SpeechRecognition + gTTS (for Voice Assistant)

### 🔹 Frontend
- HTML, CSS, JavaScript
- Chart.js (for graphs)
- CORS-enabled API integration

---

## 📸 Demo

| Component | Preview |
|----------|---------|
| 🧠 Recommendation Form | ![Form Screenshot](link_to_image) |
| 🤖 Chatbot | ![Chatbot Demo](link_to_image) |
| 🎤 Voice Assistant | ![Voice Assistant](link_to_image) |

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/sustainable-farming-ai.git
cd sustainable-farming-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
