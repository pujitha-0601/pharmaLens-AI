import streamlit as st
from groq import Groq

st.set_page_config(page_title="PharmaLens", page_icon="💊", layout="wide")

# Sidebar API Key
st.sidebar.title("🔑 Settings")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password", placeholder="gsk_...")
st.sidebar.caption("Get FREE from console.groq.com/keys")

if not api_key:
    st.warning("👈 Enter API key in sidebar")
    st.stop()

client = Groq(api_key=api_key)
st.title("💊 PharmaLens")

medicine = st.text_input("💊 Enter Medicine Name", "dolo650")

if st.button("Analyze ⚡", type="primary", use_container_width=True):
    with st.spinner("Analyzing..."):
        prompt = f"For {medicine} EDUCATIONAL: 1.Composition 2.Uses 3.Dosage 4.Combinations 5.What to avoid 6.Side effects 7.Precautions. Simple English + consult doctor note."
        res = client.chat.completions.create(model="openai/gpt-oss-20b", messages=[{"role":"user","content":prompt}])
        st.success(f"Report: {medicine.upper()}")
        st.markdown(res.choices[0].message.content)