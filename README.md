# Analyse du Génome du Dengue 🦠🔬

> **🚨 Le projet est disponible à l'adresse suivante : [https://keigonwilson.com/](https://keigonwilson.com/) 🚨**

> **Note**: Le projet se trouve sur la branche `master` 📍

Ce projet est une application web basée sur Django pour analyser et comparer les génomes du virus Dengue. Elle propose des fonctionnalités pour ajouter, modifier, supprimer et comparer des séquences génomiques. L'application comprend également une visualisation 3D des données génomiques en utilisant Three.js 🌐.

## Fonctionnalités 🚀

- **Page d'accueil** 🏠 : Une page d'accueil accueillante avec une visualisation 3D.
- **Liste des génomes** 📋 : Affiche une liste de tous les génomes dans la base de données.
- **Ajouter un génome** ➕ : Ajoutez une nouvelle séquence génomique à la base de données.
- **Modifier un génome** ✏️ : Modifiez une séquence génomique existante.
- **Supprimer un génome** ❌ : Supprimez une séquence génomique.
- **Comparer des génomes** 🔍 : Comparez deux séquences génomiques côte à côte.
- **Détails du génome** 📊 : Affiche des informations détaillées sur un génome spécifique.

## Installation ⚙️

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votreutilisateur/dengue-genome-analysis.git
   cd dengue-genome-analysis
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel** :
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```
   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurer la base de données** 🗃️ :
   Mettez à jour le paramètre `DATABASES` dans le fichier `bioinformatique2/settings.py` avec vos informations de connexion à la base de données.

6. **Appliquer les migrations** 🔄 :
   ```bash
   python manage.py migrate
   ```

7. **Lancer le serveur de développement** 🚀 :
   ```bash
   python manage.py runserver
   ```

## Utilisation 🧑‍💻

### Page d'accueil 🏠
La page d'accueil présente une visualisation 3D des données génomiques. Accédez à cette page en visitant l'URL racine de l'application.

### Liste des génomes 📋
Consultez la liste de tous les génomes dans la base de données en naviguant vers `/genomes/`. Chaque entrée de génome comprend son identifiant de séquence et sa description.

### Ajouter un génome ➕
Pour ajouter un nouveau génome, accédez à `/genomes/add/` et remplissez le formulaire avec l'identifiant de la séquence, la séquence elle-même et la description. L'application calculera automatiquement les pourcentages de A, T, C, G, le contenu GC et le ratio AT/GC.

### Modifier un génome ✏️
Pour modifier un génome existant, accédez à `/genomes/edit/<pk>/` où `<pk>` est la clé primaire du génome. Mettez à jour les champs du formulaire et enregistrez les modifications.

### Supprimer un génome ❌
Pour supprimer un génome, accédez à la page de modification du génome et cliquez sur le bouton "Supprimer le génome". Confirmez la suppression en tapant "SUPPRIMER".

### Comparer des génomes 🔍
Pour comparer deux génomes, accédez à `/genomes/compare/`. Sélectionnez deux génomes dans les menus déroulants pour afficher leurs détails côte à côte et comparez leurs pourcentages de A, T, C, G à l'aide d'un graphique en barres.

### Détails du génome 📊
Pour afficher les informations détaillées sur un génome spécifique, accédez à `/genomes/<pk>/` où `<pk>` est la clé primaire du génome. Les détails sont renvoyés sous forme de réponse JSON.

## Structure des fichiers 📂

- **bioinformatique2/** : Paramètres et configuration du projet Django.
- **genomes/** : Application Django pour l'analyse des génomes.
- **templates/genomes/** : Modèles HTML pour l'application.
- **static/** : Fichiers statiques (CSS, JavaScript, images).
- **models.py** : Modèles de base de données.
- **views.py** : Fonctions de vue.
- **forms.py** : Formulaires Django.
- **urls.py** : Routage des URL.

## Dépendances 📦

- Django
- djangorestframework
- django-cors-headers
- mssql-django
- Three.js (pour la visualisation 3D)
- Chart.js (pour les graphiques de comparaison de génomes)

## Contribuer 👩‍💻👨‍💻

1. Forkez le dépôt 🍴.
2. Créez une nouvelle branche (ex : `git checkout -b feature-branch`) 🌱.
3. Apportez vos modifications ✨.
4. Validez vos changements (ex : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`) 💾.
5. Poussez vos modifications vers la branche (`git push origin feature-branch`) 🚀.
6. Ouvrez une pull request 🔄.

## Licence 📄

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

## Contact 📬

Pour toute question ou suggestion, veuillez ouvrir un problème ou contacter le propriétaire du dépôt.

---

Ce fichier README fournit un aperçu complet du projet **Analyse du Génome du Dengue**, incluant les instructions d'installation, les détails d'utilisation et des informations sur la structure et les dépendances du projet.
```



