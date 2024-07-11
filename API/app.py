from fastapi import FASTAPI
from langchain.prompts import ChatPromptTemplate

from langchain.chat_models import ChatOpenAI
from langserv import add_routes
import uvicorn 
import os 
from langchain_community.llms import ollama

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPEnAI_API_KEY")

app = FASTAPI(
    title = "Langchaain Server",
    version = "1.0",
    description="A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model = ChatOpenAI()
# ollama llama2
llm = ollama(model='llama2')

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)


add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost", port=8000)
