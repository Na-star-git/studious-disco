import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue dans l'expérience"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Récupère le port défini par Render, sinon utilise 5000
    app.run(host="0.0.0.0", port=port, debug=False)
