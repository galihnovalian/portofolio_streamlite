import streamlit as st

st.set_page_config(layout='wide')
st.title('My Portofolio')
st.header('Data Scientist Enthusiast')

st.sidebar.title('Navigasi Halaman')

page = st.sidebar.radio('Pilih halaman', 
                        ['Tentang saya', 
                        'Dashboard', 'Prediction', 
                        'Kontak'])

if page == 'Tentang saya':
    import about
    about.about_me()
elif page == 'Kontak':
    import kontak
    kontak.munculkan_kontak()
elif page == 'Dashboard':
    import dashboard
    dashboard.tampilkan_dashboard()
elif page == 'Prediction':
    import prediksi
    prediksi.lakukan_prediksi()     