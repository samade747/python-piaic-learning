import random
import string
import streamlit as st
import pymongo
import bcrypt


# MongoDB Connection (Replace with your MongoDB URI)
MONGO_URI = "your_mongodb_connection_string"
db = client["user_db"]  # Database name
users_collection = db["users"]  # Collection name

# Custom CSS for Better UI
st.markdown("""
    <style>
        .big-font { font-size:25px !important; font-weight: bold; text-align: center; }
        .success-message { color: #4CAF50; font-size: 18px; }
        .error-message { color: #FF5252; font-size: 18px; }
        .password-box { border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; font-size: 20px; text-align: center; }
        .weak { color: #FF5252; font-weight: bold; }
        .strong { color: #4CAF50; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Function to generate a random password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak ❌ (Too short)", "weak"
    elif not any(char.isdigit() for char in password):
        return "Weak ❌ (No numbers)", "weak"
    elif not any(char in string.punctuation for char in password):
        return "Weak ❌ (No special characters)", "weak"
    else:
        return "Strong ✅", "strong"
    

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


# Function to verify password
def verify_password(entered_password, stored_hash):
    return bcrypt.checkpw(entered_password.encode(), stored_hash)

# Sidebar Navigation
page = st.sidebar.radio("🔹 Navigation", ["Signup", "Login"])


if page == "Signup":
    st.markdown("<p class='big-font'>📝 Signup</p>", unsafe_allow_html=True)

    ignup_username = st.text_input("👤 Enter Username:")

    # Password Generation & Strength Check
    password_length = st.slider("🔑 Select Password Length:", 8, 32, 12)
    if st.button("🎲 Generate Password"):
        generated_password = generate_password(password_length)
        strength_text, strength_class = check_password_strength(generated_password)
        st.markdown(f"<div class='password-box'>{generated_password}</div>", unsafe_allow_html=True)
        st.markdown(f"<p class='{strength_class}'>{strength_text}</p>", unsafe_allow_html=True)

    signup_password = st.text_input("🔐 Enter Password:", type="password")

    if st.button("✅ Signup"):
        if users_collection.find_one({"username": signup_username}):
            st.markdown("<p class='error-message'>⚠️ Username already exists!</p>", unsafe_allow_html=True)
        else:
            strength_text, strength_class = check_password_strength(signup_password)
            if "Weak" in strength_text:
                st.markdown("<p class='error-message'>❌ Password is weak! Please use a stronger password.</p>", unsafe_allow_html=True)
            else:
                hashed_pw = hash_password(signup_password)
                users_collection.insert_one({"username": signup_username, "password": hashed_pw})
                st.markdown("<p class='success-message'>🎉 Signup successful! You can now login.</p>", unsafe_allow_html=True)

elif page == "Login":
    st.markdown("<p class='big-font'>🔓 Login</p>", unsafe_allow_html=True)


    login_username = st.text_input("👤 Username:")
    login_password = st.text_input("🔐 Password:", type="password")

    if st.button("🔑 Login"):
        user = users_collection.find_one({"username": login_username})
        if user and verify_password(login_password, user["password"]):
            st.markdown("<p class='success-message'>✅ Login successful! Welcome back.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='error-message'>❌ Invalid username or password!</p>", unsafe_allow_html=True)