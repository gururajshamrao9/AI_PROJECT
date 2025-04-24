from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
diff = open("../sample_data/pr_code_diff_sample.txt").read()

response = OpenAI().ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Generate a test plan for this PR diff:\n{diff}"}]
)

print(response['choices'][0]['message']['content'])
