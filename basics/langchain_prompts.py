from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("HUGGINGFACE_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"]= api_key

llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temprature":0, "max_length":64})

capital_Template = PromptTemplate(input_variables=['country'],template="tell me the capital of {country}")

capital_chain = LLMChain(llm=llm,prompt=capital_Template)

famous_food_capital_template = PromptTemplate(input_variables=['capital'],template="tell me the famous food to try in {capital}")

famous_food_capital_chain = LLMChain(llm=llm,prompt=famous_food_capital_template)

chain = SimpleSequentialChain(chains=[capital_chain,famous_food_capital_chain])

response = chain.invoke("india")

print(response)