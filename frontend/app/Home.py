from langserve.client import RemoteRunnable
from os import environ
import streamlit as st
import requests

backend_host = environ['BACKEND_HOST']
backend_port = environ['BACKEND_PORT']

with st.sidebar:
    f'''
    ### Here is some sidebar markdown 
    * [Local Backend API Documentation](http://localhost:{backend_port}/docs)
    * [Streamlit Components](https://docs.streamlit.io/library/components/components-api)
    * [LangChain Expression Language](https://python.langchain.com/docs/expression_language/get_started)
    '''

st.title("🐍🦜🔗")
st.caption("A GenAI rapid prototyping environment for Python web apps based on LangChain & Streamlit")

'''
Select an option on the left to try out either Azure OpenAI or AWS Bedrock Large Language Models (LLMs) that support chat functionality.
'''