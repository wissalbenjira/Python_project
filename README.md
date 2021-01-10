

# SOMMAIRE

1. Présentation du projet
2. Documents mis à disposition
3. Guide du code
4. Guide de l'API
5. Conclusion


# 1. Présentation du projet

Le dataset est Online_shoppers_intention.csv. 
Ce projet a pour but de deviner l'intention du client à l'aide de 17 prédicteurs: s'il va consommer sur le site ou pas, grâce à la réponse Revenue (True si le client achète, False sinon).
Des méthodes de Machine Learning sont utilisées dans le code puis une API Flask permet de visualiser la prédiction.

# 2. Documents mis à disposition

Le Jupyter Notebook "notebook.ipynb" qui contient le code de visualisation des données et des modèles Machine Learning.
Le PowerPoint "Presentation.pdf" détaillant le contenu et les résultats de notre projet.
L'API qui regroupe les fichiers d'exécution "app.py" et "request.py", le modèle choisi "model_saved.joblib" et les templates "index.html" et "result.html".

# 3. Guide du code

Le code est divisé en plusieurs étapes:
Data Visualisation
Data Exploration
Test de modèles manuellement
Grid Search
Test automatisés (xgboost)
Sélection du modèle final

# 4. Guide de l'API

Il est possible de lancer la prédiction: 
- en console (lancement d'app.py puis du request.py), la prédiction se fait sur [0,0,0,0,1,0,0.2,0.2,0,0,2,1,1,1,1,2,0] -> retourne 0 (pas d'achat pour ce client).
- sur l'API Flask (lancement d'app.py qui fait appel aux templates), la prédiction se fait selon l'utilisateur.

# 5. Conclusion

Après de nombreux modèles test, le Gradient Boosting Classifier est le plus performant avec une précision de 90%.
