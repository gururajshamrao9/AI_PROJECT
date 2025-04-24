from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.7)
prompt = PromptTemplate.from_template("Generate realistic test data for {context}")
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("an e-commerce checkout process"))
