import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from transformers import pipeline


def translation(sentence, dest='en'):
    
    if dest == 'en':
        model = 'nwiser/eng-darija-trsl'
    elif dest == 'dj':
        model = 'nwiser/darija-eng-trsl' 

    pipe = pipeline("text2text-generation", model=model)

    translations = pipe(sentence)

    return translations[0]['generated_text'] if translations else ""

# translation(' 
# سلام، كيف داير؟ 
# ', dest='en')