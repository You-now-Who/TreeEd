import requests
import os
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {"Authorization": "Bearer " + st.secrets['HF_API_KEY']}

def get_topics(q):
	payload = {
		"inputs": "Can you give me one word examples of the list of stuff I need to know to learn - " + q + " in increaing order of difficulty as a begginer roadmap? Sure here are the one word topics, seperated by commas: Google topic,  ",
	}
	response = requests.post(API_URL, headers=headers, json=payload)
	topics = response.json()[0]['generated_text'].split(": ")[1].split(", ")
	topics = topics[1:]
	return topics

def get_ai_help(q):
	payload = {
		"inputs": "Can you give me detailed explanation on how can I learn - " + q,
	}
	response = requests.post(API_URL, headers=headers, json=payload)
	text = response.json()[0]['generated_text'].split("- ")[1]
	return text

if __name__ == "__main__":
	q = "painting"
	output = get_topics(q) 
	print(output)