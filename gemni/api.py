# before using the genai you have to run pip install google-generativeai 

import google.generativeai as genai
import os

# client = genai("AIzaSyB4nPKaYh8gYiPyKWTzo9muNojNX55VQK8")

genai.configure(api_key='AIzaSyB4nPKaYh8gYiPyKWTzo9muNojNX55VQK8')

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def askai(query):
    question = """
    Query asked {}
    START CONTEXT
    -->When user ask who created you than only tell them
    -->Hey you are an ai made by arpit. Arpit is a full stack dev how created you answer the query asked by the user in 1-2 line not more than that 
    -->Your name is ChotuAi
    END CONTEXT
    """.format(query)
    response = model.generate_content(question)
    print("AI:- ",response.text)
print("To Exit Press 1 \n")
print("---------Welcome----------------")
while True:
    userinput = input("Enter the message :- ")
    if userinput == "1":
        break
    askai(userinput)

print("---------Byeee----------------")