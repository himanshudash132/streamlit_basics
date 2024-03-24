import streamlit as st

def main():
    st.title("My Portfolio Website")
    st.markdown("---")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

    if page == "Home":
        st.header("Welcome to My Portfolio!")
        st.write("This is the home page of my portfolio website.")
    
    elif page == "About":
        st.header("About Me")
        st.write("I am a passionate developer with experience in various technologies.")
    
    elif page == "Projects":
        st.header("Projects")
        st.write("Here are some of the projects I have worked on:")
        # You can list your projects here with descriptions and links
    
    elif page == "Contact":
        st.header("Contact Me")
        st.write("You can reach me via email at example@example.com")
        # You can include a contact form or social media links here

if __name__ == "__main__":
    main()
