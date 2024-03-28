import sklearn
import streamlit as st
import pickle

def load_model():
    with open("week6/Day3/DS/data/model.pickle","br") as file:
        lr_model = pickle.load(file)
    return lr_model

def main():
    st.title("Salary Prediction App")
    yoe = st.text_input("Enter years of experience:")
    if st.button("Predict"):
        model = load_model()
        y_pred = model.predict([[int(yoe)]])
        st.write(f"The salary of {yoe} years of experiencce will be {round(y_pred[0],3)}.")




if __name__ == "__main__":
    main()
