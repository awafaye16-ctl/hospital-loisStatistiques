import streamlit as st
import poisson_page, exponentielle_page, binomiale_page, geom_page, gamma_page, beta_page,dashboard_final_page, uniforme_page

# --- CSS pour couleurs sophistiquées ---
st.markdown("""
<style>
body {
    background-color: #f4faff;
}
h1, h2, h3, h4 {
    color: #1f4e79;
}
.stButton>button {
    background-color: #1f78b4;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- Menu latéral ---
st.sidebar.title("🏥 Simulation hospitalière")
menu = st.sidebar.radio("Navigation", [
    "🏠 Accueil",
    "🏥 Arrivées (Poisson)",
    "⏱ Temps entre arrivées (Exponentielle)",
    "⚠️ Cas graves (Bernoulli/Binomiale)",
    "🧪 Examens (Géométrique)",
    "🏨 Hospitalisation (Gamma)",
    "💊 Taux de succès (Beta)",
    "📦 Variabilité (Uniforme)",
    "📊 Dashboard final"
])

# --- Router vers le bon module ---
if menu == "🏠 Accueil":
    st.title("🏥 Simulation Probabiliste d’un Service Hospitalier")
    
    st.markdown("""
    ### 🎯 **Bienvenue dans l’application de simulation hospitalière !**
    
    Cette application interactive a pour objectif de **modéliser et d’analyser le flux des patients** dans un service hospitalier à l’aide des principales **lois de probabilité**.  
    Elle permet de **comprendre, prévoir et optimiser** le fonctionnement d’un hôpital à travers une approche statistique rigoureuse mais intuitive.
    
    ---
    #### 🧮 **Lois statistiques utilisées**
    - **Poisson** → Modélise le **nombre d’arrivées de patients** dans un temps donné  
    - **Exponentielle** → Évalue le **temps entre deux arrivées successives**  
    - **Bernoulli / Binomiale** → Analyse la **probabilité d’occurrence de cas graves**  
    - **Géométrique** → Étudie le **nombre d’essais avant un succès** (ex : test médical positif)  
    - **Gamma** → Représente la **durée d’hospitalisation** selon la gravité des cas  
    - **Beta** → Estime le **taux de réussite** d’un traitement  
    - **Uniforme** → Mesure la **variabilité des durées d’attente ou de traitement**
    
    ---
    #### 🩺 **Pourquoi cette application ?**
    Elle illustre comment les **mathématiques appliquées à la santé** peuvent devenir un outil d’aide à la **prise de décision médicale** et à la **prévention** :
    - Anticiper la charge des urgences  
    - Optimiser la gestion des lits et du personnel  
    - Évaluer les performances et les risques liés aux traitements  
    
    ---
    👉 **Utilise le menu latéral** pour naviguer entre les modules, explorer chaque loi, visualiser les distributions et accéder au **dashboard final** pour une vue d’ensemble.
    """)



    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966488.png", width=150)

elif menu == "🏥 Arrivées (Poisson)":
    poisson_page.show()
elif menu == "⏱ Temps entre arrivées (Exponentielle)":
    exponentielle_page.show()
elif menu == "⚠️ Cas graves (Bernoulli/Binomiale)":
    binomiale_page.show()
elif menu == "🧪 Examens (Géométrique)":
    geom_page.show()
elif menu == "🏨 Hospitalisation (Gamma)":
    gamma_page.show()
elif menu == "💊 Taux de succès (Beta)":
    beta_page.show()
elif menu == "📦 Variabilité (Uniforme)":
    uniforme_page.show()
elif menu == "📊 Dashboard final":
    dashboard_final_page.show()
