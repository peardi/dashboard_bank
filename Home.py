import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.express.colors import sample_colorscale
from datetime import datetime, timedelta
import streamlit as st
import requests
import seaborn as sns
import matplotlib.pyplot as plt

#🛑 Code to set the Dashboard format to wide (the content will fill the entire width of the page instead of having wide margins)
def do_stuff_on_page_load():
    st.set_page_config(layout="wide")
do_stuff_on_page_load()

#Set Header
#🛑 Code to set the header
st.header('Model metrics', anchor=None)

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

#👇 Create 4 columns here using the apropriate Streamlit object. Save them as col1, col2, col3 and col4.
#👇 Reference material can be found here: https://docs.streamlit.io/library/api-reference/layout/st.columns
col1, col2 = st.columns(2)


num_applicants = df_original.size
default_count = df_original[df_original['TARGET'] == 1].shape[0]
repay_count = df_original[df_original['TARGET'] == 0].shape[0]
default_rate = (default_count/num_applicants)*100

num_test = df_test.size

df_original['AGE'] =-(df_original['DAYS_BIRTH'] / 365).astype(int)

#split into numeric
num_features = ['AMT_ANNUITY',
        'AMT_CREDIT',
        'AMT_GOODS_PRICE',
        'CNT_CHILDREN',
        'CNT_FAM_MEMBERS',
        'DAYS_EMPLOYED',
        'DAYS_ID_PUBLISH',
        'DAYS_LAST_PHONE_CHANGE',
        'DAYS_REGISTRATION',
        'DAYS_BIRTH'
        ]

#split into categorical
cat_features = ['CODE_GENDER',
        'FLAG_OWN_CAR',
        'FLAG_OWN_REALTY',
        'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS',
        'NAME_HOUSING_TYPE',
        'NAME_INCOME_TYPE',
        'OCCUPATION_TYPE',
        'FLAG_EMAIL',
        'FLAG_PHONE',
        'FLAG_WORK_PHONE',
        ]

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

#👇 Create an expander container widget with title "Theme Explorer Sunburst". Remember that everything contained on the container must be idented
with st.expander(f"Categorical Features relationship with target",expanded=True):

    #👇 Create spinner that displays "Loading..." while running. 
    with st.spinner(text="Loading..."):
        #👇 Paste the code created in activity 3.1 to produce a list of parent themes

        

        #👇 Create a select box widget to gather from the user what Parent Theme is to be output. Pass the following label 'What theme do you want to explore?' as well as the list_parent_themes
        # Save the user selected option to a chosen_theme variable

        option_cat = st.selectbox('What categorical features do you want to explore?',cat_features)
        st.write('You selected:', option_cat)

        #👇 Paste the code created in activity 3.1 to produce the df_sunburst DataFrame
        fig = sns.catplot(data=df_original, x=option_cat, hue='TARGET', kind='count', height=6, aspect=2)
    
        
        #👇 Use a plotly widget from Streamlit to visualize the fig_sunburst plot. Pass the parameter use_container_width =True to ensure the visualization expands to the container width.
        st.pyplot(fig)
#👇 Create an expander container widget with title "Theme Explorer Sunburst". Remember that everything contained on the container must be idented
with st.expander(f"Numerical Features relationship with target",expanded=True):

    #👇 Create spinner that displays "Loading..." while running. 
    with st.spinner(text="Loading..."):


        option_num = st.selectbox('What numerical features do you want to explore?',num_features)
        st.write('You selected:', option_num)

        fig = plt.figure(figsize=(10, 6))
        sns.histplot(df_original, x=option_num, hue='TARGET')
    
        
        #👇 Use a plotly widget from Streamlit to visualize the fig_sunburst plot. Pass the parameter use_container_width =True to ensure the visualization expands to the container width.
        st.pyplot(fig)
