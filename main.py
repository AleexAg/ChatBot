import streamlit as st
from langchain_openai import ChatOpenAI

llModel = ChatOpenAI(model="gpt-4o", temperature=0, api_key="")


st.title('CHATBOT GPT-4')
messages = [("System", "Eres un chatbot AI de utilidad, tu nombre es botin, habla como si fueras un humano")]

if "messages" not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])

if prompt := st.chat_input("En que puedo ayudarte? "):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append("human", prompt)

    response = llModel.invoke(messages).content

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    