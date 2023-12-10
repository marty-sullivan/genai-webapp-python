from langchain.schema import HumanMessage
from langserve.client import RemoteRunnable
from os import environ
import streamlit as st

backend_host = environ['BACKEND_HOST']
backend_port = environ['BACKEND_PORT']

gpt35_chain = RemoteRunnable(f'http://{backend_host}:{backend_port}/azure_gpt35')
gpt4_chain = RemoteRunnable(f'http://{backend_host}:{backend_port}/azure_gpt4')

st.title('Azure OpenAI Chatbot')
st.caption('A simple chatbot that uses either the latest GPT-3.5 or GPT-4 model')

model_selection = st.selectbox('Select LLM', ['gpt-4-turbo', 'gpt-3.5-turbo'])

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    avatar = "🤖" if msg["role"] == "assistant" else "👤"
    st.chat_message(msg["role"], avatar=avatar).write(msg["content"])

if prompt := st.chat_input('Type your question...'):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar='👤').write(prompt)

    if model_selection == 'gpt-3.5-turbo':
        response = gpt35_chain.stream(dict(
            messages=[
                HumanMessage(content=prompt),
            ],
        ))
    
    elif model_selection == 'gpt-4-turbo':
        response = gpt4_chain.stream(dict(
            messages=[
                HumanMessage(content=prompt),
            ],
        ))
    
    else:
        st.write('Error: Invalid model selection')

    with st.chat_message("assistant", avatar='🤖'):
        full_message = ''
        with st.empty():
            for message in response:
                full_message += message.content
                st.write(full_message)

    st.session_state.messages.append({"role": "assistant", "content": full_message})
