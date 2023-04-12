import openai
import os

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def review_paper_gpt3(chunk):
    prompt = f"Review the following scientific paper excerpt and provide a summary, strengths, and weaknesses:\n\n{chunk}\n"

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chunk,
    temperature=0.7,
    max_tokens=2000,  # Reduce the number of tokens
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)


    return response.choices[0].text.strip()
