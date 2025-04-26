from pydantic import BaseModel, Field
import requests

class HuggingFaceLLM(BaseModel):
    model_name: str = Field(..., description="gpt2")
    api_key: str = Field(..., description="your api key")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Optionally handle any extra initialization here if needed

    def _generate(self, prompt: str) -> str:
        model_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 100,
                "temperature": 0.7,
                "top_k": 50,
                "top_p": 0.9,
                "do_sample": True
            }
        }

        response = requests.post(model_url, headers=headers, json=payload)

        if response.status_code == 200:
            generated_text = response.json()[0]['generated_text']
            return generated_text
        else:
            raise Exception(f"HuggingFace API Error {response.status_code}: {response.text}")

    @property
    def _llm_type(self):
        return "huggingface"
