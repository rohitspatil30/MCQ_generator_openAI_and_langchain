import os
import pandas as pd
import traceback
import json
from src.mcq_generator.utils import read_file, get_table_data
from dotenv import load_dotenv
from src.mcq_generator.logger import logging
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()
KEY = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(openai_api_key=KEY, temperature=0.3, model='gpt-3.5-turbo')

TEMPLATE = '''
        Text: {text}
        You are an expert MCQ maker. Given the above text, it is your job to \
        create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
        Make sure the questions are not repeated and check all the questions to be conforming the text as well.
        Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
        Ensure to make {number} MCQs
        ### RESPONSE_JSON
        {response_json}

        '''
quiz_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt,
                      output_key="quiz", verbose=True)

TEMPLATE2="""
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students. \
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity
if the quiz is not at par with the cognitive and analytical abilities of the students, \
update the quiz questions which need to be changed and change the tone such that it perfectly fits the student's ability
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)

quiz_evaluation_chain = LLMChain(llm = llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

quiz_sequence = SequentialChain(chains=[quiz_chain,quiz_evaluation_chain], input_variables = ["text", "number", "subject", "tone", "response_json"],
                               output_variables=["quiz","review"], verbose=True)

