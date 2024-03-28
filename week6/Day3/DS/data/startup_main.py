import streamlit as st
import pickle 

def load_model():
    try:
        with open("week6/Day3/DS/data/mulmodel.pickle","br") as file:
            model = pickle.load(file)
        return model

    except FileNotFoundError as e:
        print(e)


def main():
    try:
        st.title("Profit Prediction App.")
        r_d_spend = st.text_input("Enter R&D Spend:")
        m_spend = st.text_input("Enter Marketing Spend:")
        if st.button("Predict"):
            model = load_model()
            y_pred = model.predict([[int(r_d_spend),int(m_spend)]])
            st.write(f"The profit with {r_d_spend} R&D Spend and {m_spend} Marketing Spend will be {round(y_pred[0],3)}.")
    except ValueError as e:
        st.write(e)

if __name__=='__main__':
    main()