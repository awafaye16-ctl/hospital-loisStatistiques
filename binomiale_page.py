import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def show():
    st.header("⚠️ Cas graves (Bernoulli/Binomiale)")
    st.info("Simulation de la proportion de patients graves.")

    st.markdown("<hr style='border:1px solid #0078A8;'>", unsafe_allow_html=True)


    # Paramètres
    p = st.slider("📌 Probabilité qu'un patient soit grave", 0.01, 1.0, 0.2)
    n = st.slider("📌 Nombre de patients par jour", 10, 500, 100)
    jours = st.slider("📌 Nombre de jours simulés", 10, 100, 50)

    # Simulation
    data = np.random.binomial(n, p, jours)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=range(0, max(data)+2), color="#ffd699", edgecolor="#ff6f00", alpha=0.7, density=True)
    x = np.arange(0, max(data)+1)
    ax.plot(x, binom.pmf(x, n, p), 'r-', lw=2, label="Théorie Binomiale")
    ax.set_title("📊 Nombre de cas graves", fontsize=16, color="#ff6f00")
    ax.set_xlabel("Nombre de cas graves")
    ax.set_ylabel("Probabilité")
    ax.legend()
    st.pyplot(fig)

        # ===============================
# 📊 MODULE : Loi Binomiale
# Objectif : Analyser la fréquence des cas graves dans un service hospitalier
# ===============================

    st.subheader("📌 Résultats numériques")
    st.write(f"👉 Moyenne observée : {moyenne_obs:.2f}")
    st.write(f"👉 Variance observée : {variance_obs:.2f}")
    st.write(f"👉 Probabilité de gravité p = {p}")

# --- Interprétation automatique des résultats ---
# La moyenne représente le nombre moyen de cas graves (ex: par jour)
# La variance montre à quel point ce nombre varie d’un jour à l’autre

# Interprétation de la moyenne
    if moyenne_obs < 2:
        interpretation_moy = "🟢 Faible nombre de cas graves — la situation est stable et maîtrisée."
    elif 2 <= moyenne_obs < 5:
        interpretation_moy = "🟡 Niveau modéré — surveillance recommandée, fluctuations possibles."
    else:
        interpretation_moy = "🔴 Niveau élevé — risque de saturation du service, nécessite un renfort médical."

# Interprétation de la variance
    if variance_obs < 1:
        interpretation_var = "🔹 Variance faible — les cas graves sont réguliers et prévisibles."
    elif 1 <= variance_obs < 4:
        interpretation_var = "🟨 Variance moyenne — certaines journées plus chargées que d’autres."
    else:
        interpretation_var = "🔴 Variance élevée — forte instabilité, pics soudains de cas graves."

# Interprétation du paramètre p
    if p < 0.2:
        interpretation_p = "🧊 Probabilité faible — peu de cas graves parmi les patients hospitalisés."
    elif 0.2 <= p < 0.5:
        interpretation_p = "⚖️ Probabilité moyenne — les cas graves représentent une part notable du flux."
    else:
        interpretation_p = "🔥 Probabilité forte — la gravité est fréquente, renforcer la vigilance clinique."

# --- Interprétation dynamique (médicale et analytique) ---
    st.subheader("🧠 Interprétation dynamique")
    st.markdown(f"""
    - **Moyenne ({moyenne_obs:.2f})** : {interpretation_moy}  
    - **Variance ({variance_obs:.2f})** : {interpretation_var}  
    - **Probabilité p = {p}** : {interpretation_p}  

    🩺 **Lecture médicale :**  
    Ce modèle binomial permet d’anticiper le nombre de **cas graves journaliers** en fonction de la probabilité d’occurrence.  
    Une moyenne élevée combinée à une variance forte indique un **risque de surcharge hospitalière**, tandis qu’une moyenne stable et une variance faible traduisent un **équilibre opérationnel**.

    💡 **Application pratique :**  
    - Planification du personnel médical (médecins, infirmiers, réanimateurs).  
    - Anticipation des lits en soins intensifs.  
    - Surveillance épidémiologique en période de pic d’activité.
    """)

# --- Recommandations automatiques selon le niveau ---
    if moyenne_obs > 5 or p > 0.5:
        st.warning("🚨 Recommandation : Activer un plan d’urgence ou renforcer les équipes de soins intensifs.")
    elif moyenne_obs < 2 and variance_obs < 1:
        st.success("✅ Situation stable : maintien du protocole actuel et suivi régulier suffisent.")
    else:
        st.info("ℹ️ Suivi recommandé : surveiller les variations quotidiennes et ajuster les ressources si besoin.")
