import openai
import os

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def review_paper_gpt3(chunk):
    prompt = f"Review the following scientific paper excerpt and provide a summary, strengths, and weaknesses:\n\n{chunk}\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
