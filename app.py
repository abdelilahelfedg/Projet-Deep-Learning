import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from flask import Flask, request, jsonify, render_template
from trsl_dr_en import translation
# from chatbot_darija import chatbot_dj

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Route pour le chatbot
# @app.route('/chatbot', methods=['POST'])
# def chatbot_darija():
#     data = request.get_json()
#     user_message = data.get('message', '').lower()
    
#     response = chatbot_dj(user_message)
    
#     return jsonify({'response': response})

# Route pour le traducteur
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    dest_lang = data.get('dest_lang', 'en')
    
    try:
        translated = translation(text, dest=dest_lang)  # Use the imported translation, not the route function
        return jsonify({'translated_text': translated.text if hasattr(translated, "text") else str(translated)})
    except Exception as e:
        return jsonify({'error': f'Erreur de traduction : {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)