from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("HUGGINGFACE_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"]= api_key

llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temprature":0, "max_length":64})


text = "what is the capital of INDIA?"

response = llm.invoke(text)

print(response)

# in response it gave me mumbai Xd
