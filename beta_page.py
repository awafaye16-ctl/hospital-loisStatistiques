import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def show():
    st.header("💊 Taux de succès d'un traitement (Beta)")
    st.info("Simulation de la probabilité de succès d’un traitement.")

    # Paramètres
    a = st.slider("📌 Paramètre a (succès +1)", 1, 20, 5)
    b = st.slider("📌 Paramètre b (échecs +1)", 1, 20, 3)
    n = st.slider("📌 Nombre de simulations", 50, 1000, 200)

    # Simulation
    data = np.random.beta(a, b, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="#cce0ff", edgecolor="#003366", alpha=0.7, density=True)
    x = np.linspace(0, 1, 200)
    ax.plot(x, beta.pdf(x, a, b), 'r-', lw=2, label="Théorie Beta")
    ax.set_title("📊 Distribution taux de succès", fontsize=16, color="#003366")
    ax.set_xlabel("Taux de succès")
    ax.set_ylabel("Densité")
    ax.legend()
    st.pyplot(fig)
        # Résultats
    st.subheader("📊 Résultats numériques")
    st.write(f"👉 Moyenne observée : {moyenne_obs:.2f}")
    st.write(f"👉 Variance observée : {variance_obs:.4f}")
    st.write(f"👉 Paramètres : a = {a}, b = {b}")

# --- Interprétation automatique ---
    if moyenne_obs < 0.4:
        niveau_moyenne = "⚠️ Faible efficacité — le traitement échoue souvent."
    elif 0.4 <= moyenne_obs < 0.7:
        niveau_moyenne = "🟡 Efficacité moyenne — résultats mitigés selon les patients."
    else:
        niveau_moyenne = "✅ Bonne efficacité — la majorité des patients réagissent positivement."

    if variance_obs < 0.02:
        niveau_variance = "🔹 Faible variance — les patients réagissent de manière homogène."
    elif 0.02 <= variance_obs < 0.1:
        niveau_variance = "🟨 Variance modérée — quelques différences dans les réponses."
    else:
        niveau_variance = "🔴 Variance élevée — forte hétérogénéité entre patients, protocole à ajuster."

# --- Interprétation dynamique ---
    st.subheader("🧠 Interprétation dynamique")
    st.markdown(f"""
    - **Moyenne ({moyenne_obs:.2f})** : {niveau_moyenne}  
    - **Variance ({variance_obs:.4f})** : {niveau_variance}  
    - **Paramètres a={a}, b={b}** : indiquent la balance entre succès (a) et échecs (b).  
    """)

# --- Conseils pratiques ---
    st.markdown("""
    ### 💡 Recommandations médicales
    - Si la variance est **élevée**, il est conseillé d’ajuster le protocole selon les profils de patients.  
    - Si la moyenne est **faible**, envisager une réévaluation du traitement ou une combinaison thérapeutique.  
    - Ces indicateurs peuvent aider à **optimiser la gestion des ressources** et **améliorer la prise de décision clinique**.
    """)
