from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("HUGGINGFACE_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"]= api_key

llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temprature":0, "max_length":64})

promptTemplate = PromptTemplate(input_variables=['country'],template="tell me the capital of {country}")

chain = LLMChain(llm=llm,prompt=promptTemplate)

response = chain.invoke("INDIA")

print(response)