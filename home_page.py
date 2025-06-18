import streamlit as st

def show_homepage():
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='color: navy;'>🏦 GOLDEN TRUST BANK</h1>
            <p style='font-size: 18px;'>Secure, simple, and smart banking for you.</p>
        </div>
    """, unsafe_allow_html=True)



    st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 16px;'>
        <p>Use the sidebar to:</p>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li>✅ Create a new account (Savings or Current)</li>
            <li>💰 Deposit or withdraw funds</li>
            <li>📊 View your current balance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
