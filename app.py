import streamlit as st
import pandas as pd
import os

import pandas_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

if 'running' not in st.session_state:
    st.session_state.running = True

with st.sidebar:
    st.title('Data-chain')
    choice=st.radio('Navigate through the app',['Upload your file','Profiling your columns','Train your model','Download the trained model','Download the analysis file'])
    st.info("Data-Chain is your hassle-free data analysis companion. Upload your data, get automated insights, and train models without any coding. It's quick, simple, and perfect for non-coders.")

if os.path.exists("data.csv"):
    df=pd.read_csv("data.csv",index_col=None)

if choice=='Upload your file':
    st.title('Upload your data for modelling')
    file=st.file_uploader("Upload your data here")
    try:
        if file:
            df=pd.read_csv(file,index_col=None)
            df.to_csv("data.csv",index=None)
            st.dataframe(df)
    except FileNotFoundError as e:
        pass

elif choice=='Profiling your columns':
    st.title("Automated Exploratory Data Analysis")
    try:
        profile_df = df.profile_report()
        st_profile_report(profile_df)

        profile_df.to_file("profile_report.html")

        st.markdown("[Download the Profile Report as HTML](profile_report.html)")

    except NameError as e:
        st.write("It seems like you haven't uploaded your dataset, kindly upload it by going to `Upload your file` in the sidebar")

elif choice=='Train your model':
    
    model_choice=st.radio('Choose the type of modelling',['Classification','Regression'])
    st.title("Machine Learning")
    col_choice=st.selectbox("Select your target",df.columns)
    if model_choice=='Classification':
        from pycaret.regression import setup,compare_models,pull,save_model
    if model_choice=='Regression':
        from pycaret.classification import setup,compare_models,pull,save_model
    if st.button('Train model'):
        setup(df,target=col_choice)
        setup_df=pull()
        st.info("These are the settings for the model")
        st.dataframe(setup_df)
        best_model=compare_models()
        compare_df=pull()
        st.info("These are the model comparisons")
        st.dataframe(compare_df)
        best_model
        save_model(best_model,'final_model')

elif choice=='Download the trained model':
    st.title("Download the model")
    with open("final_model.pkl",'rb') as f:
        st.download_button("Download the Model",f,"final_model.pkl")

elif choice=='Download the analysis file':
    st.title("Download the index.html")
    with open("index.html",'rb') as f:
        st.download_button("Download the index.html",f,"index.html")

if not st.session_state.running:
    os.remove('final_model.pkl')
    os.remove('data.csv')
    os.remove('profile_report.html')
    os.remove('model.pkl')
    os.remove('final_model.pkl')
    os.remove('input_data.csv')
    os.remove('index.html')  # Add this line to remove index.html
