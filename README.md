🚀  LIKKI AI Assistant

A production-style Multimodal AI Assistant built using Python and Generative AI.

LIKKI integrates voice recognition, text intelligence, real-time web search, image understanding, OCR, and audio synthesis into a unified, scalable AI system delivered through a Streamlit-based web interface.

This project demonstrates real-world AI system engineering beyond a basic chatbot implementation.

📌 Project Overview

LIKKI is a full-stack AI assistant capable of:

🎤 Real-time Voice Interaction

⌨️ Text-based Query Processing

🌐 Live Web Search & Image Retrieval

🖼 OCR-based Text Extraction from Images

🔊 Simultaneous Text + Audio Response Generation

The system follows a modular architecture designed for scalability, maintainability, and production-style development.

✨ Key Features
🔹 Multimodal Input Support

Voice (Speech-to-Text)

Text

Image Upload

🔹 Intelligent AI Processing

Context-aware Generative AI responses

Dynamic routing based on query type

Integration with live web search APIs

🔹 Image Understanding

Optical Character Recognition (OCR)

Extract text from uploaded images

🔹 Dual Output Generation

Text output in Streamlit UI

Audio response via Text-to-Speech engine

🔹 Clean Web Interface

Built with Streamlit

Real-time input/output updates

Structured display of search results

🏗 System Architecture
High-Level Architecture Diagram
                         ┌──────────────────────────┐
                         │        User Layer        │
                         │──────────────────────────│
                         │  🎤 Voice Input          │
                         │  ⌨️ Text Input           │
                         │  🖼 Image Upload         │
                         └─────────────┬────────────┘
                                       │
                                       ▼
                 ┌────────────────────────────────────┐
                 │         Input Processing Layer     │
                 │────────────────────────────────────│
                 │  • Speech Recognition (STT)       │
                 │  • Text Preprocessing             │
                 │  • OCR (Image → Text)             │
                 └─────────────┬──────────────────────┘
                               │
                               ▼
                 ┌────────────────────────────────────┐
                 │      Intelligence & Routing Layer  │
                 │────────────────────────────────────│
                 │  • Query Classification           │
                 │  • Context Aggregation            │
                 │  • Web Search Trigger Logic       │
                 └─────────────┬──────────────────────┘
                               │
        ┌──────────────────────┼────────────────────────┐
        ▼                      ▼                        ▼
┌────────────────┐   ┌────────────────────┐   ┌────────────────────┐
│ Generative AI  │   │  Web Search APIs   │   │  Image Search APIs │
│  (LLM Engine)  │   │  (Live Results)    │   │  (Live Images)     │
└────────┬───────┘   └──────────┬─────────┘   └──────────┬─────────┘
         │                      │                        │
         └──────────────┬───────┴───────────────┬────────┘
                        ▼                       ▼
               ┌────────────────────────────────────┐
               │        Response Aggregation Layer  │
               │────────────────────────────────────│
               │  • Merge AI + Search Results      │
               │  • Format Structured Output       │
               └─────────────┬──────────────────────┘
                             │
                             ▼
               ┌────────────────────────────────────┐
               │          Output Layer              │
               │────────────────────────────────────│
               │  • Text Output (Streamlit UI)     │
               │  • Audio Output (TTS Engine)      │
               └─────────────┬──────────────────────┘
                             │
                             ▼
               ┌────────────────────────────────────┐
               │        Streamlit Web Interface     │
               └────────────────────────────────────┘

🧠 Architectural Design Principles
Modular Architecture

Each functional block (Voice, OCR, Search, AI Engine, Output) is separated for scalability and maintainability.

Separation of Concerns

Input Layer

Processing Layer

Intelligence Layer

Output Layer

Real-Time Multimodal Processing

Supports simultaneous:

Voice recognition

Web search

AI reasoning

Audio synthesis

Extensibility

The system can be extended with:

Vector database memory (Pinecone / FAISS)

Authentication system

Cloud deployment (AWS / Azure / GCP)

Conversation history storage

LLM switching capability

🛠 Tech Stack
Core

Python

Web Interface

Streamlit

Voice Processing

SpeechRecognition

PyAudio

pyttsx3

Image Processing

Pillow

OCR Engine (Tesseract or equivalent)

AI Layer

Generative AI APIs

External Integrations

Web Search APIs

Image Search APIs

📂 Project Structure
likki-ai-assistant/
│
├── app.py
├── voice_module.py
├── ocr_module.py
├── search_module.py
├── ai_engine.py
├── requirements.txt
└── README.md


The modular design enables independent testing and easy feature expansion.

⚙ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/likki-ai-assistant.git
cd likki-ai-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

🔐 Configuration

Set environment variables for required API keys:

export GENERATIVE_AI_API_KEY=your_key_here
export SEARCH_API_KEY=your_key_here


Configure OCR engine path if required by your system.

🚀 Use Cases

Personal AI Assistant

AI Automation Demonstrations

Multimodal AI Research Projects

Educational AI Applications

Portfolio Project for AI/ML Engineering Roles

📈 Future Improvements

Cloud-native deployment

Persistent memory via vector databases

Authentication & user profiles

Conversation history storage

Async processing for performance optimization

Mobile-responsive UI

👤 Author

Gnani Tadiparthi
AI & Generative AI Developer

📄 License

This project is developed for educational and demonstration purposes.
