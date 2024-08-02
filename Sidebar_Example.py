import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters


# wide layout
st.set_page_config(layout="wide")

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
dates = {
    'years': [
        '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022',
        '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023',
        '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024',
              ],
    'months': [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
    ]
}

df = pd.DataFrame(data)
dt = pd.DataFrame(dates)

st.header("Dynamic Multi Select Filters in Streamlit")
st.write(
    "This demo app shows how to use the `DynamicFilters` class of the `streamlit-dynamic-filters` [package](https://github.com/arsentievalex/streamlit-dynamic-filters). "
    "The filters apply to a dataframe and adjust their values based on the user selection (similar to Google Sheets slicers or Only Relevant Values in Tableau).")

"""How to install and use the package:
1. Install the package using [pip](https://pypi.org/project/streamlit-dynamic-filters/):
    ```pip install streamlit-dynamic-filters```
2. Import the `DynamicFilters` class:
    ```from streamlit_dynamic_filters import DynamicFilters```
3. Create an instance of the `DynamicFilters` class and pass the dataframe and the list of fields that will serve as filters:

    ```dynamic_filters = DynamicFilters(df, filters=['col1', 'col2', 'col3', 'col4'])```
4. Display the filters in your app. The function takes location argument which can be either `sidebar` or `columns`.
    ```dynamic_filters.display_filters(location='sidebar')```
5. Display the filtered dataframe:
    ```dynamic_filters.display_df()```
6. Assign a filtered dataframe to a variable:
    ```df_filtered = dynamic_filters.filter_df()```
"""

code = """
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

dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])

with st.sidebar:
    st.write("Apply filters in any order 👇")
    
dynamic_filters.display_filters(location='sidebar')

dynamic_filters.display_df()

"""

with st.expander("See this app's code"):
    st.code(code, language='python')

dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'], filters_name='data2')
#dynamic_filters_dates = DynamicFilters(dt, filters=['years', 'months'], filters_name='dates2')

# display filters in the sidebar
with st.sidebar:
    st.write("Apply filters in any order 👇")

dynamic_filters.display_filters(location='sidebar')
#dynamic_filters_dates.display_filters(location='sidebar')

st.write("Filtered dataframe:")

# display dynamic dataframe in the main area
dynamic_filters.display_df()

#st.write("Filtered dates:")
#dynamic_filters_dates.display_df()

with st.sidebar:
    st.button("Reset Filters", on_click=dynamic_filters.reset_filters)

    st.write("Connect with me on [LinkedIn](https://www.linkedin.com/in/oleksandr-arsentiev-5554b3168/),"
             " [GitHub](https://github.com/arsentievalex), [Twitter](https://twitter.com/alexarsentiev)")

    st.write(
        "If you like this package, please consider giving it a ⭐ on [GitHub](https://github.com/arsentievalex/streamlit-dynamic-filters) or [buying me a coffee](https://www.buymeacoffee.com/arsentiev) ☕")
