import streamlit as st
import pandas as pd
import json

# Load data
with open('data/books.json', 'r') as f:
    books_data = json.load(f)

df = pd.DataFrame(books_data)

# Streamlit UI
st.title("📚 Books to Scrape Viewer")
st.write("Data scraped dari https://books.toscrape.com/")

# Filter
rating_filter = st.selectbox("Filter berdasarkan rating", options=["All"] + sorted(df["rating"].unique()))
availability_filter = st.checkbox("Hanya tampilkan buku yang tersedia")

filtered_df = df.copy()

if rating_filter != "All":
    filtered_df = filtered_df[filtered_df["rating"] == rating_filter]

if availability_filter:
    filtered_df = filtered_df[filtered_df["availability"].str.contains("In stock")]

st.dataframe(filtered_df)
