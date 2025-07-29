# Task
Task-1:-
 Gemini Chat Assistant with Real-Time Search
This project is a command-line based intelligent chatbot that combines the power of Google Gemini (Generative AI) and SerpAPI to deliver smart, real-time responses. The chatbot can handle general queries and will automatically search the internet when real-time information is required (e.g., latest news, current weather, prices).

✨ Features
🧠 Conversational AI using Gemini (Gemini 2.0 Flash Model)
🔍 Real-time web search integration via SerpAPI
📚 Dynamic context tracking with full conversation history
🔄 Automatically detects when real-time information is needed
🛠 Requirements
Python 3.7+
google-generativeai
serpapi
Install dependencies:

pip install google-generativeai serpapi

Task-2:-
 Sentiment Analysis Web App
This is a simple web application built using Flask that performs sentiment analysis on user-provided text using TextBlob. It classifies the input as Positive, Negative, or Neutral, and displays polarity and subjectivity scores.

🚀 Features
Analyze the sentiment of any text.
View:
🟢 Sentiment Label (Positive / Negative / Neutral)
📈 Polarity Score (range: -1 to +1)
🧠 Subjectivity Score (range: 0 to 1)
Stylish, modern Glassmorphism UI with animated buttons and custom badges.
🛠️ Installation & Running
Clone or download this repository.

Install dependencies:

pip install flask textblob
python -m textblob.download_corpora

Task-3:-
 Voice-Based AI Image Generator 🎤 ➜ 🧠 ➜ 🖼️
This Python app uses voice input to generate AI-powered images using MonsterAPI's txt2img model. Just speak your prompt, and the app listens, converts speech to text, sends it to the API, and downloads the resulting image to your computer.

🎯 Features
🎙️ Uses microphone input to capture speech
🔤 Converts voice to text using Google Speech Recognition
🧠 Sends text as a prompt to MonsterAPI’s txt2img model
🌄 Downloads and displays the generated image in your browser
🧾 Option to customize parameters like guidance, seed, aspect ratio
🛠️ Requirements
Install the dependencies using pip:

pip install monsterapi requests SpeechRecognition
