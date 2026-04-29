# imports
import streamlit as st
import pandas as pd
import plotly.express as px

# configure page layout to give room for columns
st.set_page_config(layout="wide")
st.title("&#127926; Spotify Explorer", text_alignment="left")

# read in dataset
data = pd.read_csv("data/dataset.csv")

# data cleaning before visualization
df = data.copy()
df = df.drop(columns=["Unnamed: 0"])

# handle missing values
df = df.dropna(subset=['artists', 'album_name', 'track_name'])

# drop only exact duplicates
df = df.drop_duplicates()

col1, col2 = st.columns(2)

with col1:
    st.write(f"Loaded **{len(df)}** tracks.")
    st.dataframe(df, use_container_width=True, height=450)

    fig = px.bar( 
        df,
        title="Track Genres Ranked by Popularity",
        x="track_genre",
        y="popularity",
        color="danceability",
        color_continuous_scale=["#ffffff", "#1ED760"],
        hover_data=["track_name", "artists"],
        height=450,
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    genre = st.selectbox("Genre", sorted(df["track_genre"].unique()))
    filtered = df[df["track_genre"] == genre]

    st.write(f"**{len(filtered)}** tracks in *{genre}*.")
    st.dataframe(filtered, use_container_width=True, height=366)

    fig = px.scatter(
        filtered,
        title="Popularity vs. Danceability",
        x="danceability",
        y="popularity",
        color="energy",
        color_continuous_scale=["#ffffff", "#1ED760"],
        hover_data=["track_name", "artists"],
        height=450,
)
    st.plotly_chart(fig, use_container_width=True)