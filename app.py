import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

#Langchain Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with OPENAI"


#prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")
    ]
)

def generate_responsse(question, llm_provider, llm,  api_key , temprature, max_tokens):
    if llm_provider == "openai":
        llm = ChatOpenAI(model=llm, api_key=api_key, temperature=temprature, max_tokens=max_tokens)
    elif llm_provider == "groq":
        llm = ChatGroq(model=llm, api_key=api_key, temperature=temprature, max_tokens=max_tokens)
    elif llm_provider == "ollama":
        llm = ChatOllama(model=llm, api_key=api_key, temperature=temprature, max_tokens=max_tokens)
    elif llm_provider == "google":
        llm = ChatGoogleGenerativeAI(model=llm, api_key=api_key, temperature=temprature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer

#Title of the app
st.title("Q&A Chatbot with OPENAI-GROQ-OLLAMA")

#Sidebar for configuration
st.sidebar.title("Configuration")

llm_provider = st.sidebar.selectbox("Select LLM Provider", ["openai", "groq", "ollama", "google"])
api_key = st.sidebar.text_input("Enter API Key", type="password")

if llm_provider == "openai":
    llm = st.sidebar.selectbox("Select LLM", ["gpt-3.5-turbo", "gpt-4", "gpt-4o"])
elif llm_provider == "groq":
    llm = st.sidebar.selectbox("Select LLM", ["openai/gpt-oss-120b", "openai/gpt-oss-20b"])
elif llm_provider == "ollama":
    llm = st.sidebar.selectbox("Select LLM", ["gemma:2b", "gemma3:1b"])
elif llm_provider == "google":
    llm = st.sidebar.selectbox("Select LLM", ["gemini-2.5-flash", "gemini-2.5-pro"])

temprature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 1, 2048, 1024)

st.write("Go ahead and ask any question")
input_text = st.text_input("You: ")

if st.button("Send"):
    response = generate_responsse(input_text,llm_provider, llm, api_key, temprature, max_tokens)
    st.write(response)
else:
    st.write("Please Provide the query")




