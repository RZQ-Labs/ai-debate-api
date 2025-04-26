from fastapi import Body
from fastapi.responses import JSONResponse
from ..utils.llm_provider import generate_llm_response
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def llm_generate(
    prompt: str = Body(..., embed=True),
    system_prompt: str = Body(None, embed=True),
    max_tokens: int = Body(1024, embed=True)
):
    result = await generate_llm_response(prompt, system_prompt, max_tokens)
    return JSONResponse(content={"result": result})
