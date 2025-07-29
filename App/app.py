import streamlit as st
import pandas as pd
import helper
import plotly.express as px
from visualizations import get_country_heatmap_data, draw_country_event_heatmap,draw_winter_event_heatmap,get_winter_event_heatmap,generate_sport_event_heatmap,draw_sport_event_heatmap


@st.cache_data
def load_summer_data():
    return pd.read_pickle("Data/Summer_Olympics_processed_data.pkl")

@st.cache_data
def load_winter_data():
    return pd.read_pickle("Data/Winter_Olympics_processed_data.pkl")

df = load_summer_data()
winter_df = load_winter_data()

st.sidebar.image("Data/Olympic_Flag.png")
st.sidebar.header("Olympics Analysis")
selected_olympics = st.sidebar.selectbox('Select Olympics',['Summer Olympics','Winter Olympics'])
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis')
)

if selected_olympics=='Summer Olympics':
    if user_menu=='Medal Tally':

        st.sidebar.header("Summer Olympics Medal Tally")

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

        heatmap_data = generate_sport_event_heatmap(df)
        draw_sport_event_heatmap(heatmap_data)


        st.title("Most Successful Athletes")
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0,'Overall')

        selected_sport = st.selectbox('Select a Sport',sport_list)
        x = helper.most_successfull(df,selected_sport)
        st.table(x)


    if user_menu=='Country-wise Analysis':

        st.sidebar.title("Country Wise Analysis")
        country = df['region'].dropna().unique().tolist()
        country.sort()
        selected_country = st.sidebar.selectbox('Select a Country',country)

        country_df = helper.yearwise_medal_tally(df,selected_country)
        fig = px.line(country_df,x='Edition',y='Medal')
        st.title("Performance of "+selected_country+" over the years")
        st.plotly_chart(fig)

        st.title(selected_country+" excels in the following")
        pt = get_country_heatmap_data(df, selected_country)
        if not pt.empty:
            draw_country_event_heatmap(pt, selected_country)
        else:
            st.write("No data available to display heatmap for this selection.")



        st.title("Top 10 athletes of "+selected_country)
        top10_df = helper.most_successfull_countryWise(df,selected_country)
        st.table(top10_df)

else:
    if user_menu=='Medal Tally':

        st.sidebar.header("Winter Olympics Medal Tally Till 2014")

        years,country = helper.year_country(winter_df)
        selected_year = st.sidebar.selectbox("Select Year",years)
        selected_country = st.sidebar.selectbox("Select Country",country)
        
        medal_tally = helper.fetch_medal_tally(winter_df,selected_year,selected_country)

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
        editions = winter_df['Year'].unique().shape[0]-1
        cities = winter_df['City'].unique().shape[0]
        sports = winter_df['Sport'].unique().shape[0]
        events = winter_df['Event'].unique().shape[0]
        athletes = winter_df['Name'].unique().shape[0]
        nations = winter_df['region'].unique().shape[0]


        st.title("Top Stats till year 2014")

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

        
        nations_over_time = helper.participating_nations_over_time(winter_df,'region')
        fig = px.line(nations_over_time, x='Edition', y='No of Countries')
        st.title("Participating Nation Over the Years")
        st.plotly_chart(fig)

        events_over_time = helper.participating_events_over_time(winter_df,'Event')
        fig = px.line(events_over_time, x='Edition', y='No of Events')
        st.title("Total Events Over the Years")
        st.plotly_chart(fig)

        athletes_over_time = helper.participating_athletes_over_time(winter_df,'Name')
        fig = px.line(athletes_over_time, x='Edition', y='No of Athletes')
        st.title("Participating Athletes Over the Years")
        st.plotly_chart(fig)

        st.title("No. of Events over time(Every Sport)")

        pt = get_winter_event_heatmap(winter_df)
        draw_winter_event_heatmap(pt)



        st.title("Most Successful Athletes")
        sport_list = winter_df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0,'Overall')

        selected_sport = st.selectbox('Select a Sport',sport_list)
        x = helper.most_successfull(winter_df,selected_sport)
        st.table(x)
    
    if user_menu=='Country-wise Analysis':

        st.sidebar.title("Country Wise Analysis")
        country = winter_df['region'].dropna().unique().tolist()
        country.sort()
        selected_country = st.sidebar.selectbox('Select a Country',country)

        country_df = helper.yearwise_medal_tally(winter_df,selected_country)
        fig = px.line(country_df,x='Edition',y='Medal')
        st.title("Performance of "+selected_country+" over the years")
        st.plotly_chart(fig)

        st.title(selected_country+" excels in the following")
        pt = get_country_heatmap_data(winter_df, selected_country)
        if not pt.empty:
            draw_country_event_heatmap(pt, selected_country)
        else:
            st.write("No data available to display heatmap for this selection.")

        st.title("Top 10 athletes of "+selected_country)
        top10_df = helper.most_successfull_countryWise(winter_df,selected_country)
        st.table(top10_df)