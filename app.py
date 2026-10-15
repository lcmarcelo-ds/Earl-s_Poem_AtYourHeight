from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='At Your Height · For Earl', page_icon='✦', layout='wide')
st.markdown('''<style>
.stApp {background:#101f2a;}
.block-container {padding-top:1rem;padding-bottom:0;max-width:1250px;}
@media(max-width:760px){.block-container{padding-left:0.4rem;padding-right:0.4rem;}}
</style>''', unsafe_allow_html=True)
with st.expander('♫ A soundtrack for these words · press play', expanded=True):
    st.video('https://www.youtube.com/watch?v=R1_573KxH2w')
    st.caption('Start the music, then take your time with the poem. Pause it before using Listen for a clearer reading.')
    st.markdown('[Open the song on YouTube ↗](https://www.youtube.com/watch?v=R1_573KxH2w)')
page = Path(__file__).with_name('index.html').read_text(encoding='utf-8')
components.html(page, height=1100, scrolling=True)
