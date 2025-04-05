import streamlit as st

st.set_page_config(layout='wide')
st.title('My Portfolio')
st.header('Data Scientist Enthusiast')

st.sidebar.title('Navigasi Halaman')

page = st.sidebar.radio('Pilih halaman', 
                        ['About Me', 
                        'Dashboard', 'Prediction', 
                        'Contact'])

if page == 'About Me':
    import about
    about.about_me()
elif page == 'Contact':
    import kontak
    kontak.munculkan_kontak()
elif page == 'Dashboard':
    import dashboard
    dashboard.tampilkan_dashboard()
elif page == 'Prediction':
    import prediksi
    prediksi.lakukan_prediksi()     