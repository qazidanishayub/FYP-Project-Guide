import streamlit as st
import google.generativeai as genai

# Directly set the API key
API_KEY = "AIzaSyAkctuTgV8j6przeRavSFdOWrdSYn6T3j8"
genai.configure(api_key=API_KEY)

## Gemini Pro Response
def get_gemini_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_text)
    return response.text

## Real Estate Chatbot Prompt
real_estate_prompt = """
You are an advanced real estate chatbot with extensive experience in property evaluation and a deep understanding of the housing market. Your task is to assist users in finding the perfect home based on their preferences and needs.

The user will provide details about their ideal home, such as the desired location, size, amenities, and budget range. Your response should analyze these requirements and provide recommendations tailored to their preferences. Assign a suitability score to each property based on how well it matches their criteria, and highlight any missing features or amenities they might want to consider.

Here is the user's input:

Location: {location}
Size: {size}
Amenities: {amenities}
Budget Range: {budget}

Please generate multiple property options, each with a detailed breakdown of its suitability and features.
"""

## Streamlit app
st.title("Real Estate Chatbot")
st.text("Find Your Dream Home with our AI Chatbot")
location = st.text_input("Desired Location")
size = st.selectbox("Desired Size", ["1 Bedroom", "2 Bedrooms", "3 Bedrooms", "4+ Bedrooms"])
amenities = st.multiselect("Desired Amenities", ["Swimming Pool", "Gym", "Backyard", "Garage", "Balcony"])
budget = st.text_input("Budget Range")
submit = st.button("Submit")

if submit:
    if location.strip() != "" and size.strip() != "" and budget.strip() != "":
        input_text = real_estate_prompt.format(location=location, size=size, amenities=", ".join(amenities), budget=budget)
        response = get_gemini_response(input_text)
        st.subheader("Recommended Properties")
        st.write(response)
    else:
        st.error("Please provide all the required information.")
