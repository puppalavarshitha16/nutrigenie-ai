# 🥗 NutriGenie AI

## AI-Powered Personalized Nutrition Assistant

NutriGenie AI is an AI-powered nutrition assistant built using IBM Granite, LangFlow, and Retrieval-Augmented Generation (RAG).

The application generates personalized Indian nutrition guidance based on a user's age, activity level, dietary preference, health goal, allergies, and food preferences.

## Problem Statement

Nutrition tools often provide generic recommendations and may not adapt to individual dietary preferences, lifestyle, and changing requirements.

NutriGenie addresses this challenge by combining an LLM with a nutrition knowledge base through RAG.

## Key Features

- Personalized one-day nutrition plans
- Indian food recommendations
- Vegetarian and non-vegetarian dietary preferences
- Approximate calorie and protein information
- Healthy food substitutions
- Hydration guidance
- Lifestyle recommendations
- Nutrition knowledge retrieval using RAG
- IBM Granite foundation model
- LangFlow-based workflow
- Streamlit user interface

## Technology Used

- IBM watsonx.ai
- IBM Granite `ibm/granite-4-h-small`
- LangFlow
- Retrieval-Augmented Generation (RAG)
- Chroma Local Knowledge Base
- Streamlit
- Python
- GitHub

## System Workflow

User Input  
↓  
Streamlit Interface  
↓  
LangFlow  
↓  
Nutrition Knowledge Base  
↓  
RAG Retrieval  
↓  
Prompt Template  
↓  
IBM Granite  
↓  
Personalized Nutrition Response

## Project Structure

```text
nutrigenie-ai/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── nutrition_data.csv
├── screenshots/
└── README.md