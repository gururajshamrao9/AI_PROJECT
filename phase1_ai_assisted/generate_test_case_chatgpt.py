import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_case(feature_desc):
    prompt = f"Write a Selenium test case in Python using unittest for the feature: {feature_desc}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(generate_test_case("Login functionality with valid credentials"))
    print ("Testing AI")
