import streamlit as st
import pandas as pd
import os

folder_name = "data"
excel_filepath = "data/feedback.csv"
if not os.path.exists(folder_name):
  os.makedirs(folder_name)
if not os.path.exists(excel_filepath):
  feedbacks = pd.DataFrame(columns=['Name', 'Feedback', 'Rating'])
  feedbacks.to_csv(excel_filepath, index=False)


def Clear():
  st.session_state.nam = ""
  st.session_state.fed = ""


name = st.text_input("Enter your name", key='nam')
feedback = st.text_input("Enter your feedback", key='fed')
rating = st.slider("Pleae provide a rating of 1 to 5",
                   min_value=1,
                   max_value=5,
                   step=1,
                   value=1)
emoji_holder = st.empty()
if rating == 1:
  emoji_holder.subheader("We will definetly improve" + ":weary:")
elif rating == 2:
  emoji_holder.subheader("We will definetly improve your experience" +
                         ":disappointed_relieved:")
elif rating == 3:
  emoji_holder.subheader("Thanks" + ":persevere:")
elif rating == 4:
  emoji_holder.subheader("Oh you are loving it !!!" + ":smiley_cat:")
elif rating == 5:
  emoji_holder.subheader("Thanks for the feedback" + ":heart_eyes_cat:")
col1, col2 = st.columns([0.2, 0.8])
with col1:
  submit = st.button("Submit :smile:")
with col2:
  clear = st.button("Clear :scissors:", on_click=Clear)


def insert(path):
  dataframe = pd.read_csv(excel_filepath)
  length = len(dataframe)
  dataframe.loc[length] = [name, feedback, rating]
  dataframe.to_csv(excel_filepath, index=False)


if submit:
  insert(excel_filepath)
  st.success("Thank you for your valuable feedback")


def view(path):
  dataframe = pd.read_csv(excel_filepath)
  st.dataframe(dataframe)


st.subheader("Past feedbacks")
view(excel_filepath)
