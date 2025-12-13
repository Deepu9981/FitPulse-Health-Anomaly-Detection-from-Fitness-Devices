import streamlit as st
import pandas as pd

st.title("FIT Band Data")

uploaded_file = st.file_uploader("Upload CSV or JSON", type=["csv", "json"])

def preprocess(df):
    # Example preprocessing
    df = df.dropna()
    return df

if uploaded_file:
    raw_df = (
        pd.read_csv(uploaded_file)
        if uploaded_file.name.endswith("csv")
        else pd.read_json(uploaded_file)
    )

    st.subheader("Uploaded Raw Data")
    st.dataframe(raw_df)

    if st.button("Preprocess Data"):
        with st.spinner("Processing data..."):
            cleaned_df = preprocess(raw_df)

        st.subheader("Cleaned Data")
        st.dataframe(cleaned_df)

        csv = cleaned_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Cleaned CSV", csv, "cleaned_data.csv")


for backend -https://huggingface.co/spaces/Deepu04/Fitpulse/resolve/main/backend.py
