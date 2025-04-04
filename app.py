import re
import random
import string
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Blacklist Check (Optional)
    common_passwords = ["password123", "123456", "qwerty", "password"]
    if password.lower() in common_passwords:
        score = 0  # Force weak score
        feedback.append("❌ Avoid common passwords like 'password123'.")
        
    return score, feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("Password Strength Meter")
    
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Check Strength"):
        if password:
            score, feedback = check_password_strength(password)
            
            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below.")
            
            for message in feedback:
                st.write(message)
        else:
            st.warning("Please enter a password.")

    if st.button("Generate Strong Password"):
        generated_password = generate_strong_password()
        st.write("Suggested Strong Password:")
        st.code(generated_password)

if __name__ == "__main__":
    main()