from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from data_fetcher import get_agriculture_data, get_climate_data

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY)

def process_question(question: str):
    try:
        agri = get_agriculture_data(limit=50)
        climate = get_climate_data(limit=50)

        if not agri["records"] or not climate["records"]:
            return {"answer": "No data fetched. Check your API keys or dataset availability.", "ok": False}

       
        agri_sample = pd.DataFrame(agri["records"]).head(5).to_dict(orient="records")
        climate_sample = pd.DataFrame(climate["records"]).head(5).to_dict(orient="records")

        prompt = f"""
You are an expert government data analyst. You have two datasets from data.gov.in:

1. Agriculture dataset (UID: {agri['resource_uid']}), sample: {agri_sample}
2. Climate dataset (UID: {climate['resource_uid']}), sample: {climate_sample}

Answer the following question concisely in 3-5 sentences. Cite data sources like (Source: data.gov.in/{agri['resource_uid']}) or (Source: data.gov.in/{climate['resource_uid']}).

Question: {question}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise analyst who cites dataset UIDs for all data points."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )

        answer = response.choices[0].message.content.strip()
        return {
            "answer": answer,
            "ok": True,
            "agri_resource": agri["resource_uid"],
            "climate_resource": climate["resource_uid"]
        }

    except Exception as e:
        return {"answer": f"Backend error: {str(e)}", "ok": False}
