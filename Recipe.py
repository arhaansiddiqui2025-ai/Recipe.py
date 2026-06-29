import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="Arhaan's Recipe Chef", page_icon="👨‍🍳")
st.title("👨‍🍳 Arhaan's Recipe Chef")
st.write("Tell me what ingredients you have, and I will generate a recipe for you!")

# 2. API Key Setup
# It is best practice to use Streamlit's secrets for security
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["pip install -U google-genai"]
else:
    api_key = st.sidebar.text_input("pip install -U google-genai", type="password")

# 3. User Input
ingredients = st.text_area("List your ingredients (e.g., tomatoes, garlic, pasta, chicken):")

if st.button("Generate Recipe"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not ingredients:
        st.warning("Please enter some ingredients first.")
    else:
        try:
            # 4. Connecting to Gemini
            client = genai.Client(api_key=api_key)
            
            prompt = f"I have the following ingredients: {ingredients}. Please suggest a delicious recipe I can make. Include ingredients list and step-by-step instructions."
            
            with st.spinner("Chef is cooking..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                # 5. Display Result
                st.markdown("### Your Recipe:")
                st.write(response.text)
        except ValueError:
            st.error("Invalid API Key format. Please check your Gemini API Key.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
