import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

excel_file_path = r"data/expense.csv"


def execution():
  try:
    dataframe = pd.read_csv(excel_file_path)
    if len(dataframe) != 0:
      max_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].max()]
      st.subheader("You are spending the most here :cry:")
      st.dataframe(max_Amount.reset_index(drop=True))

      min_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].min()]
      st.subheader("You are spending the least here :blush:")
      st.dataframe(min_Amount.reset_index(drop=True))

      st.subheader("You made the most number of transactions on :date:")
      most_transactions_date = dataframe.groupby(
          by="Date").size().nlargest(1).index
      st.dataframe(most_transactions_date)

      st.subheader("You made the least number of transactions on :date:")
      least_transactions_date = dataframe.groupby(
          by="Date").size().nsmallest(1).index
      st.dataframe(least_transactions_date)
      mode_Category = dataframe["Category"].mode()
      st.subheader("The categories for which you are spending the most :cry:")
      st.dataframe(mode_Category.reset_index(drop=True))
      st.subheader(
          "The categories for which you are spending the least :blush:")
      least_spent_category = dataframe["Category"].value_counts().idxmin()
      st.dataframe(dataframe[dataframe["Category"] == least_spent_category]
                   ["Category"].reset_index(drop=True))
      Description_data = ' '.join(list(dataframe["Description"].values))

      def generate_wordcloud(text):
        wordcloud = WordCloud(width=400, height=400,
                              background_color=None).generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

      st.subheader("Description cloud :cloud:")
      generate_wordcloud(Description_data)
    else:
      st.header("Please add some expenses before analyzing it")
  except FileNotFoundError:
    st.header("Please add some expenses before analyzing it")


execution()
