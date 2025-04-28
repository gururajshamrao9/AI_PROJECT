# phase1_ai_assisted/generate_test_case_chatgpt.py

import ollama

def generate_test_case(prompt):
    response = ollama.chat(
        model='llama3',  # Make sure you have pulled this model!
        messages=[
            {"role": "user", "content": f"Generate test cases for: {prompt}"}
        ]
    )
    return response['message']['content']

if __name__ == "__main__":
    print("Running Phase 1: AI Test Case Generation")
    print(generate_test_case("Login functionality with valid credentials"))


