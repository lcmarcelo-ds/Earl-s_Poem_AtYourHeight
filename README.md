# At Your Height — Streamlit edition

An interactive poem for Earl, from Lloyd. Eight scenes, animated reveals, midnight/daylight modes, full-poem dialog, and optional browser speech. No responses or viewing analytics are collected by the app.

## Run on your computer

Use Python 3.12. Open a terminal in this extracted folder:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On Windows, you can replace `python` with `py`. Open the Local URL displayed in the terminal. Keep the terminal running while previewing; Ctrl+C stops it.

## GitHub + Streamlit Community Cloud

1. Create a GitHub repository, such as `at-your-height`.
2. Upload the contents of this folder, not the ZIP itself. Keep app.py, index.html and requirements.txt together at the repository root. Include .streamlit/config.toml for the theme.
3. Sign in at https://share.streamlit.io with your GitHub account.
4. Create an app from your repository. Select the repository and branch, then set the main file path to app.py.
5. In advanced settings select Python 3.12, then deploy.
6. Open the resulting streamlit.app link and test it on your phone before sending it to Earl.

Use Streamlit Community Cloud for hosting this version, not GitHub Pages. GitHub stores the files; Streamlit executes app.py.

## Customize

Edit the scenes array inside index.html to change the poem. Edit the header dedication to change the names. The page is embedded in a scrollable Streamlit component to preserve its isolated styles and JavaScript interactions. Streamlit is pinned to 1.54.0 for the components API used here; review component compatibility before upgrading.

The browser Listen button uses synthesized speech, not a recorded performance. Browser/phone voice availability varies. Nothing plays automatically. Navigation stops playback, and reduced-motion preferences are respected.

No private messages, patient information, photos, or workplace identifiers are included. Check your deployment visibility before sharing; anyone allowed to access the app can read the poem.

## Validation

Python syntax and Streamlit AppTest execution are checked when supported by the build environment. Browser visual and speech checks must be completed on the deployed app; synthesized audio depends on the viewing device.

## Soundtrack

An optional YouTube player above the poem embeds the video selected by Lloyd: https://www.youtube.com/watch?v=R1_573KxH2w . Press play to start it. Playback requires internet and depends on YouTube availability and the uploader permitting embedding. An Open on YouTube link is included as a fallback. No audio is downloaded or bundled. Pause music manually before using the poem read-aloud; automatic ducking is not implemented. YouTube may show ads or require interaction. Mobile background playback is not guaranteed.
