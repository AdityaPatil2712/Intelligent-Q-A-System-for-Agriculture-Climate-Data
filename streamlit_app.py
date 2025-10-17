import streamlit as st
import requests
import json

st.set_page_config(page_title="Project Samarth", layout="centered")
st.title("Project Samarth — Agriculture & Climate Q&A")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please type a question first.")
    else:
        with st.spinner("Processing..."):
            try:
                resp = requests.get("http://127.0.0.1:8000/ask", params={"question": question}, timeout=120)
                if resp.status_code == 200:
                    data = resp.json()
                    answer = data.get("answer", "No answer returned.")
                    st.success(answer)

                    
                    ag_uid = data.get("agri_resource")
                    cl_uid = data.get("climate_resource")
                    if ag_uid or cl_uid:
                        st.markdown("**Sources used:**")
                        if ag_uid:
                            st.write(f"- Agriculture resource UID: `{ag_uid}`")
                        if cl_uid:
                            st.write(f"- Climate resource UID: `{cl_uid}`")
                else:
                    st.error(f"Backend returned HTTP {resp.status_code}. Check backend logs.")
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Make sure uvicorn is running on port 8000.")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
