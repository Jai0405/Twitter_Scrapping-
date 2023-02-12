# Twitter_Scrapping-
#IMPORT mATERIAL
import streamlit as st
import pandas as pd
from PIL import Image
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import numpy as np
import json
import base64

#BASICS
st.set_page_config(page_title="scrapper.app")

st.header("Twitter scrapping")

st.markdown("Twitter scraping refers to the process of extracting data from Twitter.The extracted data can be used for a variety of purposes, such as sentiment analysis, market research, trend analysis, and more.")

st.subheader("Tamil_Spotify Tweets")


#IMAGE UPLOAD
pic= Image.open(r"C:\Users\lenove\Downloads\35-351629_tweet-your-new-spotify-saved-tracks-twitter.png")
st.image(pic)
 
#IMPORT SCRAPPED DATE SET
df = pd.read_csv("Spotify_Tweets.csv")

Submit = st.checkbox("Click to view Total Data")
if Submit:
    st.dataframe(df)

# DOWNLOAD OPTION
st.download_button("Download CSV File as CSV",df.to_csv(),
                   file_name='Spotify_Tweets.csv',mime='csv')

#FILTER BY HASHTAG

st.header("Hashtag Filter") 

hashtag = st.text_input('Enter hashtag:')

def filter_data(hashtag, df):
    filtered_df = df[df['CONTENT'].str.contains(hashtag, na=False)]
    return filtered_df
      
if hashtag:
    filtered_df = filter_data(hashtag, df)
    st.write(filtered_df)
    
if st.button('Download as CSV'):
   
   csv = filtered_df.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Spotify_tweets.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

if st.button("Download as JSON "):
    filtered_data_json = filtered_df.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Spotify_tweets.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)


#DATE RANGE FILTERING

st.header('Date Range Filter')

#CHANGE THE DATE FORMAT

df['DATE'] = pd.to_datetime(df['DATE'] )

Start_Date = st.date_input('Enter the Start date:',value= df["DATE"].min().date())

Start_Date = pd.to_datetime(Start_Date).strftime("%Y-%m-%d %H:%M:%S")


End_Date = st.date_input('Enter the End date:',value= df["DATE"].max().date())
End_Date = pd.to_datetime(End_Date).strftime("%Y-%m-%d %H:%M:%S")

#FILTERING
filtered_date = df[(df["DATE"] >= Start_Date) & (df["DATE"] <= End_Date)]

st.write("Number of tweets:",filtered_date.shape[0])
st.dataframe(filtered_date)

#Add to download option as CSV

if st.button('Download as CSV~ Click Here'):
   
   csv = filtered_date.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Spotify_tweets.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

#Add to download option as JSON

if st.button("Download as JSON ~ Click Here"):
    filtered_data_json = filtered_date.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Spotify_tweets.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)
    
