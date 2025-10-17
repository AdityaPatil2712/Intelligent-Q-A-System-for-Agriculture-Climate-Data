# Project Samarth — Intelligent Q&A System for Agriculture & Climate Data

> **Empowering Data-Driven Governance for India's Agriculture Sector**  
> A full-stack AI system that answers complex natural-language questions about India’s agriculture and climate patterns using **live data from [data.gov.in](https://data.gov.in)**.

---

## Overview

**Project Samarth** is an intelligent **Q&A assistant** designed to make Indian government data *human-understandable*.  
It integrates **real-time datasets from data.gov.in**, analyzes them with **OpenAI’s GPT models**, and delivers meaningful, actionable insights about:

- Crop production, yield, and seasonal patterns  
- Rainfall, temperature, and climate impact  
- Agricultural economy and sustainability insights  

Built using a modern AI + data engineering stack — **FastAPI**, **Streamlit**, **Pandas**, and **OpenAI GPT**, the system enables policymakers, researchers, and citizens to query government datasets effortlessly.

---

## Features

✅ **Natural Language Q&A Interface** — Ask questions like a human, get factual data-backed answers  
✅ **Live Government Data** — Sources data directly from the official [data.gov.in APIs](https://data.gov.in/)  
✅ **Dual-Dataset Integration** — Combines both **Agriculture** and **Climate** datasets intelligently  
✅ **AI-Powered Analysis** — Uses GPT to interpret and summarize multi-dimensional government data  
✅ **Interactive Streamlit Dashboard** — Elegant front-end for seamless interaction  
✅ **FastAPI Backend** — High-performance backend connecting AI and live APIs  
✅ **Error Handling & Fallback** — Gracefully manages unavailable datasets or key issues  

---

---

## 🔑 Datasets Used

| Domain | Dataset Name | Source | Resource ID |
|---------|---------------|--------|--------------|
| 🌾 Agriculture | District-wise Crop Production (2022–23) | [data.gov.in](https://data.gov.in) | `9ef84268-d588-465a-a308-a864a43d0070` |
| ☁️ Climate | Monthly Rainfall Data of India | [data.gov.in](https://data.gov.in) | `4a69f6f6-6f81-4c07-a063-9f69e26ac5a1` |

---

## ⚙️ Tech Stack

| Layer | Technologies Used |
|--------|--------------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **AI / NLP** | OpenAI GPT-4o-mini |
| **Data Source** | data.gov.in APIs |
| **Data Processing** | Python, Pandas |
| **Environment Management** | dotenv |
| **Deployment Ready For** | Streamlit Cloud / Render / AWS EC2 |

---

## 🧩 Folder Structure

project-samarth/
│
├── backend/
│ ├── app.py # FastAPI server
│ ├── qa_engine.py # AI reasoning engine
│ ├── data_fetcher.py # Fetches live datasets
│ ├── .env # API keys (not public)
│
├── frontend/
│ └── streamlit_app.py # Streamlit web interface
│
├── README.md
└── requirements.txt


---

## 🔐 Setup Instructions

### Clone the repository
```bash
git clone https://github.com/<your-username>/project-samarth.git
cd project-samarth

### Create a Virtual Environment:
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows

### Install Requirements:
pip install -r requirements.txt

### Create .env file:
DATA_GOV_API_KEY="Generate API key form Data.gov.in"
OPENAI_API_KEY="Write your Openai API key"

### Run the Backend:
uvicorn app:app --reload

### Run the frontend:
streamlit run streamlit_app.py

### Future Enhancements ###

1)Add visual dashboards for rainfall and crop yield trends

2)Integrate geospatial (GIS) visualization

3)Enable multi-language Q&A for regional accessibility

4)Build predictive insights using ML models

#Author

Aditya Pravin Patil
Final Year B.Tech (Electronics & Computer Engineering)
MIT ADT University, Pune

Maharashtra, India
LinkedIn: https://github.com/AdityaPatil2712
GitHub: https://www.linkedin.com/in/aditya-patil-6596b02b7/
Email: adityapatil27122003@gmail.com

