import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def show():
    st.header("🏥 Arrivées des patients (Poisson)")
    st.info("Simulation du nombre d’arrivées de patients par jour.")
        
    # --- Titre principal ---
    st.markdown("<h2 class='title-hospital'>🏥 Loi de Poisson — Arrivées des patients</h2>", unsafe_allow_html=True)

    st.markdown("""
    Cette section permet de **modéliser le flux d’arrivées des patients**  
    dans un service hospitalier à l’aide de la **loi de Poisson**, qui représente  
    le **nombre d’événements aléatoires (arrivées)** sur une période donnée ⏱️.
    """)


    # Paramètres
    lam = st.slider("📌 Nombre moyen d'arrivées λ", 1, 50, 10)
    n = st.slider("📌 Nombre de jours simulés", 10, 365, 100)

    # Simulation
    data = np.random.poisson(lam, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=range(0, max(data)+2), color="#a1d6e2", edgecolor="#05386b", alpha=0.7, density=True)
    x = np.arange(0, max(data)+1)
    ax.plot(x, poisson.pmf(x, lam), 'r-', lw=2, label="Théorie Poisson")
    ax.set_title("📊 Distribution des arrivées", fontsize=16, color="#05386b")
    ax.set_xlabel("Nombre d'arrivées")
    ax.set_ylabel("Probabilité")
    ax.legend()
    st.pyplot(fig)

        # --- Résultats numériques ---
    st.markdown("<div class='section-title'>📌 Résultats numériques</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-box'><b>Moyenne</b><br>{moyenne_obs:.2f}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-box'><b>Variance</b><br>{variance_obs:.2f}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-box'><b>Paramètre λ</b><br>{lam}</div>", unsafe_allow_html=True)

    # --- Interprétation dynamique ---
    st.markdown("<div class='section-title'>🧐 Interprétation clinique et décisionnelle</div>", unsafe_allow_html=True)

    st.markdown(f"""
    | Indicateur | Interprétation médicale | Impact sur la gestion |
    |-------------|--------------------------|------------------------|
    | **Moyenne ({moyenne_obs:.2f})** | Nombre typique de patients reçus par jour | 🧾 Aide à estimer le flux moyen quotidien |
    | **Variance ({variance_obs:.2f})** | Mesure l’irrégularité du flux patient | 📅 Si élevée → journées de forte affluence imprévisibles |
    | **Paramètre λ = {lam}** | Intensité moyenne d’arrivées | 👩‍⚕️ Plus λ est grand → plus de personnel requis |

    ---

    ### 🎯 Recommandations pratiques

    - Si **λ > 10** : prévoir un **renforcement du personnel médical** et du matériel d’accueil.  
    - Si **variance > moyenne**, le service connaît de **fortes fluctuations** → adapter les horaires de travail.  
    - Si **λ < 3**, période calme : utile pour la **maintenance du matériel** et **formation du personnel**.  
    - Une **surveillance continue de λ** permet d’ajuster les ressources selon la demande réelle.

    ---

    ### 🧩 En résumé
    > La **loi de Poisson** permet de **quantifier le flux patient**  
    > et d’**anticiper les besoins en ressources hospitalières**.  
    > C’est un **outil d’aide à la décision stratégique** pour équilibrer la charge de travail,  
    > optimiser le personnel et améliorer la qualité d’accueil. 💡
    """)
