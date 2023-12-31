import streamlit as st
import pickle
import joblib

st.set_page_config(page_title="ROMA")

def get_predicted(RA_Anti-CCP):
    with open("model_randomforestforRA.sav" , 'rb') as f:
        model_n = joblib.load(f)
    return model_n.predict(RA_Anti-CCP)


st.title("Anti-CCP Prediction in Rheumatoid Arthritis patients")

'Anti-CCP stands for anti-cyclic citrulline peptide and is an autoantibody. Autoantibodies are proteins that the immune system recognizes and attacks its own normal cells as foreign substances. These attacks produce the most common inflammatory manifestations in rheumatoid arthritis. '


form = st.form("RA_Anti-CCP")
with form:
    cols = st.columns((3, 3, 1))
    txt_gender = cols[0].text_input("Gender")
    txt_age = cols[0].text_input("Age")
    txt_crp = cols[0].text_input("CRP")
    txt_rf= cols[0].text_input("RF")
    txt_sedim = cols[0].text_input("Sedim")
    txt_hgb = cols[0].text_input("HGB")
    txt_hct = cols[0].text_input("HCT")
    txt_mcv = cols[0].text_input("MCV")
    txt_rdv = cols[0].text_input("RDW-CV")






    submitted = st.form_submit_button("Predict")

if submitted:
    result = get_predicted([[float(txt_gender), float(txt_age), float(txt_crp),
                              float(txt_rf), float(txt_sedim), float(txt_hgb), float(txt_hct), float(txt_mcv), float(txt_rdv)]])

    # st.success(result)

    # Format the result as a string
    result_str = f"Predicted anti-CCP value: {result[0]:.2f}"

# Print the result to the screen
    st.success(result_str)
