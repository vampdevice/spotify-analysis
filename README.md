# _Spotify Audio Feature Analysis_

- **Author**: Sebastian Zeidler
- **Course**: CS4379G
- **Instructor**: Dr. Aniruddha Bora

# Project Proposal

Do most popular songs share certain audio features? Are songs with
certain audio features more likely to be popular? Are there sub genres/hidden genres based
on overlapping features that aren’t currently recognized by Spotify? I would like to explore
the most popular genres of songs and their features and try to discover any un-labeled
groups of features that make up new genres. (Explore audio features (tempo, energy,
valence, danceability) across genres and decades. Cluster songs using k-means or
DBSCAN on audio features and visualize clusters in PCA/t-SNE reduced space.)

# Dataset

The dataset can be found on Kaggle at https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset. The dataset contains information on over 14,000 songs and over 100 genres. The data contains each song's track ID, artist name, album name, song title, and audio features collected by Spotify such as Energy, Tempo, Loudness, and Danceability.

# Dependencies and Libraries

- pandas
- numpy
- matplotlib
- seaborn
- sklearn

# How to Run

Follow these steps to run the code:

- Clone this repository
- Download the dataset provided above as a .zip file
  - Extract All
  - Insert "dataset.csv" into "data" folder.
- Install the required dependencies
- Open "spotify_analysis.ipynb"
- Select "Run All"
