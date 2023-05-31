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


def translate_en2zh(text:str):
    # Tokenize the text
    batch = tokenizer(text=[text],return_tensors='pt',truncation=True, max_length=512)

    # Perform the translation and decode the output
    translation = model.generate(**batch)
    result = tokenizer.batch_decode(translation, skip_special_tokens=True)
    print('translate_en2zh: {en}\\n{zh}\\n')
    print(text)
    print(result)
    return result[0]

# text = "In terms of time, the Chinese space station was built more than 20 years later than the International Space Station."
# print(translate_en2zh(text))
#
# while True:
#     op = input('type a to continue, others to stop:')
#     if op == 'a':
#         print(translate_en2zh(input('type any english to translate to chinese:')))
#     else:
#         break