import streamlit as st
import pandas as pd

# Load the data
@st.cache_data # This makes the app load the file only once for speed
def load_data():
    return pd.read_csv("recipes.csv")

st.set_page_config(page_title="Arhaan's Recipe Finder", page_icon="🌍")
st.title("🌍 Arhaan's Recipe Finder")

df = load_data()

user_input = st.text_input("Enter ingredients (comma separated):")

if user_input:
    user_ingredients = [i.strip().lower() for i in user_input.split(",")]
    
    # Logic to calculate matches
    def count_matches(recipe_ingredients):
        recipe_list = [i.strip().lower() for i in recipe_ingredients.split(",")]
        return len([i for i in user_ingredients if i in recipe_list])

    # Calculate scores
    df['score'] = df['ingredients'].apply(count_matches)
    
    # Filter and Sort
    results = df[df['score'] > 0].sort_values(by='score', ascending=False)

    if not results.empty:
        for index, row in results.iterrows():
            with st.expander(f"{row['name']} ({row['score']} match)"):
                st.write(f"**Ingredients:** {row['ingredients']}")
                st.write(f"**Instructions:** {row['instructions']}")
    else:
        st.warning("No recipes found. Try different ingredients!")
