from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##FUNCTION TO LOAD GEMINI MODEL AND GEMINI PRO MODEL AND GET RESPONSES
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="QnA Demo")
st.header("Nitin's first GenAI App")
input=st.text_input("What do you wanna know about", key="Input")
submit=st.button("Ask your question")

##When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("Here you go")
    st.write(response)

