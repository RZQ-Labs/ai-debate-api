from fastapi import Body
from fastapi.responses import JSONResponse
from ..utils.llm_provider import generate_llm_response
from fastapi import APIRouter
from ..utils.auth import get_current_user
from fastapi import Depends
from ..schemas.prompt_schema import PromptInput

router = APIRouter(
    prefix="/llm",
    tags=["LLM"]
)

@router.post("/generate")
async def llm_generate(
    prompt_in: PromptInput,
    _: str = Depends(get_current_user)
):
    result = await generate_llm_response(prompt_in.prompt, prompt_in.system_prompt, prompt_in.max_tokens)
    return JSONResponse(content={"result": result})
