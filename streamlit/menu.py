import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("main_app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["Admin", "Super Admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Mange admin access",
            disabled=st.session_state.role != "Super Admin",
        )

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("main_app.py", label="Log in")

def menu():
    # Determine if a user is logged in or not, then show the corrext
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue
    # to render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("main_app.py")

    menu()
