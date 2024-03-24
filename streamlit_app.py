
import os
import json
import traceback
import pandas as pd
import streamlit as st
import pdfplumber
from langchain.callbacks import get_openai_callback
from src.mcq_generator.logger import logging
from src.mcq_generator.MCQGenerator import quiz_sequence
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()


def read_file(uploaded_file):
    """Reads a PDF file and returns its text content."""
    text = ''
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += (page.extract_text() or '')  # Handle None
        return text
    except Exception as e:
        logging.error(f"Failed to read PDF: {e}")  # Log the specific error
        raise Exception("Error reading the PDF file")


def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        # iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append(
                {"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False


with open(r'D:\\languages\\python\\projects\\GenerativeAI_projects\\MCQ_generator_openAI_and_langchain\\Response.json', 'r') as file:
    try:
        RESPONSE_JSON = json.load(file)
    except json.decoder.JSONDecodeError:
        st.error("The JSON file is empty or not in the correct format.")

st.title("MCQ generator using OpenAI and Langchain🦜⛓️")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF to start")
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=5)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity Level Of Questions",
                         max_chars=20, placeholder="Simple")
    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Processing..."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = quiz_sequence({
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    })

                logging.info(f"Total Tokens: {cb.total_tokens}")
                logging.info(f"Prompt Tokens: {cb.prompt_tokens}")
                logging.info(f"Completion Tokens: {cb.completion_tokens}")
                logging.info(f"Total Cost: {cb.total_cost}")

                if isinstance(response, dict):
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        df = pd.DataFrame(table_data)
                        df.index += 1
                        st.table(df)
                        st.text_area(
                            "Review", value=response.get("review", ""))
                    else:
                        st.error("Error in processing quiz data.")
            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")
                st.error(
                    "An error occurred. Please check the logs for more details.")
