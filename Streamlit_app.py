import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

with open('Response.json','r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQ Generator using Langchain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or TXT file")
    mcq_cnt = st.number_input("Enter number of MCQs",min_value=3,max_value=50)
    subject = st.text_input("Enter name of the subject",max_chars=20)
    tone = st.text_input("Enter complexity level of questions",max_chars=20,placeholder="simple")
    button = st.form_submit_button("Generate")

    if button and uploaded_file is not None and mcq_cnt and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text" : text,
                            "number" : mcq_cnt,
                            "subject" : subject,
                            "tone" : tone,
                            "response_json" : json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")
            else:
                print(f"total tokense:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in table data")
                    else:
                        st.write(response)
