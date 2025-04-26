from app.utils import openrouter
import openai
from app.utils.indobert import indobert_fill_mask
from app.settings import settings

async def generate_llm_response(prompt: str, system_prompt: str = None, max_tokens: int = 1024):
    if settings.llm_provider == "openai":
        openai.api_key = settings.openai_api_key
        model = settings.openai_model
        messages = [
            {"role": "system", "content": system_prompt or "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]
    elif settings.llm_provider == "indobert":
        # IndoBERT is not async, so run in thread pool
        import asyncio
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(None, indobert_fill_mask, prompt)
        return results[0] if results else ""
    else:
        return await openrouter.call_openrouter(prompt, system_prompt, max_tokens)
