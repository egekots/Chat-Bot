from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os

st.title("Chat Bot")

st.markdown("Please put your API key first!")

with st.sidebar:
    st.header("Settings")
    api_key=st.text_input("Put your Gemini API key :",key="password")

if api_key:

    os.environ["GEMINI_API_KEY"]=api_key

    st.success("Agent is ready! Write your question.")
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]

    for message in st.session_state.messages:
        if isinstance(message,HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        if isinstance(message,AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)

    
    prompt=st.chat_input("Say Something")

    if prompt:

        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append(HumanMessage(prompt))

        
        llm=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            temperature=1
        )

        response=llm.invoke(st.session_state.messages).content
        with st.chat_message("assistant"):
            st.markdown(response)
            st.session_state.messages.append(AIMessage(response))
else:
    st.info("Please put your Gemini API Key!")