import streamlit as st
import requests

st.set_page_config(page_title="Country Information Finder", page_icon="🌎", layout="wide")

# Apply background color
st.markdown("""
    <style>
        body {background-color: #1c1c1c; color: white;}
        .main {background-color: #1c1c1c; color: white;}
        h1 {color: #2E86C1; text-align: center;}
        .nav-bar {background-color: #2E86C1; padding: 10px;}
        .nav-bar a {color: white; margin: 0 15px; text-decoration: none; font-weight: bold;}
        .nav-bar a:hover {color: #FFD700;}
        .footer {text-align: center; margin-top: 20px; color: #888;}
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class='nav-bar'>
        <a href='#'>Home</a>
        <a href='#'>About</a>
        <a href='#'>Contact</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1>🌎 Country Information Finder</h1>", unsafe_allow_html=True)

country = st.text_input("Enter a country name:")

if st.button("Search"):
    if country:
        try:
            response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
            if response.status_code == 200:
                data = response.json()[0]

                st.subheader(f"Information about {data['name']['common']}")
                st.markdown(f"**Capital:** {data['capital'][0]}")
                st.markdown(f"**Population:** {data['population']}")
                st.markdown(f"**Area:** {data['area']} sq. km")
                st.markdown(f"**Region:** {data['region']}")
                st.markdown(f"**Subregion:** {data['subregion']}")
                st.markdown(f"**Currency:** {', '.join([curr['name'] for curr in data['currencies'].values()])}")
                st.markdown(f"**Languages:** {', '.join(data['languages'].values())}")
                st.markdown(f"**Timezones:** {', '.join(data['timezones'])}")

            else:
                st.error("Country not found. Please check the spelling or try a different country.")
        except Exception as e:
            st.error("An error occurred while fetching data. Please try again later.")
    else:
        st.warning("Please enter a country name to search.")

# Footer
st.markdown("""
    <div class='footer'>
        Built by <a href='https://github.com/samade747' target='_blank'>samade747@GitHub</a> & <a href='https://twitter.com/samaddeveloper' target='_blank'>samaddeveloper@X</a>
    </div>
""", unsafe_allow_html=True)


# import streamlit as st
# import requests

# st.set_page_config(page_title="Country Information Finder", page_icon="🌎", layout="wide")

# # Apply background color
# st.markdown("""
#     <style>
#         body {background-color: #1c1c1c; color: white;}
#         .main {background-color: #1c1c1c; color: white;}
#         h1 {color: #2E86C1; text-align: center;}
#         .nav-bar {background-color: #2E86C1; padding: 10px;}
#         .nav-bar a {color: white; margin: 0 15px; text-decoration: none; font-weight: bold;}
#         .nav-bar a:hover {color: #FFD700;}
#     </style>
# """, unsafe_allow_html=True)

# # Navigation Bar
# st.markdown("""
#     <div class='nav-bar'>
#         <a href='#'>Home</a>
#         <a href='#'>About</a>
#         <a href='#'>Contact</a>
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("<h1>🌎 Country Information Finder</h1>", unsafe_allow_html=True)

# country = st.text_input("Enter a country name:")

# if st.button("Search"):
#     if country:
#         try:
#             response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
#             if response.status_code == 200:
#                 data = response.json()[0]

#                 st.subheader(f"Information about {data['name']['common']}")
#                 st.markdown(f"**Capital:** {data['capital'][0]}")
#                 st.markdown(f"**Population:** {data['population']}")
#                 st.markdown(f"**Area:** {data['area']} sq. km")
#                 st.markdown(f"**Region:** {data['region']}")
#                 st.markdown(f"**Subregion:** {data['subregion']}")
#                 st.markdown(f"**Currency:** {', '.join([curr['name'] for curr in data['currencies'].values()])}")
#                 st.markdown(f"**Languages:** {', '.join(data['languages'].values())}")
#                 st.markdown(f"**Timezones:** {', '.join(data['timezones'])}")

#             else:
#                 st.error("Country not found. Please check the spelling or try a different country.")
#         except Exception as e:
#             st.error("An error occurred while fetching data. Please try again later.")
#     else:
#         st.warning("Please enter a country name to search.")
