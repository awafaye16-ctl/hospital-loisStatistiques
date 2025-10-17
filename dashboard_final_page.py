# dashboard_final_page.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, expon, binom, geom, gamma, beta

# Fonction principale pour la page Dashboard Final
def show():
    st.header("📑 Dashboard Final - Synthèse Globale")
    st.info("Ce tableau de bord récapitule tous les modules et résultats simulés pour le service hospitalier.")

    st.subheader("1️⃣ Paramètres simulés pour chaque loi")
    # Sliders pour reprendre ou ajuster les paramètres de simulation
    n_patients = st.slider("Nombre de patients simulés (pour tous les modules)", 50, 500, 100)

    # Paramètres exemples (on peut les relier aux sliders des modules)
    lambda_poisson = st.slider("📌 Arrivées moyennes (Poisson) λ", 1, 20, 5)
    theta_expon = st.slider("📌 Durée moyenne entre arrivées (Exponentielle) θ", 0.5, 10.0, 2.0)
    p_binom = st.slider("📌 Probabilité cas graves (Binomiale) p", 0.01, 1.0, 0.2)
    k_gamma = st.slider("📌 Paramètre forme hospitalisation (Gamma) k", 0.5, 10.0, 2.0)
    theta_gamma = st.slider("📌 Paramètre échelle hospitalisation (Gamma) θ", 0.5, 20.0, 6.0)
    alpha_beta = st.slider("📌 Paramètre α taux succès (Beta)", 1, 20, 5)
    beta_beta = st.slider("📌 Paramètre β taux succès (Beta)", 1, 20, 5)

    st.markdown("---")

    st.subheader("2️⃣ Simulation et KPIs")
    # Simulation Poisson - arrivées
    arrivals = poisson.rvs(mu=lambda_poisson, size=n_patients)
    mean_arrivals = np.mean(arrivals)

    # Simulation Exponentielle - temps d'attente
    waiting_times = expon.rvs(scale=theta_expon, size=n_patients)
    mean_waiting = np.mean(waiting_times)

    # Simulation Binomiale - cas graves
    cases_graves = binom.rvs(n=1, p=p_binom, size=n_patients)
    mean_graves = np.mean(cases_graves)

    # Simulation Gamma - durée hospitalisation
    stays = gamma.rvs(a=k_gamma, scale=theta_gamma, size=n_patients)
    mean_stay = np.mean(stays)
    var_stay = np.var(stays)

    # Simulation Beta - taux de succès traitement
    successes = beta.rvs(a=alpha_beta, b=beta_beta, size=n_patients)
    mean_success = np.mean(successes)

    # Affichage KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("🏥 Arrivées moyennes", f"{mean_arrivals:.2f} patients")
    col2.metric("⏱️ Temps moyen attente", f"{mean_waiting:.2f} jours")
    col3.metric("⚕️ Cas graves moyen", f"{mean_graves:.2f}")

    col4, col5 = st.columns(2)
    col4.metric("🏨 Durée moyenne séjour", f"{mean_stay:.2f} jours")
    col5.metric("💊 Taux succès moyen", f"{mean_success:.2f}")

    st.markdown("---")

    st.subheader("3️⃣ Graphiques combinés")
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("📊 Distributions simulées par module", fontsize=18)

    # Poisson
    axs[0,0].hist(arrivals, bins=15, color="#a6cee3", edgecolor="#1f78b4", alpha=0.7)
    axs[0,0].set_title("🏥 Arrivées (Poisson)")
    axs[0,0].set_xlabel("Nombre d'arrivées")
    axs[0,0].set_ylabel("Fréquence")

    # Exponentielle
    axs[0,1].hist(waiting_times, bins=15, color="#b2df8a", edgecolor="#33a02c", alpha=0.7)
    axs[0,1].set_title("⏱️ Attente (Exponentielle)")
    axs[0,1].set_xlabel("Temps d'attente")
    axs[0,1].set_ylabel("Fréquence")

    # Binomiale
    axs[0,2].hist(cases_graves, bins=2, color="#fb9a99", edgecolor="#e31a1c", alpha=0.7)
    axs[0,2].set_title("⚕️ Cas graves (Binomiale)")
    axs[0,2].set_xlabel("0=Non, 1=Oui")
    axs[0,2].set_ylabel("Fréquence")

    # Géométrique
    exams = geom.rvs(p=0.3, size=n_patients)
    axs[1,0].hist(exams, bins=15, color="#fdbf6f", edgecolor="#ff7f00", alpha=0.7)
    axs[1,0].set_title("🧪 Examens (Géométrique)")
    axs[1,0].set_xlabel("Nombre d'examens")
    axs[1,0].set_ylabel("Fréquence")

    # Gamma
    axs[1,1].hist(stays, bins=15, color="#cab2d6", edgecolor="#6a3d9a", alpha=0.7)
    axs[1,1].set_title("🏨 Durée séjour (Gamma)")
    axs[1,1].set_xlabel("Durée (jours)")
    axs[1,1].set_ylabel("Fréquence")

    # Beta
    axs[1,2].hist(successes, bins=15, color="#ffff99", edgecolor="#b15928", alpha=0.7)
    axs[1,2].set_title("💊 Taux succès (Beta)")
    axs[1,2].set_xlabel("Probabilité succès")
    axs[1,2].set_ylabel("Fréquence")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    st.pyplot(fig)

    st.markdown("---")

    st.subheader("4️⃣ Interprétation dynamique globale")
    st.markdown(f"""
- **Arrivées moyennes** : {mean_arrivals:.2f} → nombre moyen de patients par période.  
- **Temps moyen attente** : {mean_waiting:.2f} jours → si élevé, prévoir renfort personnel.  
- **Cas graves moyen** : {mean_graves:.2f} → planifier lits et interventions spécifiques.  
- **Durée moyenne séjour** : {mean_stay:.2f} jours, variance = {var_stay:.2f} → lits à prévoir pour courts et longs séjours.  
- **Taux succès moyen** : {mean_success:.2f} → suivi de l’efficacité des traitements.  
- **Examens (Géométrique)** : nombre moyen = {np.mean(exams):.2f} → impact sur temps de diagnostic et ressources.  

👉 Ce dashboard final permet de visualiser **tous les modules** et d’anticiper **la capacité hospitalière et la charge de travail**, de façon claire et interactive.
""")
