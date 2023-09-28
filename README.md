# Multi Select Filters Demo App

[![Open Demo App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dynamic-filters-demo.streamlit.app/)

This demo app shows how to use the `DynamicFilters` class of the `streamlit-dynamic-filters` [package](https://github.com/arsentievalex/streamlit-dynamic-filters). The filters apply to a dataframe and adjust their values based on the user selection (similar to Google Sheets slicers or Only Relevant Values in Tableau).

Sample usage:

```
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
    }

df = pd.DataFrame(data)

dynamic_filters = DynamicFilters(df, filters=['Region', 'Country', 'City'])

dynamic_filters.display_filters(location='sidebar')

dynamic_filters.display_df()
```

Demo GIF:
<img src="https://i.postimg.cc/mDG8BfK4/multiselect-demo.gif"/>   
