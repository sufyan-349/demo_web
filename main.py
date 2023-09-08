import streamlit as st
import pandas as pd

st.title("Welcome to Sufyan Khan page")
st.header("Paragraph: Python")
st.subheader("Sub Head: Java")
st.markdown("I Love python")                                                 # Text
st.code("""for i in range(1,5,1):
                print('Hello')""")  # Code section like provided by ChatGPT
df = pd.read_csv("data.csv")
st.dataframe(df)                      # Add Datasets (excel, csv)       [Expandable, Editable]

name = st.text_input("Enter your Name: ")
fname = st.text_input("Enter your Father Name: ")
adr = st.text_area("Enter Text: ")
clas = st.selectbox("Enter your class: ",(1,2,3,4,5))

button = st.button("Done")
if button:
    st.markdown((f"""
    Name:        {name}  \n
    Father Name: {fname} \n
    Address:     {adr}   \n
    Class:       {clas}
"""))
    



# To create a Requirements.txt  :command prompt : pip freeze > requirements.txt