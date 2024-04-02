import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import streamlit as st
import traceback
import pandas as pd
from langchain.callbacks import get_openai_callback
from Tools.TutorTools.quiz_utils import get_table_data, RESPONSE_JSON

import sqlite3


from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

llm = ""


template = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to\
create a quiz of {number} multiple choice questions for grade {grade} students in {tone} tone.
Make sure that questions are not repeated and check all the questions to be conforming to the text as well.
Make sure to format your response like the RESPONSE_JSON below and use it as a guide.\
Ensure to make the {number} MCQs.
### RESPONSE_JSON
{response_json}
"""
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "grade", "tone", "response_json"],
    template=template,
)
quiz_chain = LLMChain(
    llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True
)

template = """You are an expert english grammarian and writer. Given a multiple choice quiz for {grade} grade students.\
You need to evaluate complexity of the questions and give a complete analysis of the quiz if the students 
will be able to understand the questions and answer them. Only use at max 50 words for complexity analysis.
If quiz is not at par with the cognitive and analytical abilities of the students,\
update the quiz questions which need to be changed and change the tone such that it perfectly fits the students abilities. 
Quiz MCQs:
{quiz}
Critique from an expert english writer of the above quiz:"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["grade", "quiz"], template=template
)
review_chain = LLMChain(
    llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True
)

generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "grade", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True,
)


def startQuiz():
    st.title("Quiz")

    with st.form("user_inputs"):
        uploaded_file = st.text_input("On what topic should the quiz be conducted", max_chars=100, placeholder="simple")

        mcq_count = st.number_input("No of MCQs", min_value=3, max_value=20)
        grade = "Any"
        tone = "funny"

        button = st.form_submit_button("Create quiz")

    if button and uploaded_file is not None and mcq_count and grade and tone:
        with st.spinner("Loading..."):
            try:

                text = wikipedia.run(uploaded_file)

                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "grade": grade,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON),
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            else:
                if isinstance(response, dict):
                    quiz = response.get("quiz", None)
                    print(quiz)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])


                            #Writes into the database
                            result = st.number_input("How many did you get right??", min_value=1, max_value=10)
                            if result:
                                conn = sqlite3.connect('results.db')
                                conn.execute(f"INSERT INTO results (Topic, score) VALUES ('{uploaded_file}', {result})")
                                conn.commit()
                                conn.close()
                            return uploaded_file
                        else:
                            st.error("Error in table data")
                else:
                    st.write(response)
                    
                



    

    






    

