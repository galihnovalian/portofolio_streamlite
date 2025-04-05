import streamlit as st

def munculkan_kontak():
    st.title("Contact")
    st.write("If you want to collaborate with me you can reach me at:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/galihnovalian)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/galihnovalian)"
    )
    
    # Email
    st.write("📧 Email: galihnovalian.gn@gmail.com")