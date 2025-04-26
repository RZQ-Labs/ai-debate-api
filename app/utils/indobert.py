from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch
from typing import Optional
from app.settings import settings

INDOBERT_MODEL_PATH = settings.indobert_model_path

class IndoBERTSingleton:
    _tokenizer = None
    _model = None

    @classmethod
    def get_tokenizer(cls):
        if cls._tokenizer is None:
            cls._tokenizer = AutoTokenizer.from_pretrained(INDOBERT_MODEL_PATH)
        return cls._tokenizer

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = AutoModelForMaskedLM.from_pretrained(INDOBERT_MODEL_PATH)
        return cls._model

def indobert_fill_mask(text: str, top_k: int = 1) -> Optional[list]:
    tokenizer = IndoBERTSingleton.get_tokenizer()
    model = IndoBERTSingleton.get_model()
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    mask_token_index = (inputs.input_ids == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
    mask_logits = logits[0, mask_token_index, :]
    top_tokens = torch.topk(mask_logits, top_k, dim=1).indices[0].tolist()
    results = []
    for token in top_tokens:
        token_str = tokenizer.decode([token])
        filled = text.replace(tokenizer.mask_token, token_str)
        results.append(filled)
    return results
