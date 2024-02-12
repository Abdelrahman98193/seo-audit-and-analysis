import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.title("SEO Analysis of URLs in CSV")

def analyze_csv(file):
    df = pd.read_csv(file)
    
    if 'url' not in df.columns:
        st.error("CSV file must contain a column named 'url'")
        return
    
    st.success("CSV file loaded successfully!")
    
    # SEO Analysis for each URL in the CSV
    for url in df['url']:
        st.markdown(f"## SEO Analysis for URL: {url}")
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Perform SEO analysis here using BeautifulSoup
                # You can extract meta tags, title, headings, links, etc.
                
                st.write("SEO analysis results:")
                # Display SEO analysis results for the URL
                
            else:
                st.error(f"Failed to fetch URL: {url}. Status Code: {response.status_code}")
        except requests.RequestException as e:
            st.error(f"An error occurred while fetching URL: {url}. Error: {e}")
            
st.write("Upload a CSV file containing a column 'url' for SEO analysis:")
file = st.file_uploader("Upload CSV", type=['csv'])

if file is not None:
    analyze_csv(file)
