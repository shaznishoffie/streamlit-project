import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation
menu_with_redirect()

if st.session_state.role not in ["Admin", "Super Admin"]:
    st.warning("You do not have permission to view this page")
    st.stop()

st.title("This page is only for admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
