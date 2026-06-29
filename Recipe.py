import streamlit as st

# A local "Database" of recipes
# You can expand this list as much as you want!
recipe_db = [
    {
        "name": "Paneer Butter Masala",
        "ingredients": ["paneer", "butter", "tomato", "onion", "cream"],
        "instructions": "1. Sauté onions and tomatoes. 2. Blend into a paste. 3. Add butter and paneer. 4. Cook until soft."
    },
    {
        "name": "Egg Omelette",
        "ingredients": ["egg", "onion", "pepper", "salt"],
        "instructions": "1. Whisk eggs with salt and pepper. 2. Add chopped onions. 3. Fry on a hot pan."
    },
    {
        "name": "Veg Sandwich",
        "ingredients": ["bread", "butter", "potato", "onion"],
        "instructions": "1. Boil and mash potatoes. 2. Apply butter on bread. 3. Stuff potatoes and toast."
    }
]

st.title("🍳 Offline Recipe Finder")
st.write("Enter the ingredients you have, and I'll find a matching recipe.")

# User Input
user_input = st.text_input("Enter ingredients (e.g., egg, onion):")

if user_input:
    # Convert input to a list of ingredients
    user_ingredients = [i.strip().lower() for i in user_input.split(",")]
    
    st.write("---")
    
    found_recipe = False
    for recipe in recipe_db:
        # Check if ALL user ingredients are present in the recipe's ingredient list
        if all(item in recipe["ingredients"] for item in user_ingredients):
            st.success(f"### You can make: {recipe['name']}")
            st.write(f"**Instructions:** {recipe['instructions']}")
            found_recipe = True
            
    if not found_recipe:
        st.warning("No perfect match found. Try fewer ingredients!")
