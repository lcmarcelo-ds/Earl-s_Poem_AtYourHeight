from pathlib import Path
import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="At Your Height · For Earl", page_icon="✦", layout="wide")
st.markdown("""<style>
.stApp {background:#101f2a;}
.block-container {padding-top:1rem;padding-bottom:0;max-width:1250px;}
@media(max-width:760px){.block-container{padding-left:0.4rem;padding-right:0.4rem;}}
</style>""", unsafe_allow_html=True)
root = Path(__file__).resolve().parent

@st.cache_data(show_spinner=False)
def load_page(html_bytes, audio_bytes):
    audio = base64.b64encode(audio_bytes).decode("ascii")
    return html_bytes.decode("utf-8").replace("__SOUNDTRACK_DATA__", audio)

page = load_page((root / "index.html").read_bytes(), (root / "soundtrack.mp3").read_bytes())
components.html(page, height=1200, scrolling=True)
