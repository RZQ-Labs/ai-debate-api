from fastapi import Body
from fastapi.responses import JSONResponse
from ..utils.llm_provider import generate_llm_response
from fastapi import APIRouter
from ..utils.auth import get_current_user
from fastapi import Depends

router = APIRouter(
    prefix="/llm",
    tags=["LLM"]
)

@router.post("/generate")
async def llm_generate(
    prompt: str = Body(..., embed=True),
    system_prompt: str = Body(None, embed=True),
    max_tokens: int = Body(1024, embed=True),
    _: str = Depends(get_current_user)
):
    result = await generate_llm_response(prompt, system_prompt, max_tokens)
    return JSONResponse(content={"result": result})
