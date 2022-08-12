import streamlit as st
import pandas as pd
import numpy as np
import requests




json = requests.get('https://visits.evofitness.no/api/v1/locations/1e724456-b640-4b03-9b65-0cf7734aa38e/current').json()


st.title(json)


