# hospital-loisStatistiques

---

# 🎯 Projet : Étude des Lois de Probabilité – Application Interactive Streamlit

### 👩‍💻 Auteur : **Awa [Nom de famille]**

### 🏫 Université : **Assane Seck University of Ziguinchor**

### 📅 Année : **2025**

### 🔧 Technologies : **Python, Streamlit, NumPy, Matplotlib, SciPy**

---

## 🧠 Description du projet

Ce projet est une **application interactive Streamlit** permettant d’explorer, de visualiser et de comprendre les **principales lois de probabilité** à travers des **simulations dynamiques** et des **tests statistiques**.

L’objectif est de rendre les notions abstraites de la statistique **visuelles, intuitives et pédagogiques**, tout en offrant une expérience interactive et fluide.

---

## 📊 Lois de probabilité étudiées

| Type        | Nom de la loi         | Paramètres principaux | Description                                                         |
| ----------- | --------------------- | --------------------- | ------------------------------------------------------------------- |
| 🔹 Discrète | **Loi de Poisson**    | λ (intensité)         | Modélise le nombre d’événements rares dans un intervalle de temps.  |
| 🔹 Discrète | **Loi Binomiale**     | n, p                  | Compte le nombre de succès dans une série d’expériences.            |
| 🔹 Discrète | **Loi Géométrique**   | p                     | Nombre d’essais avant le premier succès.                            |
| 🔹 Continue | **Loi Exponentielle** | λ                     | Temps entre deux événements successifs.                             |
| 🔹 Continue | **Loi Gamma**         | k, θ                  | Généralisée de l’exponentielle (somme de variables exponentielles). |
| 🔹 Continue | **Loi Beta**          | α, β                  | Modélise les proportions ou probabilités.                           |
| 🔹 Continue | **Loi Uniforme**      | a, b                  | Toutes les valeurs dans un intervalle sont équiprobables.           |

---

## 🚀 Fonctionnalités principales

✅ **Interface intuitive** via `Streamlit`
✅ **Génération aléatoire de données** selon les lois choisies
✅ **Visualisation dynamique** (histogrammes, densités, courbes PDF et CDF)
✅ **Statistiques descriptives** : moyenne, variance, écart-type, etc.
✅ **Formules mathématiques** rendues en LaTeX
✅ **Animations interactives** pour visualiser la variation des paramètres
✅ **Dashboard final comparatif** entre les lois

---

## 🧩 Structure du projet

```
Stat_Maths_Projects/
│
├── app.py                        # Page principale Streamlit (menu de navigation)
│
├── poisson_page.py               # Loi de Poisson
├── binomiale_page.py             # Loi Binomiale
├── geom_page.py                  # Loi Géométrique
├── exponentielle_page.py         # Loi Exponentielle
├── gamma_page.py                 # Loi Gamma
├── beta_page.py                  # Loi Beta
├── uniforme_page.py              # Loi Uniforme
│
├── dashboard_final_page.py       # Tableau de bord comparatif final
│
├── requirements.txt              # Dépendances du projet
└── README.md                     # Présent fichier de documentation
```

---

## ⚙️ Installation et exécution

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/awa/Stat_Maths_Projects.git
cd Stat_Maths_Projects
```

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate  # sous Windows
# ou
source venv/bin/activate  # sous Linux / macOS
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

**Exemple de contenu de `requirements.txt` :**

```
streamlit
numpy
matplotlib
scipy
```

### 4️⃣ Lancer l’application

```bash
streamlit run app.py
```

Puis ouvre le lien généré (souvent : [http://localhost:8501](http://localhost:8501)) dans ton navigateur.

---

## 🧮 Exemple de formules intégrées

Quelques exemples rendus en LaTeX :

* **Loi de Poisson :**
  \( P(X = k) = \dfrac{\lambda^k e^{-\lambda}}{k!} \)

* **Loi Exponentielle :**
  \( f(x) = \lambda e^{-\lambda x}, \quad x \ge 0 \)

* **Loi Uniforme :**
  \( f(x) = \dfrac{1}{b - a}, \quad a \le x \le b \)

---

## 📸 Captures d’écran

*(À compléter par Awa après exécution du projet — par exemple :)*

```
📍 Poisson_page.png
📍 Exponentielle_page.png
📍 Uniforme_page.png
📍 Dashboard_final_page.png
```

---

## 🌈 Points forts du projet

✨ Interface claire et colorée
✨ Explications mathématiques intégrées
✨ Expérience utilisateur interactive
✨ Visualisation instantanée des variations des paramètres
✨ Adapté à l’enseignement et à l’auto-apprentissage

---

## 🧠 Objectif pédagogique

Ce projet permet aux étudiants et passionnés de statistique de :

* Comprendre intuitivement la forme et les propriétés des lois de probabilité.
* Visualiser les effets des paramètres sur les distributions.
* Expérimenter par la simulation Monte-Carlo.
* Acquérir des bases solides en analyse probabiliste.

---

## 💡 Améliorations futures

🔹 Ajouter la **loi normale** et la **loi du Khi-deux**
🔹 Créer un **mode test interactif**
🔹 Ajouter des **explications audio et vidéos**
🔹 Déployer sur **Streamlit Cloud** avec authentification utilisateur

---

## 📬 Contact

👩‍💻 **Auteur :** Awa
📧 **Email :** [awa.dev@gmail.com](mailto:awa.dev@gmail.com) *(à remplacer par ton vrai mail)*
🔗 **Portfolio :** [https://awa-portfolio.github.io](https://awa-portfolio.github.io)
💼 **LinkedIn :** [https://linkedin.com/in/awa](https://linkedin.com/in/awa)

---

## 🏁 Citation

> “Les statistiques ne sont pas des chiffres froids,
> mais des outils puissants pour comprendre le monde.”
> — *Awa, Data Enthusiast*

---

Souhaites-tu que je t’ajoute une **section "Déploiement sur Streamlit Cloud"** (avec le token, le `secrets.toml`, et les étapes précises) pour le rendre encore plus complet ?
