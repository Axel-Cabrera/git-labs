import streamlit as st
import requests
import pandas  as pd
import json

def post_spark_job(user, repo, job, token):
    # Define the API endpoint
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/dispatches'
    # Define the data to be sent in the POST request
    payload = {
      "event_type": job
    }

    headers = {
      'Authorization': 'Bearer ' + token,
      'Accept': 'application/vnd.github.v3+json',
      'Content-type': 'application/json'
    }

    st.write(url)
    st.write(payload)
    st.write(headers)

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Display the response in the app
    st.write(response)

def get_spark_results(url_results):
    response = requests.get(url_results)
    st.write(response)

    if  (response.status_code ==  200):
        st.write(response.json())




st.title("Spark & streamlit")

st.header("spark-submit Job")

github_user  =  st.text_input('Github user', value='adsoftsito')
github_repo  =  st.text_input('Github repo', value='bigdata')
spark_job    =  st.text_input('Spark job', value='spark')
github_token =  st.text_input('Github token', value='***')

if st.button("POST spark submit"):
    post_spark_job(github_user, github_repo, spark_job, github_token)

st.header("spark-submit results")

url_results=  st.text_input('URL results', value='https://raw.githubusercontent….')

if st.button("GET spark results"):
    get_spark_results(url_results)

