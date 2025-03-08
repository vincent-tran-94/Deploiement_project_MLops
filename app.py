import pickle
from flask import Flask, request, render_template

# Charger le modèle
with open("models/RandomClassifierForest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Charger le vectorizer utilisé lors de l'entraînement
with open("models/tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)


# Initialiser l'application Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        tweet_text = request.form["tweet"]
        if tweet_text:
            # Transformer le texte en représentation numérique
            tweet_features = vectorizer.transform([tweet_text])

            # Faire la prédiction
            prediction = model.predict(tweet_features)[0]
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5009)
