import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to extract title and meta description from a webpage
def extract_title_meta(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text if soup.find('title') else 'Title not found'
    meta_description_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description_tag['content'] if meta_description_tag else 'Meta Description not found'
    return title, meta_description

# Main Streamlit app
st.title('SEO Analysis Tool')

# Text input for user to enter URLs
urls_input = st.text_area('Enter URLs (one per line):', height=200)

# Process the URLs and display results
if st.button('Analyze'):
    urls = urls_input.strip().split('\n')
    seo_analysis_results = []
    for url in urls:
        url = url.strip()
        title, meta_description = extract_title_meta(url)
        seo_analysis_results.append({'URL': url, 'Title': title, 'Meta Description': meta_description})

    # Display the SEO analysis results
    for result in seo_analysis_results:
        st.write(result)
