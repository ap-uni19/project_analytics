import streamlit as st
import os

# Verzeichnisse
plotly_dir = "../references/plotly"
matplotlib_dir = "../references/matplotlib"

# Plotly-Visualisierungen mit Dropdown
def display_plotly_visualizations_with_png():
    st.header("Explorative Datenanalyse (EDA)")

    html_files = sorted(
        [file for file in os.listdir(plotly_dir) if file.endswith(".html")],
        key=lambda x: os.path.getmtime(os.path.join(plotly_dir, x))
    )
    png_file = "01_korrelationsmatrix.png"  # Spezifische PNG-Datei

    # Kombinierte Liste für Dropdown-Menü
    visualization_options = html_files + [png_file]

    # Dropdown-Menü
    selected_visualization = st.selectbox(
        "Wähle eine Visualisierung aus:",
        options=visualization_options,
        format_func=lambda x: x.replace('_', ' ').replace('.html', '').replace('.png', '')  # Anzeigename verbessern
    )

    # Anzeige der ausgewählten Visualisierung
    if selected_visualization.endswith(".html"):
        file_path = os.path.join(plotly_dir, selected_visualization)
        try:
            with open(file_path, "r") as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=1500, width=900)
        except FileNotFoundError:
            st.error(f"Die Datei '{selected_visualization}' konnte nicht gefunden werden.")
    elif selected_visualization == png_file:
        file_path = os.path.join(matplotlib_dir, png_file)
        if os.path.exists(file_path):
            st.image(file_path, use_container_width=True)
        else:
            st.error(f"Die Datei '{png_file}' konnte nicht gefunden werden.")

# Matplotlib-Bildern
def display_matplotlib_visualizations():
    st.header("Ergbnisse Modelle")
    png_files = sorted(
        [file for file in os.listdir(matplotlib_dir) if file.endswith(".png") and file != "01_korrelationsmatrix.png"],
        key=lambda x: os.path.getmtime(os.path.join(matplotlib_dir, x))
    )
    if not png_files:
        st.warning("Keine Matplotlib-Bilder gefunden.")
        return

    for file in png_files:
        file_path = os.path.join(matplotlib_dir, file)
        st.markdown(f"### {file.replace('_', ' ').replace('.png', '')}")
        st.image(file_path, use_container_width=True)

# Sidebar-Navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Seite auswählen", ["Einführung", "EDA", "Modelle", "Über"])

# Sidebar Logik
if page == "Einführung":
    st.header("Fussball-Martkwerte vorhersagen")
elif page == "EDA":
    display_plotly_visualizations_with_png()
elif page == "Modelle":
    display_matplotlib_visualizations()
elif page == "Über":
    st.header("Über die Webseite")
    st.write("Autor: Antonino Piloro")
    st.write("Diese Webseite zeigt Ergebnisse des Projektes, zur Vorhersage von Fussball-Martkwerte, welche sich in Powerpoint, explorativen Datenanalyse (EDA) und der Modellierung untertzeilt.")
    st.write("Zusätzlich können Sie den Bericht im PDF-Format und die Powerpoint herunterladen.")

# Download-Button für PDF PowerPoint
st.sidebar.download_button(
    label="PDF herunterladen",
    data=open('report.pdf', 'rb').read(),
    file_name='report.pdf',
    mime='application/pdf'
)
