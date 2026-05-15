import streamlit as st
import pickle as pkl

with open("model.pkl","rb") as f:
    model = pkl.load(f)
st.title("Marks Analyzer")
st.header("Know own marks with one click✅")
st.write("marks are just a marks, not a certificate of your wisdom🧠")
st.set_page_config(
    page_title= "Marks Analyzer",
    page_icon= "icon.png"
)
hrs = st.number_input("Enter your number of hours that you studied📖")
bt = st.button("Click here to check marks.👆")
op = model.predict([[hrs]])[0]
print(op)
if bt:
    if hrs<0:
        st.error("You cannot study in negative hrs")
    elif 0< hrs <= 9.5:
        if op < 33:
            op = str(op)
            st.warning(f"you are fail with {op[:5]} marks.")

            op = str(op)
            st.info(f"you are pass with {op[:5]} marks.")
    elif hrs>24:
        st.error("enter hours less than 24hrs")
    else:
        st.success("Congratulations! you will get: 100 marks.") 
