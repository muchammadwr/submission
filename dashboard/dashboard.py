# Import library
import pandas as pd
import streamlit as st
import plotly.express as px

# Make title
st.set_page_config(
    page_title="Dashboard Sales",
    page_icon=':bar_chart',
    layout="wide"
)
st.title("Dashboard Sales")

# Read data 
df = pd.read_csv("data.csv")

# Sidebar
st.sidebar.header("Filter here")
payment = st.sidebar.multiselect(
    "Payment Type",
    options=df['payment_type'].unique(),
    default=df['payment_type'].unique()
)

df_selection = df.query(
    "payment_type == @payment"
)

total_sales = int(df_selection['order_id'].count())
average_rating = round(df_selection['review_score'].mean(), 1)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.header("Total Sales")
    st.subheader(total_sales)
with middle_column:
    st.header("Average Rating")
    st.subheader(average_rating)

st.markdown("---")

#  Most highest categorical product
st.subheader("Most highest categorical product sold")
categorical_count = df_selection.groupby(by='product_category_name_english').order_id.count().sort_values(ascending=False).reset_index().head(5)
fig_categorical_count = px.bar(
    categorical_count,
    x='product_category_name_english',
    y='order_id'
)
st.plotly_chart(fig_categorical_count)

# Number of sold in each city
st.subheader("Number of sold in each city")
city_sold = df_selection.groupby(by='customer_city').order_id.count().sort_values(ascending=False).reset_index().head(5)
fig_city_sold = px.bar(
    city_sold,
    x='customer_city',
    y='order_id'
)
st.plotly_chart(fig_city_sold)

# Number of average score rating in each product
st.subheader("Number of average score rating in each product")
average_score = df_selection.groupby(by='product_category_name_english').review_score.mean().sort_values(ascending=False).round(1).reset_index().head(5)
fig_average_score = px.bar(
    average_score,
    y='product_category_name_english',
    x='review_score')
st.plotly_chart(fig_average_score)