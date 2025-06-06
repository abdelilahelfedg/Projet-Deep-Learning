# import os
# os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# os.environ["USE_TF"] = "0"
# from transformers import pipeline
# from llama_cpp import Llama

# # Chemin vers ton fichier GGUF
# MODEL_PATH = "darija-chat2/unsloth.Q4_K_M.gguf"

# # Charger le modèle une seule fois (à l'initialisation)
# llm = Llama(model_path=MODEL_PATH, n_ctx=512)

# def chatbot_dj(sentence):
#     output = llm(sentence, max_tokens=100)
#     # Récupérer le texte généré
#     return output["choices"][0]["text"].strip()


# from transformers import pipeline

# # Crée le pipeline de génération de texte avec un modèle Hugging Face (ici GPT-2)
# chatbot = pipeline("text-generation", model="AbdelilahFdg/darija-chat1")

# def chatbot_dj(sentence):
#     # Génère une réponse à partir de l'entrée utilisateur
#     response = chatbot(sentence, max_new_tokens=100)
#     return response[0]['generated_text'].strip()