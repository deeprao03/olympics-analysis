def medal_tally(df):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Year','City','Sport','Event','Medal'])
    medal_df = medal_df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_df['Total'] = medal_df['Gold'] + medal_df['Silver'] + medal_df['Bronze']
    return medal_df

def year_country(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')

    country = df['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0,'Overall')

    return years,country

def fetch_medal_tally(df,year,country):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Year','City','Sport','Event','Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df


    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region']==country]


    if year !='Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year']==year]


    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag==1:
        x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else:
        x  = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    return x


def participating_nations_over_time(df,col):
    nation_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('count')
    nation_over_time.rename(columns={'Year':'Edition','count':"No of Countries"},inplace=True)
    nation_over_time = nation_over_time.groupby('Edition')['No of Countries'].sum().reset_index()
    return nation_over_time

def participating_events_over_time(df,col):
    events_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('count')
    events_over_time.rename(columns={'Year':'Edition','count':"No of Events"},inplace=True)
    events_over_time = events_over_time.groupby('Edition')['No of Events'].sum().reset_index()
    return events_over_time

def participating_athletes_over_time(df,col):
    athletes_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('count')
    athletes_over_time.rename(columns={'Year':'Edition','count':"No of Athletes"},inplace=True)
    athletes_over_time = athletes_over_time.groupby('Edition')['No of Athletes'].sum().reset_index()
    return athletes_over_time

def most_successfull(df, sport):
    temp_df = df[df['Medal'] != 'No medal'].reset_index(drop=True)

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    # Count medals
    p = temp_df['Name'].value_counts().reset_index()
    p.rename(columns={'count':'Medals'},inplace=True)
    p = p.head(15)
    p = p.merge(temp_df,on='Name',how='left')[['Name','Medals','Sport','region']]
    p = p.drop_duplicates('Name')

    p = p.sort_values(by='Medals', ascending=False).reset_index(drop=True)
    p.index += 1
    p.index.name = 'Rank'

    return p
