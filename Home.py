import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.express.colors import sample_colorscale
from datetime import datetime, timedelta
import streamlit as st
import requests

#🛑 Code to set the Dashboard format to wide (the content will fill the entire width of the page instead of having wide margins)
def do_stuff_on_page_load():
    st.set_page_config(layout="wide")
do_stuff_on_page_load()

#Set Header
#🛑 Code to set the header
st.header('Model metrics', anchor=None)

#Set Sidebar Elements
#🛑 Code to set the Sidebar
with st.sidebar:
    st.header('Filters', anchor=None)
    values = st.slider(
        'Select the Start and End Years',
        1950, 2017, (1950, 2017))
    min_year = values[0]
    max_year = values[1]
    st.write('Date Range: '+str(values[0])+'-01-01 to '+str(values[1])+'-01-01')

#🛑 Code to import the dataset
df_original = pd.read_csv('https://miles-become-a-data-scientist.s3.us-east-2.amazonaws.com/J3/M3/data/train.csv')
url_test = 'https://drive.google.com/file/d/116hMPDLUX79i964j7JDGukQ2HWn5vZnS/view?usp=drive_link'


# Download the file from Google Drive
file_content = requests.get(url_test).content

# Save the file to a local directory
with open('X_test_proc_dff.csv', 'wb') as f:
    f.write(file_content)

# Use the file in your Streamlit app
df_test = pd.read_csv('X_test_proc_dff.csv')

# Display the data
st.write(df.head())

#👇 Create 4 columns here using the apropriate Streamlit object. Save them as col1, col2, col3 and col4.
#👇 Reference material can be found here: https://docs.streamlit.io/library/api-reference/layout/st.columns
col1, col2 = st.columns(2)


num_applicants = df.size
default_count = df_original[df_original['TARGET'] == 1].shape[0]
repay_count = df_original[df_original['TARGET'] == 0].shape[0]
default_rate = (default_loans/num_applicants)*100

num_test = df_test.size


#👇 Use col1.metric(title,value) to produce a column with the metric_new_master_themes metric. Set the title to "New Master Themes"
col1.metric('Number applicants',num_applicants)


#👇 Create a metric with the metric_new_themes and set it to col2. Give it the title "New Themes". The procedure is similar to the one you performed before
col2.metric('default rate',default_rate)



# Get the number of missing values in the dataframe
missing_values = df_original.isnull().sum()

# Get the distribution of the target variable
target_distribution = df_original['TARGET'].value_counts()

# Print the results
st.write('There are {} missing values in the dataframe.'.format(missing_values.sum()))
st.write('The target variable is distributed as followss:')
st.write(target_distribution)
