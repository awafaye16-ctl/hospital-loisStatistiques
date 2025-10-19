import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def show():
    st.header("🧪 Nombre d’examens avant succès (Géométrique)")
    st.info("Simulation du nombre d’examens nécessaires pour diagnostiquer.")

    # Paramètres
    p = st.slider("📌 Probabilité de succès par examen", 0.01, 1.0, 0.3)
    n = st.slider("📌 Nombre de patients simulés", 50, 500, 200)

    # Simulation
    data = np.random.geometric(p, n)
    moyenne_obs = np.mean(data)
    variance_obs = np.var(data)

    # Graphique
    fig, ax = plt.subplots()
    ax.hist(data, bins=range(1, max(data)+2), color="#d0f0c0", edgecolor="#006400", alpha=0.7, density=True)
    ax.set_title("📊 Distribution du nombre d’examens", fontsize=16, color="#006400")
    ax.set_xlabel("Nombre d’examens")
    ax.set_ylabel("Probabilité")
    st.pyplot(fig)

   # Résultats
    st.subheader("📌 Résultats numériques")
    st.write(f"👉 Moyenne observée : **{moyenne_obs:.2f} examens**")
    st.write(f"👉 Variance observée : **{variance_obs:.2f}**")
    st.write(f"👉 Probabilité de succès p = **{p}**")

    # Interprétation dynamique
    st.subheader("🧐 Interprétation dynamique")
    st.markdown(f"""
    ### 1️⃣ Signification des indicateurs

    - **Moyenne ({moyenne_obs:.2f})**  
    → Nombre moyen d’examens réalisés avant d’obtenir un résultat concluant (diagnostic confirmé ou test positif).  
    Si la moyenne est **élevée (> 4)**, cela signifie que les patients nécessitent plusieurs examens avant une détection fiable — ce qui indique **une complexité diagnostique**.

    - **Variance ({variance_obs:.2f})**  
    → Mesure la variabilité du nombre d’examens nécessaires :  
    - **Faible variance (< 2)** : les patients suivent un schéma stable de diagnostic.  
    - **Forte variance (> 5)** : certains cas nécessitent beaucoup plus d’examens → possible manque de protocoles ou cas rares.

    - **Probabilité de succès (p = {p})**  
    → Représente la probabilité qu’un examen soit concluant.  
    - **p élevé (> 0.6)** : tests fiables, diagnostics rapides.  
    - **p moyen (0.3–0.6)** : fiabilité modérée, nécessite plusieurs vérifications.  
    - **p faible (< 0.3)** : faible efficacité des tests ou diagnostic difficile → besoin d’amélioration technique.

    ---

    ### 2️⃣ Interprétation clinique et opérationnelle

    | Indicateur | Interprétation médicale | Impact sur l’organisation |
    |-------------|--------------------------|----------------------------|
    | Moyenne haute (> 4) | Patients nécessitant plusieurs examens avant confirmation | ⚠️ Risque de surcharge de travail pour les laboratoires |
    | Variance forte (> 5) | Hétérogénéité des cas | 🧪 Nécessité d’un protocole plus standardisé |
    | p élevé (> 0.6) | Tests fiables, diagnostics rapides | ✅ Optimisation du flux patient |
    | p faible (< 0.3) | Diagnostic complexe ou matériel peu précis | 🔧 Besoin de renforcement technologique ou de formation |

    ---

    ### 3️⃣ Recommandations de gestion

    - **Si la moyenne dépasse 4 et la variance > 5** → revoir la **chaîne de diagnostic** pour réduire les retards.  
    - **Si p < 0.4** → investir dans des **examens plus performants** ou **former le personnel** à l’interprétation des résultats.  
    - **Surveiller mensuellement p** pour détecter les baisses de performance d’un test.  
    - **Corréler ces résultats** avec les coûts pour identifier les examens les plus rentables.

    ---

    ### 4️⃣ Conclusion décisionnelle
    > La **loi géométrique** modélise la **charge de travail diagnostique**.  
    > En suivant la moyenne, la variance et la probabilité p, les gestionnaires peuvent **optimiser les protocoles de tests**,  
    > **anticiper la demande en équipements**, et **améliorer la rapidité du diagnostic patient**.
    """)
