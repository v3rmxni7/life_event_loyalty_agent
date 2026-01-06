# src/llm/groq_client.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class GroqClient:
    """
    Thin wrapper around Groq API
    Exposes a single .run(prompt) interface
    """

    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise EnvironmentError("GROQ_API_KEY not found in environment")

        self.client = Groq(api_key=api_key)
        self.model = model

    def run(self, prompt: str) -> str:
        """
        Sends prompt to Groq and returns raw text output
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a precise enterprise AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content
