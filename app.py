import os
import uuid
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="NutriGenie AI",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 NutriGenie AI")
st.subheader("Personalized Nutrition Assistant")
st.write(
    "Get practical, personalized nutrition guidance powered by "
    "IBM Granite, LangFlow and RAG."
)

st.divider()

age = st.number_input("Age", min_value=10, max_value=100, value=22)
activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)
diet = st.selectbox(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)
goal = st.selectbox(
    "Health Goal",
    ["Maintain healthy weight", "Weight loss", "Muscle gain", "Healthy eating"]
)
allergies = st.text_input(
    "Food Allergies",
    placeholder="Example: None, peanuts, dairy"
)
preferences = st.text_input(
    "Food Preferences",
    placeholder="Example: Indian food, high protein"
)

st.divider()

if st.button("✨ Generate My Nutrition Plan", use_container_width=True):

    flow_id = os.getenv("FLOW_ID")
    api_key = os.getenv("LANGFLOW_API_KEY")
    langflow_url = os.getenv(
        "LANGFLOW_URL",
        "http://localhost:7860"
    )

    if not flow_id or not api_key:
        st.error(
            "LangFlow configuration is missing. "
            "Please set FLOW_ID and LANGFLOW_API_KEY."
        )
        st.stop()

    prompt = f"""
Create a personalized one-day nutrition plan for this user.

Age: {age}
Activity level: {activity}
Diet preference: {diet}
Health goal: {goal}
Food allergies: {allergies}
Food preferences: {preferences}

Use the retrieved nutrition knowledge from the NutriGenie
knowledge base.

Include:
1. Breakfast
2. Mid-morning snack
3. Lunch
4. Evening snack
5. Dinner
6. Approximate calories and protein
7. Healthy food swaps
8. Hydration guidance
9. A short explanation of why the foods are suitable

Prefer culturally relevant Indian foods when appropriate.
Do not diagnose or treat medical conditions.
If important medical information is missing, clearly state that
the advice is general and recommend consulting a qualified
healthcare professional for medical concerns.
"""

    url = f"{langflow_url}/api/v1/run/{flow_id}"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    payload = {
        "input_value": prompt,
        "input_type": "chat",
        "output_type": "chat",
        "session_id": str(uuid.uuid4())
    }

    try:
        with st.spinner("NutriGenie is creating your plan..."):

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=90
            )

            response.raise_for_status()
            data = response.json()

        answer = None

        for group in data.get("outputs", []):
            for output in group.get("outputs", []):
                results = output.get("results", {})
                message = results.get("message", {})

                if isinstance(message, dict):
                    answer = message.get("text")

                if answer:
                    break

            if answer:
                break

        if answer:
            st.success("Your personalized nutrition plan is ready!")
            st.markdown(answer)
        else:
            st.error(
                "The flow responded, but the answer format "
                "could not be read."
            )
            st.json(data)

    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to LangFlow: {e}")

    except Exception as e:
        st.error(f"Something went wrong: {e}")