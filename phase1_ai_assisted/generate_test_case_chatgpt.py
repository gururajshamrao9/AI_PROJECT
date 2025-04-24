import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_case(feature):
    prompt = f"Generate test cases for the feature: {feature}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # <- Update this if you confirm gpt-4 works
        messages=[
            {"role": "system", "content": "You are an expert software QA engineer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(generate_test_case("Login functionality with valid credentials"))

