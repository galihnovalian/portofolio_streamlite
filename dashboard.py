import streamlit as st
import numpy as np
import pandas as pd

# def tampilkan_dashboard():
#     data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
#     st.line_chart(data)

#     st.markdown("### Filter Data")
#     range_slider = st.slider("Pilih range nilai:", 0, 100, (25, 75))
#     st.write(f"Anda memilih range: {range_slider}")

def tampilkan_dashboard():
    st.title("📊 Analitic Dashboard")
    st.markdown("Welcome to Interactive Data Analitic Dashboard !")

    # Data dummy
    np.random.seed(42)
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=100),
        'Sales': np.random.randint(100, 500, size=100),
        'Visitor': np.random.randint(50, 300, size=100),
        'Category': np.random.choice(['A', 'B', 'C'], size=100)
    })

    # Sidebar filter
    st.sidebar.header("Filter Data")
    kategori_terpilih = st.sidebar.multiselect("Choose Category", options=data['Category'].unique(), default=data['Category'].unique())

    data_filtered = data[data['Category'].isin(kategori_terpilih)]

    # Statistik ringkas
    st.subheader("Statistic Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{data_filtered['Sales'].sum():,}")
    col2.metric("Average Sales", f"{data_filtered['Sales'].mean():.2f}")
    col3.metric("Total Visitor", f"{data_filtered['Visitor'].sum():,}")

    # Line chart penjualan
    st.subheader("Daily Sales Trend")
    st.line_chart(data_filtered.set_index('Date')['Sales'])

    # Bar chart pengunjung per kategori
    st.subheader("Customer per Category")
    pengunjung_kat = data_filtered.groupby('Category')['Visitor'].sum()
    st.bar_chart(pengunjung_kat)

    # Tabel data
    st.subheader("Data")
    st.dataframe(data_filtered)
