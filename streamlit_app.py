import streamlit as st
import pandas as pd
import numpy as np
import requests




json = requests.get('https://visits.evofitness.no/api/v1/locations/1e724456-b640-4b03-9b65-0cf7734aa38e/current').json()



name = json['name']
max_capacity = json['max_capacity']
percentageUsed = round(float(json['percentageUsed']), 2)
current_visitors = json['current']

# Make a nice output text with the variable above
output = f'{name} \n Kapasitet: {max_capacity} \n Antall personer som er på besøk nå: {current_visitors} \n Ledighet: {percentageUsed}'

st.title(output)


