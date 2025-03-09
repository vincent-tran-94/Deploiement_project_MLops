# Analyse de Sentiment des Tweets sur les Jeux Vidéo

## Objectif du Projet

L'objectif principal de ce projet est de déterminer si un type de jeu vidéo est perçu comme bon, mauvais ou neutre à partir d'un ensemble de tweets. Pour cela, nous utilisons des modèles de traitement du langage naturel (NLP) et de Machine Learning.

## Étapes du Projet

1. **Exploration et Analyse des Données** : 
   - Comprendre la structure des données.
   - Nettoyer les valeurs manquantes.
   - Éliminer les doublons.
   - Améliorer la qualité du contenu des tweets pour mieux représenter le corpus.

2. **Prétraitement des Données** :
   - Utilisation de la méthode TF-IDF (Term Frequency-Inverse Document Frequency) pour pondérer les mots.
   - Identifier la fréquence des mots et leur importance relative pour chaque tweet.

3. **Entraînement des Modèles** :
   - Utilisation de la bibliothèque Scikit-learn pour entraîner différents modèles de Machine Learning.
   - Test de plusieurs hyperparamètres avec différentes expériences utilisant MLFlow.

## Installation des Librairies

Pour installer les librairies nécessaires, exécutez la commande suivante :

```bash
pip install -r requirements.txt
```

## Lancement de MLFlow

Pour lancer MLFlow et suivre les expériences, utilisez la commande suivante:

```bash
mlflow server --host 127.0.0.1 --port 8080 
```

Cela démarrera une interface utilisateur MLFlow à l'adresse `http://127.0.0.1:8080` où vous pourrez visualiser et comparer les différentes expériences.

## Structure du Projet

- `data/` : Contient le jeux de données utilisés pour l'analyse.
- `Mlflow_experiments.ipynb` : Contient le notebooks Jupyter pour l'exploration des données et l'entraînement des modèles.
- `requirements.txt` : Liste des librairies Python nécessaires pour le projet.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
