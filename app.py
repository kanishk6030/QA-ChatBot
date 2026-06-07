from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_NAME"] = "Chatbot"



## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions. Please response to the user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key,llm,temperature,max_tokens):
    llm = ChatGroq(model = llm,api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    out_parser = StrOutputParser()
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"question": question})
    return answer

## Title of the app
st.title("Q&A Chatbot With Groq")

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key",type="password")

## Dropdown to select the model
llm = st.sidebar.selectbox("Select the model", ["llama-3.3-70b-versatile", "openai/gpt-oss-120b", "openai/gpt-oss-20b" , "llama-3.1-8b-instant"] )

## Slider for temperature
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0, value=0.7)
## Slider for max tokens
max_tokens = st.sidebar.slider("Max Tokens",min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Ask any question and get an answer from the Groq model!")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(f"Assistant: {response}")

else:
    st.write("Please enter a question to get started.")