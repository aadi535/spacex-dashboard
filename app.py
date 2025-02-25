import streamlit as st
import pandas as pd
import os

# Set Streamlit page configuration
st.set_page_config(page_title="🚀 SpaceX Launch Dashboard", layout="wide")

# Load data function
@st.cache_data
def load_data():
    file_path = "D:/NASA_Meteorite_Dashboard/spacex_launch_data_fixed.csv"  # Update this path if needed
    if not os.path.exists(file_path):  # Check if file exists
        st.error(f"🚨 Error: Dataset file not found at: {file_path}")
        return pd.DataFrame()  # Return empty DataFrame
    df = pd.read_csv(file_path)

    # Rename column if needed (ensure "class" exists in your dataset)
    if "class" in df.columns:
        df.rename(columns={"class": "Success"}, inplace=True)
    
    return df

# Load dataset
df = load_data()

# Check if data is loaded successfully
if df.empty:
    st.warning("⚠ No data loaded. Please check the dataset file.")
else:
    # Display title and description
    st.title("🚀 SpaceX Launch Dashboard")
    st.write("Explore SpaceX launches with interactive data visualizations.")

    # Show dataset preview
    st.subheader("📊 Dataset Preview")
    st.dataframe(df)  # Display full dataset initially

    # Show available columns for debugging
    st.write("🔍 **Columns in dataset:**", df.columns.tolist())

    # Sidebar filter for success/failure
    st.sidebar.header("🎯 Filter Launch Results")
    launch_status = st.sidebar.radio("Select Launch Outcome:", ("All", "Success", "Failure"))

    # Apply filter based on selection
    if launch_status == "Success":
        df = df[df["Success"] == 1]
    elif launch_status == "Failure":
        df = df[df["Success"] == 0]

    # Display filtered data
    st.subheader("🚀 Filtered Launch Data")
    st.dataframe(df)

    # Display success/failure counts
    st.sidebar.subheader("📊 Success vs Failure Count")
    success_count = df["Success"].sum()
    failure_count = len(df) - success_count
    st.sidebar.write(f"✅ Success: {success_count}")
    st.sidebar.write(f"❌ Failure: {failure_count}")
