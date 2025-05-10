import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("movie.xlsx")

df.columns = df.columns.str.strip()

# Drop rows with missing Genre
df = df.dropna(subset=['Genre'])


df['Genre'] = df['Genre'].str.strip().str.title()

# Get all unique genres 
all_genres = sorted(df['Genre'].unique().tolist())

st.title("🎬 Screenly")
st.subheader("🎭 Choose Your Mood")

selected_genres = []

# Display checkboxes 
for i in range(0, len(all_genres), 6):
    cols = st.columns(6)
    for j in range(6):
        if i + j < len(all_genres):
            with cols[j]:
                genre_label = all_genres[i + j]
                if st.checkbox(genre_label, key=genre_label):
                    selected_genres.append(genre_label)

st.markdown("---")
# st.write(" Selected Genres:", selected_genres)

# Filter and display matching movies
if selected_genres:
    filtered_movies = df[df['Genre'].isin(selected_genres)]

    st.write("🍿 Recommended Movies:")
    for i in range(0, len(filtered_movies), 6):
        cols = st.columns(6)
        for j in range(6):
            if i + j < len(filtered_movies):
                movie = filtered_movies.iloc[i + j]
                with cols[j]:
                    st.image(movie['Poster'], width=180)
                    st.caption(f"🎬{movie['Title']}")
