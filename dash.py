import streamlit as st
import pandas as pd
import plotly.graph_objects as go
  
st.title("Lunokhod warehouse data")
st.markdown("The dashboard will help workers to get to know information about the lunokhod bots status in a ware house")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
  
data = pd.read_csv("SampleRCAIIdashboard.csv")
  
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Bar Chart', 'Bubble Chart'))
  
st.sidebar.checkbox("Show Analysis by time", True, key = 1)
selected_status = st.sidebar.selectbox('Select any stats',
                                       options = ['picks', 
                                       'Distance_travelled_km'])
  
fig = go.Figure()

  
if chart_visual == 'Bar Chart':
    if selected_status == 'picks':
        fig.add_trace(go.Bar(x=data.name, y=data.picks,
                             name='No.of packages transported'))
    if selected_status == 'Distance_travelled_km':
        fig.add_trace(go.Bar(x=data.name, y=data.Distance_travelled_km,
                             name='Distance travelled by lunokhod'))
  
elif chart_visual == 'Bubble Chart':
    if selected_status == 'picks':
        fig.add_trace(go.Scatter(x=data.name, 
                                 y=data.picks,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='No.of packages transported'))
          
    if selected_status == 'Distance_travelled_km':
        fig.add_trace(go.Scatter(x=data.name, y=data.Distance_travelled_km,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='Distance travelled by lunokhod'))
          

st.plotly_chart(fig, use_container_width = True)