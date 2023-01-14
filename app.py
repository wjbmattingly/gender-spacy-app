import streamlit as st
from spacy_streamlit import visualize_spans
import spacy
import toml
from gender_spacy import gender_spacy as gs

@st.cache(allow_output_mutation=True)
def load_model():
    nlp = gs.GenderParser("en_core_web_sm")
    return nlp

st.image("https://github.com/sidatasciencelab/gender-spacy/raw/main/images/genderspacy-logo.png")

st.markdown("Currently using version: <a href='https://pypi.org/project/gender-spacy/'>![PyPI - PyPi](https://img.shields.io/pypi/v/gender-spacy)</a>", unsafe_allow_html=True)


project_data = toml.load("project.toml")
text = st.text_area("Paste Text Here", value="Harry Potter was the main character. He was only 11.", height=100)

nlp = load_model()
doc = nlp.process_doc(text)
visualize_spans(doc, spans_key="ruler", displacy_options={"colors": project_data["colors"]})