from openai import OpenAI


def analyze_failure(error_message):

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a QA automation expert"},
            {"role": "user", "content": f"Analyze this automation failure: {error_message}"}
        ]
    )

    return response.choices[0].message.content

#Use when test fails
try:
    assert page.locator("#checkout").is_visible()
except Exception as e:

    from src.utilities.ai_failure_analyzer import analyze_failure

    print(analyze_failure(str(e)))