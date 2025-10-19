import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform



def show():
    st.header("📦 Variabilité aléatoire (Uniforme)")
    # --- En-tête stylisé ---
    st.markdown("""
    <div style="background-color:#e3f2fd; padding:15px; border-radius:10px; text-align:center;">
        <h2 style="color:#1565c0;">⚖️ Loi Uniforme — Répartition équilibrée des événements</h2>
        <p style="color:#424242; font-size:16px;">
        Cette loi permet de modéliser un phénomène où toutes les valeurs dans un intervalle sont <b>également probables</b>.
        Elle est idéale pour représenter des délais, durées ou mesures réparties sans biais.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Simulation de durées ou délais aléatoires non prédictibles.")

    # Paramètres
    low = st.slider("📌 Valeur minimale", 0, 50, 5)
    high = st.slider("📌 Valeur maximale", 10, 100, 30)
    n = st.slider("📌 Nombre de simulations", 50, 500, 200)

    # Simulation
    data = np.random.uniform(low, high, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="#ffd6e0", edgecolor="#b30059", alpha=0.7, density=True)
    x = np.linspace(low, high, 200)
    ax.plot(x, uniform.pdf(x, low, high-low), 'r-', lw=2, label="Théorie Uniforme")
    ax.set_title("📊 Distribution uniforme", fontsize=16, color="#b30059")
    ax.set_xlabel("Valeurs")
    ax.set_ylabel("Densité")
    ax.legend()
    st.pyplot(fig)

        # --- Résultats numériques ---
    st.subheader("📊 Résultats numériques")
    st.markdown(f"""
    <div style="background-color:#ffffff; padding:15px; border-radius:10px; box-shadow:0px 2px 6px #b0bec5;">
        <ul style="list-style-type:none; font-size:16px; color:#37474f;">
            <li>✅ <b>Moyenne observée :</b> {moyenne_obs:.2f}</li>
            <li>📈 <b>Variance observée :</b> {variance_obs:.2f}</li>
            <li>🧭 <b>Intervalle :</b> [{low}, {high}]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- Interprétation dynamique ---
    st.subheader("🩺 Interprétation et application hospitalière")
    st.markdown(f"""
    <div style="background-color:#f1f8e9; padding:20px; border-radius:10px;">
        <p style="font-size:16px; color:#2e7d32;">
        🔹 <b>Moyenne ({moyenne_obs:.2f})</b> : représente la valeur moyenne d’un paramètre stable (ex. temps d’attente, dose moyenne).
        </p>
        <p style="font-size:16px; color:#2e7d32;">
        🔹 <b>Variance ({variance_obs:.2f})</b> : indique le degré d’incertitude ou de variabilité du phénomène observé.
        Une variance faible = comportement prévisible ; élevée = fluctuations importantes.
        </p>
        <p style="font-size:16px; color:#2e7d32;">
        🔹 <b>Intervalle [{low}, {high}]</b> : définit les limites possibles du phénomène (délais, températures, durée d’attente...).
        </p>
        <hr style="border:1px solid #c5e1a5;">
        <p style="font-size:16px; color:#1b5e20;">
        💡 <b>En pratique hospitalière :</b> la loi uniforme est utile pour :
        <ul>
            <li>🔹 Estimer les <b>délais d’attente moyens</b> des patients dans une file sans priorité.</li>
            <li>🔹 Simuler des <b>temps d’exécution</b> lorsque l’incertitude est uniforme.</li>
            <li>🔹 Planifier la <b>répartition équitable des ressources</b> quand aucune heure n’est plus probable qu’une autre.</li>
        </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- Recommandation d’utilisation ---
    st.subheader("💬 Recommandations")
    st.markdown("""
    <div style="background-color:#e3f2fd; padding:15px; border-radius:10px;">
        <p style="font-size:16px; color:#0d47a1;">
        ✅ <b>Utilisez la loi uniforme</b> lorsque vous ne disposez d’aucune information privilégiée sur la probabilité d’un événement.<br>
        ⚙️ Elle est parfaite pour les <b>simulations hospitalières</b> ou les <b>études de performance</b> où chaque valeur possible a la même chance d’apparaître.
        </p>
    </div>
    """, unsafe_allow_html=True)
