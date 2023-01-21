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


default_text = """
During the year Miss Densmore arranged in final order 245 songs to accompany her manuscript on Seminole music and revised portions of the text to conform to this arrangement of the material. 

In December 1941 Miss Densmore was appointed as consultant at The National Archives for work in connection with the Smithsonian Densmore collection of sound recordings of American Indian music, and duiing the ensuing months she was engaged in planning the organization of the collection.
"""

project_data = toml.load("project.toml")
text = st.text_area("Paste Text Here", value=default_text, height=100)

nlp = load_model()
doc = nlp.process_doc(text)
doc = nlp.coref_resolution()
visualize_spans(doc, spans_key="ruler", displacy_options={"colors": project_data["colors"]})