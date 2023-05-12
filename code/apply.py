import streamlit as st
import pandas as pd

# Create navigation menu
menu = ["Submit Form", "View Applications"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Submit Form":
    st.subheader("Submit a New Application")
    # Get user input
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    # Add input to CSV file
    if st.button("Submit"):
        df = pd.read_csv("applications.csv")
        new_row = {"Name": name, "Email": email, "Phone": phone, "Status": "Pending"}
        df = df.append(new_row, ignore_index=True)
        df.to_csv("applications.csv", index=False)
        st.success("Application submitted!")

elif choice == "View Applications":
    st.subheader("View Applications")
    # Read CSV file
    df = pd.read_csv("applications.csv")
    # Display table
    st.dataframe(df)

# Add status updates
if choice == "View Applications":
    st.subheader("View Applications")
    # Read CSV file
    df = pd.read_csv("applications.csv")
    # Display table
    df["Status"] = df["Status"].fillna("Pending")
    for i, row in df.iterrows():
        if st.button(f"Accept {i}"):
            df.at[i, "Status"] = "Accepted"
        elif st.button(f"Reject {i}"):
            df.at[i, "Status"] = "Rejected"
    st.dataframe(df)
    # Update CSV file
    df.to_csv("applications.csv", index=False)

