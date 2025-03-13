import re
import streamlit as st

# Set up the Streamlit page
st.title("Password Strength Checker")
st.write("##### This is a simple password strength checker that checks the strength of your password and gives you suggestions on how to improve it.")

# Function to check password strength (unchanged)
def check_password_strength(password):
    score = 0
    message = ""

    if len(password) > 8:
        score += 1
    else:
        message += "Password should be at least 8 characters long.<br>"

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        message += "Password should contain at least one uppercase and one lowercase letter.<br>"

    if re.search(r"[0-9]", password):
        score += 1
    else:
        message += "Password should contain at least one number (0-9).<br>"

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        message += "Password should contain at least one special character (!@#$%^&*()_+).<br>"

    if score == 4:
        return "✅ Password is strong.", 100
    elif score == 3:
        return "⚠️ Password is moderate, consider adding more security. <br>" + message, 75
    elif score == 2:
        return "⚠️ Password is fine but you should improve it by given suggestions below <br>" + message, 50
    else:
        return "❌ Password is weak. Improve it by given suggestions below <br>" + message, 25

# Get the password input from the user
password = st.text_input("Enter your password:")

if st.button("Check Password"):
    if password:
        password_strength, progress = check_password_strength(password)
        st.markdown(password_strength, unsafe_allow_html=True)

        # Set the color of the progress bar based on the password strength
        color_map = {
            25: "#ff0000",  # Red
            50: "#ff6600",  # Orange
            75: "#ffcc00",  # Yellow
            100: "#00ff00"  # Green
        }
        selected_color = color_map.get(progress, "#ff0000")

        st.markdown(f"""
        <style>
            div[data-testid="stProgress"] > div > div > div > div {{
                background-color: {selected_color} !important;
                background-image: none !important;
            }}
        </style>
        """, unsafe_allow_html=True)

        st.progress(progress)

    else:
        st.write("Please enter a password to check its strength.")