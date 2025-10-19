import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def show():
    st.header("🏨 Durée d’hospitalisation (Gamma)")
    st.info("Simulation dynamique avec interprétation automatique.")

    # Paramètres interactifs
    k = st.slider("📌 Paramètre k (forme)", 1, 10, 2)
    theta = st.slider("📌 Paramètre θ (échelle)", 1, 10, 6)
    n = st.slider("📌 Nombre de patients simulés", 50, 1000, 200)

    # Simulation
    data = np.random.gamma(k, theta, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="#a1d6e2", edgecolor="#05386b", alpha=0.7, density=True, label="Simulation")
    x = np.linspace(0, max(data), 200)
    ax.plot(x, stats.gamma.pdf(x, a=k, scale=theta), "r-", lw=2, label="Théorie Gamma")
    ax.set_title("📊 Durée des séjours hospitaliers", fontsize=16, color="#05386b")
    ax.set_xlabel("Durée (jours)")
    ax.set_ylabel("Densité")
    ax.legend()
    st.pyplot(fig)

    # Résultats dynamiques
    st.subheader("📌 Résultats numériques")
    st.write(f"👉 Durée moyenne observée : **{moyenne_obs:.2f} jours**")
    st.write(f"👉 Variance observée : **{variance_obs:.2f}**")
    st.write(f"👉 Paramètre de forme k = {k}")
    st.write(f"👉 Paramètre d’échelle θ = {theta}")

# Interprétation dynamique
    st.subheader("🧐 Interprétation dynamique")
    st.markdown(f"""
    ### 1️⃣ Signification des indicateurs
    - **Durée moyenne ({moyenne_obs:.2f} jours)**  
    → C’est la **durée moyenne d’hospitalisation** d’un patient.  
    Elle indique le **temps typique d’occupation d’un lit** dans le service.

    - **Variance ({variance_obs:.2f})**  
    → Mesure la **variabilité des durées de séjour**.  
    - **Faible variance (< 2)** : la majorité des patients restent une durée similaire (bonne stabilité).  
    - **Forte variance (> 5)** : certains patients restent beaucoup plus longtemps, signe de **cas complexes**.

    - **Paramètre de forme (k = {k})**  
    → Reflète la **régularité** des séjours.  
    - Si **k < 1** → beaucoup de séjours très courts, mais aussi quelques très longs : service d’urgences typique.  
    - Si **k ≈ 2–5** → séjour modéré et régulier : médecine générale, chirurgie standard.  
    - Si **k > 5** → séjours très homogènes : hospitalisation planifiée ou soins standardisés.

    - **Paramètre d’échelle (θ = {theta})**  
    → Influence la **durée moyenne** des hospitalisations.  
    Une valeur élevée de θ (> 2) indique des **séjours longs** nécessitant **plus de ressources**.

    ---

    ### 2️⃣ Interprétation médicale et opérationnelle
    | Paramètre | Interprétation clinique | Implication pratique |
    |------------|-------------------------|----------------------|
    | k faible (< 1) | Patients hétérogènes, flux imprévisible | ⚠️ Besoin d’une gestion flexible et d’un service d’urgence performant |
    | k modéré (2–5) | Patients avec durées moyennes stables | ✅ Bonne planification des lits possible |
    | k élevé (> 5) | Séjours réguliers et prévisibles | 📅 Optimiser la rotation des lits et anticiper les sorties |
    | θ élevé (> 2) | Longues hospitalisations | 🛏️ Risque de saturation des lits, prévoir renforts médicaux |
    | θ faible (< 1) | Séjours courts | 🚀 Service dynamique, libération rapide des lits |

    ---


    ### 3️⃣ Recommandations de gestion
    - **Si la moyenne dépasse 10 jours et que la variance est > 5** → mettre en place un **suivi post-hospitalisation** pour accélérer les sorties.  
    - **Si k < 1** → améliorer la **triage initiale** pour mieux répartir les patients selon la gravité.  
    - **Si θ > 2** → envisager un **renforcement du personnel de rééducation** ou de **suivi des cas lourds**.  
    - **Surveiller mensuellement** l’évolution de k et θ pour détecter les changements de profil patient.

    ---

    ### 4️⃣ Conclusion décisionnelle
    > La **loi Gamma** permet d’identifier la **structure de la durée des séjours hospitaliers**.  
    > En analysant k et θ, les responsables peuvent **prévoir la demande en lits**, **réduire les engorgements**,  
    > et **améliorer la fluidité du parcours patient** tout en maintenant la qualité des soins.
    """)
