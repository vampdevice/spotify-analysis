import streamlit as st
import pandas as pd

st.title("Spotify Explorer")

data = pd.read_csv("data/dataset.csv")

# data cleaning before visualization
df = data.copy()
df = df.drop(columns=["Unnamed: 0"])

# handle missing values
df = df.dropna(subset=['artists', 'album_name', 'track_name'])

# drop only exact duplicates
df = df.drop_duplicates()

st.write(f"Loaded **{len(df)}** tracks.")
st.dataframe(df, use_container_width=True)

genre = st.selectbox("Genre", sorted(df["track_genre"].unique()))
filtered = df[df["track_genre"] == genre]

st.write(f"**{len(filtered)}** tracks in *{genre}*.")
st.dataframe(filtered, use_container_width=True)