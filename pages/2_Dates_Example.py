import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

def clear_cache():
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)

# wide layout
st.set_page_config(layout="wide")

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

dt = pd.DataFrame(dates)

st.header("Dynamic Multi Select Filters in Streamlit")
st.write("This demo app shows how to use the `DynamicFilters` class of the `streamlit-dynamic-filters` [package](https://github.com/arsentievalex/streamlit-dynamic-filters). "
             "The filters apply to a dataframe and adjust their values based on the user selection (similar to Google Sheets slicers or Only Relevant Values in Tableau).")


dynamic_filters = DynamicFilters(dt, filters=['years', 'months']
                                 ,filters_name="dates"
                                 )

# display filters in the sidebar
st.write("Apply filters in any order 👇")

dynamic_filters.display_filters(location='columns', num_columns=2, gap='large')

st.write("Filtered dataframe:")

# display dynamic dataframe in the main area
dynamic_filters.display_df()

with st.sidebar:
    st.button('Reset All Filters', on_click=clear_cache)
    st.write("Connect with me on [LinkedIn](https://www.linkedin.com/in/oleksandr-arsentiev-5554b3168/),"
             " [GitHub](https://github.com/arsentievalex), [Twitter](https://twitter.com/alexarsentiev)")

    st.write("If you like this package, please consider giving it a ⭐ on [GitHub](https://github.com/arsentievalex/streamlit-dynamic-filters) or [buying me a coffee](https://www.buymeacoffee.com/arsentiev) ☕")
