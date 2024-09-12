import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for GPT-4 or "gpt-3.5-turbo" for GPT-3.5
            messages=[
                {"role": "system", "content": "You are a helpful assistant for an e-commerce website."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Log the error for debugging
        print(f"Error during OpenAI API call: {str(e)}")
        return "Sorry, I'm unable to assist with that right now. Please try again later."
