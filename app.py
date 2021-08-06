# Core Pkg
import streamlit as st 
import streamlit.components.v1 as stc 
# Load EDA
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
from sklearn.decomposition import LatentDirichletAllocation
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize
import ipywidgets
from ipywidgets import interact


st.write("# Drug Prescription Wizard")

message_text = st.text_input("Enter a condition")

pd.options.display.max_columns = 30
df = pd.read_csv('drug.csv', encoding="latin-1", na_values='')
df.head()
print('We have ', len(df), 'conditions in the data')

#delete all the records where Condition is Missing
df = df.dropna()
df['review']= df['review'].astype(str)
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
    return text
    
df['review'] = df['review'].apply(clean_text)

# lets remove the unique Id, date, review, len, and sentiment column also
df = df.drop(['date','uniqueID','review'], axis = 1)

# Lets Calculate an Effective Rating
min_rating = df['rating'].min()
max_rating = df['rating'].max()

def scale_rating(rating):
    rating -= min_rating
    rating = rating/(max_rating -1)
    rating *= 5
    rating = int(round(rating,0))

    if(int(rating) == 0 or int(rating)==1 or int(rating)==2):
        return 0
    else:
        return 1
    
df['eff_score'] = df['rating'].apply(scale_rating)
# lets also calculate Usefulness Score
df['usefulness'] = df['rating']*df['usefulCount']*df['eff_score']
# lets remove all the Duplicates from the Dataset
df = df.drop_duplicates()

# lets find the Highest and Lowest Rated Drugs for each Condition
#@interact
def high_low_rate(condition = list(df['condition'].value_counts().index)):
    Top_5_Drugs = df[df['condition'] == condition][['drugName','usefulness']].sort_values(by = 'usefulness', ascending = False).head().reset_index(drop = True)

    Bottom_5_Drugs = df[df['condition'] == condition][['drugName','usefulness']].sort_values(by = 'usefulness', ascending = True).head().reset_index(drop = True)

    return Top_5_Drugs


if message_text != '':

	result = high_low_rate(message_text)

st.write("Top 5 Drugs")
st.write(result)
