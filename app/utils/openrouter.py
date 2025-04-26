import httpx
from app.settings import settings

OPENROUTER_API_KEY = settings.openrouter_api_key
OPENROUTER_BASE_URL = settings.openrouter_api_url
OPENROUTER_MODEL = settings.openrouter_model_name

async def call_openrouter(prompt: str, system_prompt: str = None, max_tokens: int = 1024):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt or "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OPENROUTER_BASE_URL}/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
