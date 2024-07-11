from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st 
import os 
from dotenv import load_dotenv


load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")
##  Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##  Prompt Template 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistent. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

st.title("Langchain Demo with OpenAI API")
input_text =st.text_input("Search the topic u want")


# ollama LLama 2 LLM 
llm = ollama(model= "llama2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser()


if input_text:
    st.write(chain.invoke({'question':input_text}))



