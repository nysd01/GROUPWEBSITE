# utils.py
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I'm unable to assist with that right now. Please try again later."

