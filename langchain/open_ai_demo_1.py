from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# get env vars
from dotenv import load_dotenv
import os

# prep api key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# create a chat model
llm = ChatOpenAI(api_key=openai_api_key)

# create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

# create a prompt template
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({"input": "how can langsmith help with testing?"})

print(response)


