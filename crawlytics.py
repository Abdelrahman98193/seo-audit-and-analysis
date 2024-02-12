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
    
    # Create a list to store SEO analysis results
    seo_results = []
    
    # SEO Analysis for each URL in the CSV
    for url in df['url']:
        st.markdown(f"## SEO Analysis for URL: {url}")
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Perform SEO analysis here using BeautifulSoup
                # You can extract meta tags, title, headings, links, etc.
                
                # Sample SEO analysis result for demonstration
                seo_data = {
                    'URL': url,
                    'Title': 'Sample Title',
                    'Meta Description': 'Sample Meta Description',
                    'Headings': 'Sample Headings',
                    'Links': 'Sample Links'
                }
                
                # Add the SEO analysis results to the list
                seo_results.append(seo_data)
                
                # Display SEO analysis results in table format
                st.table(pd.DataFrame([seo_data]))
                
            else:
                st.error(f"Failed to fetch URL: {url}. Status Code: {response.status_code}")
        except requests.RequestException as e:
            st.error(f"An error occurred while fetching URL: {url}. Error: {e}")
    
    # Display all SEO analysis results in a table at the end
    if seo_results:
        st.write("## All SEO Analysis Results")
        st.table(pd.DataFrame(seo_results))

st.write("Upload a CSV file containing a column 'url' for SEO analysis:")
file = st.file_uploader("Upload CSV", type=['csv'])

if file is not None:
    analyze_csv(file)
