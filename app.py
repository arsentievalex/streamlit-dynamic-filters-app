import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi']
}

df = pd.DataFrame(data)

st.title("Dynamic Multi Select Filters in Streamlit")
st.subheader("This demo app shows how to use the DynamicFilters class to create dynamic multiselect filters in Streamlit.")

dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])

# display filters in the sidebar
with st.sidebar:
    dynamic_filters.display_filters()

# display dynamic dataframe in the main area
dynamic_filters.display_df()
