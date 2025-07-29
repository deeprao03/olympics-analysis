import pandas as pd

def year_country(df):
    """Return list of years and countries with 'Overall' at the top."""
    years = sorted(df['Year'].dropna().unique().tolist())
    years.insert(0, 'Overall')

    countries = sorted(df['region'].dropna().unique().tolist())
    countries.insert(0, 'Overall')

    return years, countries


def fetch_medal_tally(df, year, country):
    """Return medal tally based on year and/or country."""
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
        group_field = 'region'
    elif year == 'Overall':
        temp_df = medal_df[medal_df['region'] == country]
        group_field = 'Year'
    elif country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == year]
        group_field = 'region'
    else:
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]
        group_field = 'region'

    agg_df = temp_df.groupby(group_field)[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    agg_df['Total'] = agg_df['Gold'] + agg_df['Silver'] + agg_df['Bronze']

    if group_field == 'region':
        agg_df = agg_df.sort_values(by='Gold', ascending=False).reset_index(drop=True)
    else:
        agg_df = agg_df.sort_values(by=group_field).reset_index(drop=True)

    return agg_df


def participating_nations_over_time(df, col):
    """Return number of participating nations over the years."""
    df_unique = df.drop_duplicates(['Year', col])
    counts = df_unique['Year'].value_counts().reset_index()
    counts.columns = ['Edition', 'No of Countries']
    counts = counts.sort_values('Edition').reset_index(drop=True)
    return counts


def participating_events_over_time(df, col):
    """Return number of unique events over the years."""
    df_unique = df.drop_duplicates(['Year', col])
    counts = df_unique['Year'].value_counts().reset_index()
    counts.columns = ['Edition', 'No of Events']
    counts = counts.sort_values('Edition').reset_index(drop=True)
    return counts


def participating_athletes_over_time(df, col):
    """Return number of unique athletes over the years."""
    df_unique = df.drop_duplicates(['Year', col])
    counts = df_unique['Year'].value_counts().reset_index()
    counts.columns = ['Edition', 'No of Athletes']
    counts = counts.sort_values('Edition').reset_index(drop=True)
    return counts


def most_successfull(df, sport):
    """Return top 15 most successful athletes overall or by sport."""
    temp_df = df[df['Medal'] != 'No medal']
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    p = temp_df['Name'].value_counts().reset_index()
    p.columns = ['Name', 'Medals']

    p = p.head(15)
    p = p.merge(temp_df[['Name', 'Sport', 'region']], on='Name', how='left')
    p = p.drop_duplicates('Name')
    p = p.sort_values(by='Medals', ascending=False).reset_index(drop=True)

    p.index += 1
    p.index.name = 'Rank'
    return p


def yearwise_medal_tally(df, country):
    """Return year-wise medal tally for a specific country."""
    temp_df = df[df['Medal'] != 'No medal']
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    new_df = temp_df[temp_df['region'] == country]

    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    final_df.rename(columns={'Year': 'Edition'}, inplace=True)
    return final_df


def country_event_heatmap(df, country):
    """Return a heatmap-style pivot table of medals by sport and year for a country."""
    temp_df = df[df['Medal'] != 'No medal']
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    new_df = temp_df[temp_df['region'] == country]

    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt


def most_successfull_countryWise(df, country):
    """Return top 10 most successful athletes from a specific country."""
    temp_df = df[(df['Medal'] != 'No medal') & (df['region'] == country)]

    p = temp_df['Name'].value_counts().reset_index()
    p.columns = ['Name', 'Medals']
    p = p.head(10)

    p = p.merge(temp_df[['Name', 'Sport']], on='Name', how='left')
    p = p.drop_duplicates('Name')
    p = p.sort_values(by='Medals', ascending=False).reset_index(drop=True)

    p.index += 1
    p.index.name = 'Rank'
    return p
