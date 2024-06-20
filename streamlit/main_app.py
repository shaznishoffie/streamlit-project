import streamlit as st
from menu import menu

# Set title
st.title('Welcome to the Test App')

# Initialise st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialise the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Sessiont State
    st.session_state.role = st.session_state._role

# Selectbox to choose role
st.selectbox(
    "Select your role",
    [None, "User", "Admin", "Super Admin"],
    key="_role",
    on_change=set_role,
)
menu()
