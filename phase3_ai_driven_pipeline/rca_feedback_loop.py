from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
logs = open("../sample_data/test_failures_logs.txt").read()

prompt = f"Perform RCA on test logs:\n{logs}"
response = OpenAI().ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
print(response["choices"][0]["message"]["content"])
