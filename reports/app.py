import streamlit as st
import os

# Automatisches Sammeln von HTML-Dateien aus einem Verzeichnis
directory = "../references/plotly"

# Liste der Dateien in der Reihenfolge, wie sie im Verzeichnis vorkommen

html_files = sorted(
    [file for file in os.listdir(directory) if file.endswith(".html")],
    key=lambda x: os.path.getmtime(os.path.join(directory, x))
)
# Erstelle ein Wörterbuch mit den Dateinamen und Pfaden
html_file_paths = {
    os.path.splitext(file)[0]: os.path.join(directory, file)
    for file in html_files
}

# Titel der App
st.title("Explorative Datenanalyse des Projektes Fußballer-Marktwert Vorhersage ")

# Dropdown-Menü für die Visualisierungen (Reihenfolge wie im Verzeichnis)
selected_file = st.selectbox(
    "Wähle eine Visualisierung aus:",
    options=html_files,  # In ursprünglicher Reihenfolge
)

# Lade und zeige die ausgewählte HTML-Datei
file_path = html_file_paths[os.path.splitext(selected_file)[0]]
try:
    with open(file_path, "r") as file:
        html_content = file.read()

    # Dynamischer Titel basierend auf dem Dateinamen
    st.markdown(f"### {selected_file.replace('_', ' ').replace('.html', '')}")
    st.components.v1.html(html_content, height=1500,  width=900)
except FileNotFoundError:
    st.error(f"Die Datei '{file_path}' konnte nicht gefunden werden.")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Seite auswählen", ["EDA", "Modelle", "Über"])

if page == "EDA":
    st.header("EDA")
    # EDA-Inhalte hier
elif page == "Modelle":
    st.header("Modelle")
    # Modell-Inhalte hier
    directory_png = "../references/matplotlib"

    png_files = sorted(
        [ file for file in os.listdir(directory_png) if file.endswith(".png")],
        key=lambda x: os.path.getmtime(os.path.join(directory_png, x))
        )
    # Erstelle ein Wörterbuch mit den Dateinamen und Pfaden
    png_files_paths = {
        os.path.splitext(file)[0]: os.path.join(directory_png, file)
        for file in png_files
    }
    selected_file = st.selectbox(
    "Wähle eine Visualisierung aus:",
    options=html_files,  # In ursprünglicher Reihenfolge
    )
    st.title("Analyse der Ergebnisse")
    st.image(file)

else:
    st.header("Über")
    st.write("Beschreibung der Webseite")

st.download_button(
    label="PDF herunterladen",
    data=open('report.pdf', 'rb'),
    file_name='report.pdf',
    mime='text/csv'
)