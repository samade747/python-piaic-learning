import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Streamlit app ka layout aur appearance set karna
st.set_page_config(page_title="Data Sweeper", layout="wide")

# CSS styling se app ko dark mode ka look dena
st.markdown(
    '''
    <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333;
            padding: 1rem;
            color: white;
            border-bottom: 3px solid #0078D7;
        }
        .navbar h1 {
            margin: 0;
            font-size: 1.8rem;
            color: #66c2ff;
        }
        .navbar a {
            color: #66c2ff;
            text-decoration: none;
            margin: 0 1rem;
            font-weight: bold;
        }
        .navbar a:hover {
            color: #005a9e;
        }
        .main {
            background-color: #121212;
        }
        .block-container {
            padding: 3rem 2rem;
            border-radius: 12px;
            background-color: #1e1e1e;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        h1, h2, h3, h4, h5, h6 {
            color: #66c2ff;
        }
        .stButton>button {
            border: none;
            border-radius: 10px;
            background-color: #28a745;
            color: white;
            padding: 0.8rem 1.6rem;
            font-size: 1.1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        }
        .stButton>button:hover {
            background-color: #218838;
            cursor: pointer;
        }
        .stDataFrame, .stTable {
            border-radius: 12px;
            overflow: hidden;
        }
        .css-1aumxhk, .css-18e3th9 {
            text-align: left;
            color: white;
        }
        .stDownloadButton>button {
            background-color: #0078D7;
            color: white;
        }
        .stDownloadButton>button:hover {
            background-color: #005a9e;
        }
    </style>
    '''
    , unsafe_allow_html=True
)

# Navbar se navigation asaan ho jati hai
st.markdown(
    '''
    <div class="navbar">
        <h1>Data Sweeper</h1>
        <div>
            <a href="#upload">Upload File</a>
            <a href="#cleaning">Data Cleaning</a>
            <a href="#visualization">Visualization</a>
            <a href="#conversion">Conversion</a>
        </div>
    </div>
    <p style="color:white; text-align:center;">Build by <a href="https://github.com/samade747" target="_blank" style="color:#66c2ff;">samade747</a> | <a href="https://www.linkedin.com/in/samaddeveloper" target="_blank" style="color:#66c2ff;">samaddeveloper</a></p>
    '''
    , unsafe_allow_html=True
)

st.title("Data Sweeper - File Conversion aur Data Cleaning")
st.write("Apne CSV aur Excel files ko convert karo aur data ko clean bhi kar lo.")

uploaded_files = st.file_uploader("File upload karo (CSV ya Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Yeh file type support nahi hota: {file_extension}")
            continue

        st.write(f"**📄 File ka Naam:** {file.name}")
        st.write(f"**📏 File ka Size:** {file.size / 1024:.2f} KB")
        st.write("🔍 File ka Preview:")
        st.dataframe(df.head())

        st.subheader("🛠️ Data Cleaning Options")
        if st.checkbox(f"Data clean karein {file.name} ke liye"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Duplicate hataayein {file.name} se"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicate rows hata di gayi hain!")
            with col2:
                if st.button(f"Missing values fill karein {file.name} ke liye"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values ko fill kar diya gaya hai!")

        st.subheader("🎯 Select Columns for Conversion")
        columns = st.multiselect(f"Konsa columns choose karna hai {file.name} ke liye", df.columns, default=df.columns)
        df = df[columns]

        st.subheader("📊 Visualization Options")
        if st.checkbox(f"Visualization dikhayein {file.name} ke liye"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert karein {file.name} ko:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert karo {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                mime_type = "text/csv"
                file_name = file.name.replace(file_extension, ".csv")
            else:
                df.to_excel(buffer, index=False, engine='openpyxl')
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                file_name = file.name.replace(file_extension, ".xlsx")

            buffer.seek(0)
            st.download_button("⬇️ Converted File Download karo", buffer, file_name, mime=mime_type)

st.success("🎉 Sab files successfully process ho gayi hain!")
