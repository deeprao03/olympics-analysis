import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# This function generates the heatmap pivot table (cached for speed)
@st.cache_data
def get_country_heatmap_data(df, country):
    temp_df = df[df['Medal'] != 'No medal'].drop_duplicates(
        subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal']
    )

    if country != "Overall":
        temp_df = temp_df[temp_df['region'] == country]

    pt = temp_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt


# This function draws the heatmap using the cached pivot table
def draw_country_event_heatmap(pt, country):
    fig, ax = plt.subplots(figsize=(26, 13))
    sns.heatmap(pt, annot=True, fmt='.0f', ax=ax)
    ax.set_title(f"Medals won by {country} (Sport vs Year)", fontsize=16)
    st.pyplot(fig)

@st.cache_data
def get_winter_event_heatmap(df):
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    pt = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)
    return pt

def draw_winter_event_heatmap(pt):
    fig, ax = plt.subplots(figsize=(20, 20))
    sns.heatmap(pt, annot=True, ax=ax, linewidths=0.5)
    st.pyplot(fig)

@st.cache_data
def generate_sport_event_heatmap(df):
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    heatmap_data = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)
    return heatmap_data

def draw_sport_event_heatmap(heatmap_data):
    fig, ax = plt.subplots(figsize=(20, 20))
    sns.heatmap(heatmap_data, annot=True, ax=ax, linewidths=0.5)
    st.pyplot(fig)