import joblib
import streamlit as st


# from pathlib import Path

model = joblib.load("Sallary_Predictor.joblib")

# print(model.predict([[1.4]]))
# print(model.predict([[2.3]]))

st.title("Salary predictor ")
st.markdown("Here you will pass down year of experience and you will get predicted sallery : ")

year = st.text_input(label = "Year of Experience", placeholder="How many year of experience you have : ")

if st.button("Predict: "):
    output = model.predict([[float(year)]])
    st.write(f"The predicted sallery = {round(output [0])} rupees")
    # st.write (int(output [0]))



#    py -m streamlit run "C:\Users\Jay Mankotia\Desktop\AI ML\01 Salaery Pridictor\slr.ui.py"
