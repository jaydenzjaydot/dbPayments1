import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time

#importing dataframe
loans = pd.read_csv(r"C:\Users\SVNET Analyst\Documents\PYTHON\code\SLR_Dashboard\payments\dbPayments\LoansMasterFile.csv")
payments = pd.read_csv(r"C:\Users\SVNET Analyst\Documents\PYTHON\code\SLR_Dashboard\payments\dbPayments\PaymentsMaster.csv")
st.set_page_config(page_title = "SLR Dashboard",
page_icon = "Active",
layout = 'wide',initial_sidebar_state="auto",menu_items=None)
st.title("SLR Dashboard")
st.markdown('*Welcome* to the **new world** of ***Data Visualization***')
#top level filters
sector_filter=st.selectbox("Select the Sector",pd.unique(loans.sector))

#Data frame filter
df = loans[loans['sector']==sector_filter]

#Interactive Charts
fig_col1,fig_col2 = st.columns(2)

with fig_col1:
    st.markdown('### Chart 1')
    fig1=px.density_heatmap(data_frame=df,y='total_due',x='loan_cons_amt')
    st.write(fig1)

with fig_col2:
    st.markdown('### Chart 2')
    fig2 = px.histogram(data_frame=df,x='total_due')
    st.write(fig2)