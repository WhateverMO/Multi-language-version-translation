import huggingface_hub.utils._validators
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

didnt_load_flag,tokenizer,model = True,'',''

while didnt_load_flag:
    try:
        tokenizer = AutoTokenizer.from_pretrained("./opus-mt/en-zh/tokenizer")
        model = AutoModelForSeq2SeqLM.from_pretrained("./opus-mt/en-zh/model")
        didnt_load_flag = False
    except huggingface_hub.utils._validators.HFValidationError:
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
        tokenizer.save_pretrained("./opus-mt/en-zh/tokenizer")
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
        model.save_pretrained("./opus-mt/en-zh/model")
