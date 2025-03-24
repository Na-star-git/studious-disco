from flask import Flask

app = Flask(__name__)  # Maintenant, Flask est reconnu

@app.route("/")
def home():
    return "Bienvenue dans l'expérience"

if __name__ == "__main__":
    app.run(debug=True)
