import streamlit as st
import pandas as pd
import sqlite3

st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to", ('Home', 'Add Data', 'View Data'))

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS submissions
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT,
    status TEXT)
''')

def add_submission(name, email, phone, message):
    c.execute('INSERT INTO submissions (name, email, phone, message, status) VALUES (?, ?, ?, ?, ?)', (name, email, phone, message, 'Pending'))
    conn.commit()

def view_submissions():
    c.execute('SELECT * FROM submissions')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Phone', 'Message', 'Status'])
    return df

if page == 'Home':
    st.title('Welcome to the Form App')
    st.write('Use the navigation menu on the left to add or view data.')
    
elif page == 'Add Data':
    st.title('Add Data')
    name = st.text_input('Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone')
    message = st.text_input('Message')
    
    if st.button('Submit'):
        add_submission(name, email, phone, message)
        st.success('Submission added to database.')
        
elif page == 'View Data':
    st.title('View Data')
    df = view_submissions()
    st.dataframe(df)
