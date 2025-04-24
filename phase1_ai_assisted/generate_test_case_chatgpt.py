import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_case(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a QA engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

print(generate_test_case("Login functionality with valid credentials"))
print(test)
