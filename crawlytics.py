import streamlit as st
from advertools import sitemap_ping
import xml.etree.ElementTree as ET

def create_sitemap_xml(urls):
    root = ET.Element("urlset")
    root.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

    for url in urls:
        url_elem = ET.SubElement(root, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = url

    tree = ET.ElementTree(root)
    tree.write("sitemap.xml")

    st.success("Sitemap generated successfully!")

st.title('Sitemap Generator')

urls_input = st.text_area('Enter the URLs (separate by line)', height=200)

if st.button('Generate Sitemap'):
    urls_list = urls_input.split('\n')
    create_sitemap_xml(urls_list)
