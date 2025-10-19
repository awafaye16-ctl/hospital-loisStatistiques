import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def show():
    st.header("⏱ Temps entre arrivées (Loi Exponentielle)")
    st.info("Simulation du temps d’attente entre deux arrivées successives de patients dans un service hospitalier.")

    # === Paramètres ===
    lam = st.slider("📌 Taux d'arrivée λ", 0.1, 5.0, 1.0)
    n = st.slider("📌 Nombre d’intervalles simulés", 50, 500, 200)

    # === Simulation ===
    data = np.random.exponential(1 / lam, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # === Graphique ===
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="#A8E6CF", edgecolor="#1B5E20", alpha=0.8, density=True)
    x = np.linspace(0, max(data), 200)
    ax.plot(x, expon.pdf(x, scale=1 / lam), 'r-', lw=2, label="Théorie (Exponentielle)")
    ax.set_title("📊 Distribution des temps entre arrivées", fontsize=16, color="#1B5E20")
    ax.set_xlabel("Temps entre arrivées")
    ax.set_ylabel("Densité de probabilité")
    ax.legend()
    st.pyplot(fig)

    # === Résultats numériques ===
    st.markdown("---")
    st.subheader("📌 Résultats numériques")
    st.write(f"👉 Durée moyenne observée : **{moyenne_obs:.2f}**")
    st.write(f"👉 Variance observée : **{variance_obs:.2f}**")
    st.write(f"👉 Paramètre λ = **{lam:.3f}**")

    # === Interprétation dynamique ===
    st.markdown("---")
    st.subheader("🧐 Interprétation dynamique")
    st.markdown(f"""
    ### 1️⃣ Signification des indicateurs
    - **Durée moyenne ({moyenne_obs:.2f})**  
      → Représente le **temps moyen entre deux arrivées successives de patients**.  
      C’est une mesure directe du **rythme de fréquentation** du service.

    - **Variance ({variance_obs:.2f})**  
      → Évalue la **stabilité du flux d’arrivée**.  
      Une **faible variance (< 1)** indique une **bonne régularité**,  
      tandis qu’une **variance élevée (> 1)** révèle des **pics d’arrivée imprévisibles**.

    - **Taux d’arrivée λ = {lam:.3f}**  
      → Correspond au **nombre moyen de patients arrivant par unité de temps** (ex. : par heure ou par jour).  
      Formellement :  
      {r"\( \lambda = \frac{1}{\text{moyenne}} \)"}  
      - Si λ > 0.5 → arrivée **rapide** (moins de 2 unités de temps entre chaque patient).  
      - Si 0.1 ≤ λ ≤ 0.5 → flux **modéré**.  
      - Si λ < 0.1 → rythme **faible** ou **activité calme**.

    ---

    ### 2️⃣ Interprétation médicale
    - Un **λ élevé** → forte affluence : les patients arrivent **fréquemment**, le personnel doit **gérer plusieurs cas simultanément**.  
    - Un **λ modéré** → activité **stable** et **prévisible** : le service fonctionne normalement.  
    - Un **λ faible** → faible fréquentation : possible **baisse de cas** ou **sous-utilisation** du service.

    ---

    ### 3️⃣ Recommandations opérationnelles
    | Situation observée | Interprétation | Actions recommandées |
    |---------------------|----------------|----------------------|
    | λ > 0.5 | Surcharge potentielle | ⚠️ Renforcer l’équipe médicale et administrative, prioriser les urgences |
    | 0.1 ≤ λ ≤ 0.5 | Activité normale | ✅ Maintenir la répartition actuelle du personnel |
    | λ < 0.1 | Faible activité | 💤 Réévaluer les horaires, optimiser les ressources |

    ---

    ### 4️⃣ Conclusion décisionnelle
    > Le paramètre **λ** est un **indicateur clé de pression hospitalière**.  
    > Sa surveillance permet de **prévoir les pics d’activité**, d’**adapter le personnel**,  
    > et d’**optimiser la qualité et la rapidité de la prise en charge**.
    """)

