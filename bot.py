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

# Custom CSS for background image and animations
st.markdown(
    """
    <style>
    body {
        background-size: cover;
        background-attachment: fixed;
    }
    .title {
        animation: fadeInDown 2s;
    }
    .text, .subheader, .write {
        animation: fadeInUp 2s;
    }
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    /* Marquee styles */
    .marquee {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        animation: marquee 15s linear infinite;
    }
    .marquee img {
        width: 150px; /* Adjust the size of the images */
        margin-right: 10px; /* Space between images */
    }
    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for marquee - Replace `your-github-username` and `your-repo` with your actual GitHub username and repository name
st.markdown(
    """
    <div class="marquee">
        <img src="https://www.adanirealty.com/-/media/Project/Realty/Blogs/Types-Of-Residential-Properties.png" alt="Image 1">
      
    </div>
    """,
    unsafe_allow_html=True
)

# Apply CSS classes to Streamlit elements
st.markdown('<div class="title">Real Estate Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Find Your Dream Home with our AI Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Desired Location</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Desired Size</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Desired Amenities</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Budget Range</div>', unsafe_allow_html=True)
st.markdown('<div class="text">Submit</div>', unsafe_allow_html=True)

if submit:
    if location.strip() != "" and size.strip() != "" and budget.strip() != "":
        input_text = real_estate_prompt.format(location=location, size=size, amenities=", ".join(amenities), budget=budget)
        response = get_gemini_response(input_text)
        st.markdown('<div class="subheader">Recommended Properties</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="write">{response}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="text">Please provide all the required information.</div>', unsafe_allow_html=True)
