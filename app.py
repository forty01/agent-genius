import streamlit as st
import google.generativeai as genai
import os
import tempfile

# --- CONFIGURATION ---
st.set_page_config(page_title="AgentGenius", page_icon="🕵️‍♂️", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.caption("Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)")
    
    st.divider()
    st.markdown("### 🧠 Model Config")
    model_name = st.selectbox("Select Model", ["gemini-1.5-flash", "gemini-1.5-pro"])
    st.caption("Flash is faster/cheaper. Pro is smarter.")

# --- MAIN APP ---
st.title("🕵️‍♂️ AgentGenius: Rate Sheet Reader")
st.markdown("Upload a carrier rate sheet (PDF) to extract annuity rates automatically.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' ready for analysis.")
    
    if st.button("🚀 Extract Rates"):
        if not api_key:
            st.error("⚠️ Please enter your Gemini API Key in the sidebar.")
        else:
            try:
                with st.spinner("🤖 Gemini is reading the PDF... (This may take 10-20 seconds)"):
                    
                    # 1. Configure Gemini
                    genai.configure(api_key=api_key)
                    
                    # 2. Save uploaded file to a temporary file (Gemini needs a file path)
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name

                    # 3. Upload file to Gemini
                    sample_file = genai.upload_file(path=tmp_file_path, display_name="Rate Sheet")
                    
                    # 4. Define the Prompt
                    prompt = """
                    You are an expert Annuity Analyst. Analyze this rate sheet PDF.
                    Extract the following information into a JSON format:
                    1. Carrier Name
                    2. Product Name
                    3. A list of 'Rates' containing: Term (e.g. 5-Year), Account Type (e.g. S&P 500), Cap Rate, and Participation Rate.
                    
                    If a value is missing, use "N/A".
                    Return ONLY the JSON. Do not include markdown formatting like ```json.
                    """
                    
                    # 5. Generate Content
                    model = genai.GenerativeModel(model_name=model_name)
                    response = model.generate_content([sample_file, prompt])
                    
                    # 6. Display Results
                    st.subheader("✅ Extracted Data")
                    st.json(response.text)
                    
                    # Cleanup
                    os.remove(tmp_file_path)

            except Exception as e:
                st.error(f"An error occurred: {e}")                "Product": "Benefit Control",
                "5-Year Rate": "8.50%"
            })

# Footer
st.markdown("---")
st.caption("AgentGenius v0.1 - Built for The Fortier Team")
