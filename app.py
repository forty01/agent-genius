import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="AgentGenius", page_icon="🕵️‍♂️", layout="wide")

# Title and Header
st.title("🕵️‍♂️ AgentGenius")
st.markdown("### Your Personal Annuity Intelligence System")

# Sidebar for API Key (We will use this in Level 2)
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key from Google AI Studio")

# Main Content Area
st.write("---")
st.header("📄 Upload Rate Sheet")

uploaded_file = st.file_uploader("Upload a Carrier Rate Sheet (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")
    
    # Placeholder for the AI logic
    if st.button("Analyze with Gemini AI"):
        if not api_key:
            st.error("⚠️ Please enter your Gemini API Key in the sidebar first.")
        else:
            st.info("🚀 AI Analysis coming in Level 2! Great job getting this far.")
            
            # Mock display to show what it WILL look like
            st.subheader("Preview of Extracted Data:")
            st.json({
                "Carrier": "Allianz (Example)",
                "Product": "Benefit Control",
                "5-Year Rate": "8.50%"
            })

# Footer
st.markdown("---")
st.caption("AgentGenius v0.1 - Built for The Fortier Team")
