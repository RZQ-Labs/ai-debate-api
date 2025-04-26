from transformers import AutoTokenizer, AutoModelForMaskedLM
AutoTokenizer.from_pretrained('indobenchmark/indobert-base-p1', cache_dir='./models/indobert')
AutoModelForMaskedLM.from_pretrained('indobenchmark/indobert-base-p1', cache_dir='./models/indobert')
