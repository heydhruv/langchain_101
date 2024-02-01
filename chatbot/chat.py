from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()

API = os.environ.get('OPENAI_API_KEY')

def get_openai_response(question):
    llm = OpenAI(API)  # Create an OpenAI instance using the API key
    response = llm(question)  # Get the response from the model
    return response  # Return the response

# Basic Streamlit setup
st.set_page_config(page_title="Chatbot")
st.header("Langchain x ChatGPT")
input = st.text_input("Input: ", key="input")

if submit := st.button("Ask The Question"):  # Use := for assignment within if condition
    response = get_openai_response(input)  # Get the response within the block
    st.subheader("The Response is")
    st.write(response)  # Display the response
