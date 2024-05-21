import json
import requests  
import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie  
import google.generativeai as genai

# Directly set the API key
API_KEY = "AIzaSyAkctuTgV8j6przeRavSFdOWrdSYn6T3j8"
genai.configure(api_key=API_KEY)

## Gemini Pro Response
def get_gemini_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_text)
    return response.text
 

# Function to get the base64 of the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your image and encode it in base64
img_base64 = get_base64_of_bin_file('static/back.jpg')

# Load custom CSS
background_image_css = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""

st.markdown(background_image_css, unsafe_allow_html=True)

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

# Load custom CSS
with open('style.css') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://lottie.host/0f0192c8-b733-4ca2-995d-8fb543834b0c/ltHN2qxTH8.json"
lottie_animation = load_lottieurl(lottie_url)

# Display Lottie animation in the top right corner
if lottie_animation:
    st.markdown(
        """
        <div style="position: absolute; top: 50%; left:100%; transform: translate(-50%, -50%); width: 50px; height: 50px;">
            <div id="lottie-animation"></div>
        </div>
        """, unsafe_allow_html=True
    )
    st_lottie(
        lottie_animation,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium",  # Adjust quality as needed: "low", "medium", "high"
        height=150,        # Adjust height as needed
        width=150,         # Adjust width as needed
        key='lottie_animation'
    )

st.markdown("<div class='marquee-container'><p class='marquee'>Find Your Dream Home with our AI Chatbot</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='custom-header'>Please provide the details of your ideal home below:</h2>", unsafe_allow_html=True)

with st.form(key='real_estate_form'):
    location = st.text_input("Desired Location")
    size = st.selectbox("Desired Size", ["1 Bedroom", "2 Bedrooms", "3 Bedrooms", "4+ Bedrooms"])
    amenities = st.multiselect("Desired Amenities", ["Swimming Pool", "Gym", "Backyard", "Garage", "Balcony"])
    budget = st.text_input("Budget Range")
    submit = st.form_submit_button("Submit")

# JavaScript to apply effect when amenity is selected
js_code = """
<script>
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                this.parentElement.classList.add('amenity-selected');
            } else {
                this.parentElement.classList.remove('amenity-selected');
            }
        });
    });
</script>
"""

st.markdown(js_code, unsafe_allow_html=True)

if submit:
    if location.strip() != "" and size.strip() != "" and budget.strip() != "":
        input_text = real_estate_prompt.format(location=location, size=size, amenities=", ".join(amenities), budget=budget)
        response = get_gemini_response(input_text)
        st.markdown("<div class='response-section'><p class='response-text'>Recommended Properties:</p><p class='response-text'>{}</p></div>".format(response), unsafe_allow_html=True)
    else:
        st.error("Please provide all the required information.")