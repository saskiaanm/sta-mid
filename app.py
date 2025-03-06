git init  
git add .  
git commit -m "First commit"  
git branch -M main  
git remote add origin https://github.com/saskiaanm/sta-mid.git
git push -u origin main  

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Data extracted from the image
data = {
    'jenis_bencana': ['Tornado', 'Flood', 'Tidal Wave', 'Earthquake', 'Volcanic Eruption', 
                      'Forest Fire', 'Drought', 'Landslide', 'Tsunami'],
    '2012': [543, 581, 29, 12, 7, 49, 263, 287, 0],
    '2013': [500, 710, 36, 6, 8, 21, 66, 293, 0],
    '2014': [618, 588, 20, 13, 4, 100, 7, 598, 2],
    '2015': [571, 523, 7, 25, 9, 46, 7, 502, 0],
    '2016': [663, 820, 22, 10, 7, 178, 19, 598, 0],
    '2017': [885, 973, 11, 17, 1, 96, 129, 844, 0],
    '2018': [804, 673, 34, 22, 58, 370, 33, 473, 2],
    '2019': [568, 247, 8, 13, 4, 55, 33, 355, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df.set_index('jenis_bencana', inplace=True)
df_transposed = df.T

st.title("Disaster Data Visualization")

st.subheader("Summary Statistics")
st.write(df.describe())

midpoints = (df.max(axis=1) + df.min(axis=1)) / 2
st.subheader("Midpoints")
st.write(midpoints)

class_boundaries = pd.concat([df.min(axis=1), df.max(axis=1)], axis=1)
class_boundaries.columns = ['Lower Boundary', 'Upper Boundary']
st.subheader("Class Boundaries")
st.write(class_boundaries)

st.subheader("Mean")
st.write(df.mean(axis=1))

st.subheader("Median")
st.write(df.median(axis=1))

st.subheader("Mode")
st.write(df.mode(axis=1))

st.subheader("Frequency Table")
st.write(df)

st.subheader("Column Graph")
st.bar_chart(df)

st.subheader("Line Graph")
st.line_chart(df_transposed)

st.subheader("Area Chart")
st.area_chart(df_transposed)

st.subheader("Histogram")
fig, ax = plt.subplots()
df.plot(kind='hist', alpha=0.7, ax=ax, bins=20, figsize=(12, 6), title='Histogram for Disaster Data')
st.pyplot(fig)

st.subheader("Pie Chart (2019 Data)")
fig, ax = plt.subplots()
df['2019'].plot(kind='pie', autopct='%1.1f%%', ax=ax, figsize=(8, 8), title='Pie Chart for 2019 Disaster Data')
st.pyplot(fig)

st.subheader("Stem and Leaf Plot")
for disaster in df.index:
    st.text(f"{disaster}: {' '.join(str(x) for x in df.loc[disaster] if x != 0)}")
