# imports
import streamlit as st
import pandas as pd
import plotly.express as px

# configure page layout to give room for columns
st.set_page_config(page_title="Spotify Analysis", page_icon=":headphones:", layout="wide")
st.title(":headphones: Spotify Analysis Explorer", text_alignment="left")

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
    # display the loaded tracks in a dataframe
    st.write(f"Loaded **{len(df)}** tracks.")
    st.dataframe(df, use_container_width=True, height=450)

    df_grouped = df.groupby("track_genre", as_index=False)["popularity"].mean()

    # bar chart of average track popularity by genre
    fig = px.bar( 
        df_grouped,
        title="Average Track Popularity by Genre",
        x="track_genre",
        y="popularity",
        color="popularity",
        color_continuous_scale=["#ffffff", "#1ED760"],
        height=450,
    )

    fig.update_yaxes(
        range=[0, 100],
        tickformat=".0f"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    # genre select box
    genre = st.selectbox("Genre", sorted(df["track_genre"].unique()))
    filtered = df[df["track_genre"] == genre]

    # display dataframe of the tracks in a particular genre
    st.write(f"**{len(filtered)}** tracks in *{genre}*.")
    st.dataframe(filtered, use_container_width=True, height=366)

    # scatter plot of popularity and danceability for each genre
    fig = px.scatter(
        filtered,
        title=(f"Popularity vs. Valence in {genre}"),
        x="valence",
        y="popularity",
        color="energy",
        color_continuous_scale=["#ffffff", "#1ED760"],
        hover_data=["track_name", "artists"],
        height=470,
    )

    st.plotly_chart(fig, use_container_width=True)