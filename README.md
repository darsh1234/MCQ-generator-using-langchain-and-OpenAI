# MCQ Generator

MCQ Generator is a web application that utilizes LangChain and the OpenAI API to generate multiple-choice questions (MCQs) based on a provided text or PDF file. Users can specify the subject, difficulty level, and quantity of MCQs to be generated.

## Technologies Used

- LangChain
- OpenAI API (Model used - ChatGPT 3.5 Turbo)
- Streamlit
- AWS (EC2, ELB)

## Installation

1. Clone the repository:

```git clone https://github.com/darsh1234/MCQ-generator-using-langchain-and-OpenAI.git```

```cd MCQ-generator-using-langchain-and-OpenAI```

2. Create a virual environment (Recommended):

```conda create --name mcq_env python=3.10```

```conda activate mcq_env```


3. Dependencies
Ensure you have all the dependecies installed as given in requirements.txt

```pip install -r requirements.txt```

4.create a .env file in the root directory

```touch .env```

5. add your OpenAI API Key to the .env file

```OPENAI_API_KEY = ""```

6. Run the webapp

```streamlit run Stremalit_app.py```


## Deployment 
The application has been deployed to AWS and streamlit.io
You can find instructions on deploying the project to an AWS EC2 Instance (t2.medium or t2.large is recommended) running Ubuntu  in EC2_Ubuntu_commands.txt