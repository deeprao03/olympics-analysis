import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/deep_rao03/3 Month/Projects/Olympics/Data/olympics_dataset.csv")
region_df = pd.read_csv("/home/deep_rao03/3 Month/Projects/Olympics/Data/regions.csv")

df = preprocessor.preprocess(df,region_df)

st.sidebar.header("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)


if user_menu=='Medal Tally':

    st.sidebar.header("Medal Tally")

    years,country = helper.year_country(df)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Medal Tally")

    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Overall Medal Tally in "+str(selected_year))

    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title("Overall Medal Tally of "+selected_country)

    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title("Medal tally of "+selected_country+" in "+str(selected_year))
    
    st.table(medal_tally)

if user_menu =='Overall Analysis':
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]


    st.title("Top Stats")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)

    with col2:
        st.header("Hosts")
        st.title(cities)

    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)

    with col2:
        st.header("Nations")
        st.title(nations)

    with col3:
        st.header("Athletes")
        st.title(athletes)

    
    nations_over_time = helper.participating_nations_over_time(df,'region')
    fig = px.line(nations_over_time, x='Edition', y='No of Countries')
    st.title("Participating Nation Over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.participating_events_over_time(df,'Event')
    fig = px.line(events_over_time, x='Edition', y='No of Events')
    st.title("Total Events Over the Years")
    st.plotly_chart(fig)

    athletes_over_time = helper.participating_athletes_over_time(df,'Name')
    fig = px.line(athletes_over_time, x='Edition', y='No of Athletes')
    st.title("Participating Athletes Over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")

    x = df.drop_duplicates(['Year','Sport','Event'])
    x = x.pivot_table(index ='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype(int)
    fig, ax = plt.subplots(figsize=(20, 20))
    sns.heatmap(x, annot=True, ax=ax, linewidths=0.5)
    st.pyplot(fig)


    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successfull(df,selected_sport)
    st.table(x)