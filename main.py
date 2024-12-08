# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

import streamlit as st

st.title("Create Your POET with OPENAI")
subject = st.text_input("Please Insert Your Concept.")
st.write("Concept : " + subject)

if st.button("GO"):
    with st.spinner("Loading..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
