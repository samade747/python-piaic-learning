import streamlit as st
import requests
import geocoder

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/weather/"

st.set_page_config(page_title="🌤️ Weather App", layout="wide")

# Function to get user's location
def get_location():
    g = geocoder.ip('me')
    return g.city if g.city else "Nairobi"

# UI Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://source.unsplash.com/1600x900/?weather');
        background-size: cover;
        color: white;
    }
    .weather-box {
        background: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
    }
    h2, h3, p {
        margin: 10px 0;
    }
    .weather-icon {
        width: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌤️ Real-Time Weather App")
st.write("Get weather details by location or search for any city.")

# Get user's location automatically
default_city = get_location()
city = st.text_input("Enter City Name", default_city)

if st.button("Get Weather"):
    response = requests.get(API_URL + city)
    
    if response.status_code == 200:
        data = response.json()
        
        if "error" in data:
            st.error("City not found. Please try again.")
        else:
            icon_url = f"http://openweathermap.org/img/wn/{data['icon']}@2x.png"
            
            st.markdown(f"""
                <div class='weather-box'>
                    <h2>🌍 {data['city']}</h2>
                    <img src='{icon_url}' class='weather-icon'>
                    <h3>{data['weather'].capitalize()}</h3>
                    <p>🌡️ <b>Temperature:</b> {data['temperature']}°C</p>
                    <p>💧 <b>Humidity:</b> {data['humidity']}%</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Error fetching data. Try again later.")


# import streamlit as st
# import requests
# import geocoder

# # FastAPI backend URL
# API_URL = "http://127.0.0.1:8000/weather/"

# st.set_page_config(page_title="🌤️ Weather App", layout="wide")

# # Function to get user's location
# def get_location():
#     g = geocoder.ip('me')
#     return g.city if g.city else "Nairobi"

# # UI Styling
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://source.unsplash.com/1600x900/?weather');
#         background-size: cover;
#     }
#     .weather-box {
#         background: rgba(255, 255, 255, 0.7);
#         padding: 20px;
#         border-radius: 15px;
#         text-align: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("🌤️ Real-Time Weather App")
# st.write("Get weather details by location or search for any city.")

# # Get user's location automatically
# default_city = get_location()
# city = st.text_input("Enter City Name", default_city)

# if st.button("Get Weather"):
#     response = requests.get(API_URL + city)
    
#     if response.status_code == 200:
#         data = response.json()
        
#         if "error" in data:
#             st.error("City not found. Please try again.")
#         else:
#             st.markdown(f"""
#                 <div class='weather-box'>
#                     <h2>🌍 {data['city']}</h2>
#                     <h3>{data['weather'].capitalize()}</h3>
#                     <p>🌡️ <b>Temperature:</b> {data['temperature']}°C</p>
#                     <p>💧 <b>Humidity:</b> {data['humidity']}%</p>
#                 </div>
#             """, unsafe_allow_html=True)
#     else:
#         st.error("Error fetching data. Try again later.")
