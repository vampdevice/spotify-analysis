# imports
import streamlit as st
import pandas as pd
import plotly.express as px

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

fig = px.bar(
    df,
    x="track_genre",
    y="popularity",
    color="danceability",
    hover_data=["track_name", "artists"],
    height=450,
)
st.plotly_chart(fig, use_container_width=True)

genre = st.selectbox("Genre", sorted(df["track_genre"].unique()))
filtered = df[df["track_genre"] == genre]

fig = px.scatter(
    filtered,
    x="danceability",
    y="popularity",
    color="energy",
    hover_data=["track_name", "artists"],
    height=450,
)
st.plotly_chart(fig, use_container_width=True)

st.write(f"**{len(filtered)}** tracks in *{genre}*.")
st.dataframe(filtered, use_container_width=True)