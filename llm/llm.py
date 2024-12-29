from g4f import models
from g4f.client import Client

class LLM:
    def __init__(self):
        self._model = models.gpt_4
        self._web_search = True

    def process(self, message):
        client = Client()
        response = client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": message}],
            web_search=self._web_search,
        )

        return response.choices[0].message.content

