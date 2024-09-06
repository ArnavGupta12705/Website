import streamlit as st
import pandas as pd
import os

folder_name = "data"
excel_filepath = "data/expense.csv"

if not os.path.exists(folder_name):
  os.makedirs(folder_name)

if not os.path.exists(excel_filepath):
  expenses = pd.DataFrame(
      columns=['Date', 'Category', 'Description', 'Currency', 'Amount'])
  expenses.to_csv(excel_filepath, index=False)


def insert(date, category, description, currency_type, amount):
  print("add expense to csv file...testing")
  dataframe = pd.read_csv(excel_filepath)
  length = len(dataframe)

  if description != "" and amount > 0:

    dataframe.loc[length] = [
        date, category, description, currency_type, amount
    ]

    dataframe.to_csv(excel_filepath, index=False)

    st.balloons()

  else:
    st.error(
        'Please provide a description and a valid amount value greater than zero.',
        icon="🚨")


# Function to clear fields
def clear():
  st.session_state.am = 0
  st.session_state.desc = ""


# Input fields
date = st.date_input('Date')
category = st.selectbox("Category", [
    "Housing", "Utilities", "Transportation", "Food", "Healthcare",
    "Insurance", "Debt Payments", "Entertainment", "Personal Care",
    "Education", "Savings", "Taxes", "Miscellaneous"
])
description = st.text_area('Description :flashlight:', key='desc')
currency_type = st.selectbox("Currency Type :heavy_dollar_sign:",
                             ["Dollars", "Euros"])
amount = st.number_input('Amount',
                         key='am',
                         min_value=0,
                         step=1,
                         max_value=2000000)

# Buttons for adding and clearing expenses
col1, col2 = st.columns([0.24, 0.9])
with col1:
  add_expense = st.button("Add Expense :money_with_wings:")
with col2:
  clear_button = st.button("Clear :scissors:", on_click=clear)

# When add expense button is clicked
if add_expense:
  insert(date, category, description, currency_type, amount)
