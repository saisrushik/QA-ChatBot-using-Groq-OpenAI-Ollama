# 🤖 Q&A Chatbot with OpenAI, Groq, Ollama & Google Gemini

A multi-provider Q&A chatbot built with **Streamlit** and **LangChain**, allowing you to seamlessly switch between OpenAI, Groq, Ollama, and Google Gemini models from a single interface.

## ✨ Features

- **Multi-LLM Support** — Choose from four LLM providers:
  - **OpenAI** — GPT-3.5 Turbo, GPT-4, GPT-4o
  - **Groq** — GPT-OSS-120B, GPT-OSS-20B
  - **Ollama** — Gemma 2B, Gemma3 1B (local models)
  - **Google Gemini** — Gemini 2.5 Flash, Gemini 2.5 Pro
- **Configurable Parameters** — Adjust temperature and max tokens via sidebar sliders
- **Secure API Key Input** — API keys are entered as masked password fields
- **LangSmith Tracing** — Built-in LangChain tracing for monitoring and debugging

## 🛠️ Tech Stack

| Component   | Technology                          |
|-------------|-------------------------------------|
| Frontend    | Streamlit                           |
| LLM Framework | LangChain                        |
| LLM Providers | OpenAI, Groq, Ollama, Google GenAI |
| Tracing     | LangSmith                          |

## 📋 Prerequisites

- Python 3.8+
- API keys for the provider(s) you want to use (OpenAI / Groq / Google)
- [Ollama](https://ollama.com/) installed locally (if using Ollama models)
- [LangSmith](https://smith.langchain.com/) API key (for tracing)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd "QA ChatBot with Groq-OpenAI-Ollama"
```

### 2. Create a Virtual Environment

```bash
conda create -p venv python==3.10 -y
```

**Activate it:**

- **Windows:** `conda activate venv/`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

### 5. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## 📖 Usage

1. **Select an LLM Provider** from the sidebar dropdown.
2. **Enter your API Key** for the selected provider.
3. **Choose a model** from the available options.
4. **Adjust Temperature** (0.0 – 1.0) and **Max Tokens** (1 – 2048) as needed.
5. **Type your question** in the input box and click **Send**.

## 📁 Project Structure

```
QA ChatBot with Groq-OpenAI-Ollama/
├── app.py              # Main Streamlit application
├── .env                # Environment variables (not committed)
├── requirements.txt    # Python dependencies
├── venv/               # Virtual environment
└── README.md           # This file
```

## ⚙️ Configuration

| Parameter     | Description                        | Default |
|---------------|------------------------------------|---------|
| LLM Provider  | AI provider to use                 | OpenAI  |
| Model         | Specific model for the provider    | —       |
| Temperature   | Controls response randomness       | 0.7     |
| Max Tokens    | Maximum length of the response     | 1024    |
