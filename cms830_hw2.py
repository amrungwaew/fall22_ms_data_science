import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

df_iris = sns.load_dataset('iris')
labels = df_iris.columns
df_form = pd.DataFrame(df_iris, columns = labels)
df_px = px.data.iris()
px_handle = px.scatter_3d(df_px, x='sepal_length', y='sepal_width', z='petal_width', color='species', max_size=5)
st.plotly_chart(px_handle)