# you can run a streamlit file after installing it with "pip install streamlit"
# for example "streamlit run streamlit_skeleton.py"
import streamlit as st
import pandas as pd
import numpy as np 

st.markdown("# DOPP3")
st.markdown("## Data Preparation")

### caching stuff must happen in a func
@st.cache
def load_migration_by_dest():
    migration_by_dest = pd.read_csv("data/clean/migration_by_destination_and_origin.csv", sep=";" 
#    , error_bad_lines=False
    , na_values=''
    , encoding="cp1252")
    return migration_by_dest

migration_by_dest = load_migration_by_dest()

st.write(migration_by_dest)

st.balloons()