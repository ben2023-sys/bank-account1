import streamlit as st
from home_page import show_homepage
from accounts.savings_account import SavingsAccount
from accounts.current_account import CurrentAccount

st.set_page_config(page_title="Bank App", layout="centered")

show_homepage()

st.sidebar.header("Create Account")
account_type = st.sidebar.selectbox("Select Account Type", ["Savings", "Current"])
name = st.sidebar.text_input("Your Name")
initial_balance = st.sidebar.number_input("Initial Balance", min_value=0, step=100)

if st.sidebar.button("Create Account"):
    if not name:
        st.warning("Please enter your name.")
    else:
        if account_type == "Savings":
            account = SavingsAccount(name, initial_balance)
        else:
            account = CurrentAccount(name, initial_balance)

        st.session_state['account'] = account
        st.success(f"{account_type} account created for {name}")

if 'account' in st.session_state:
    account = st.session_state['account']
    st.subheader(f"Hello, {account.owner} 👋")

    action = st.radio("Choose Action", ["Check Balance", "Deposit", "Withdraw"])

    if action == "Check Balance":
        st.info(f"Your Balance: ₦{account.get_balance()}")

    elif action == "Deposit":
        amount = st.number_input("Amount to Deposit", min_value=0, step=100)
        if st.button("Deposit"):
            st.success(account.deposit(amount))

    elif action == "Withdraw":
        amount = st.number_input("Amount to Withdraw", min_value=0, step=100)
        if st.button("Withdraw"):
            result = account.withdraw(amount)
            if "Withdrew" in result:
                st.success(result)
            else:
                st.error(result)
