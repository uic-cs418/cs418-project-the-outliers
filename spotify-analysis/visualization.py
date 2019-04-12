import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import GetTopYearly
import GetTop50Country

def get_csv(filename):
    return pd.read_csv(filename)

def get_country_csv(country):
    """
    Opens the Top50.csv file for the country provided.

    Args:
        country(string): the country to open
    Returns:
        pandas dataset
    """
    return get_csv('top50CountryCSV/' + country + "Top50.csv")

def get_yearly_csv(year):
    """
    Opens the TopTracks.csv file for the year provided.

    Args:
        country(string): the year to open
    Returns:
        pandas dataset
    """
    return get_csv('topTracksYearsCSV/' + year + "TopTracks.csv")

def makeDanceabilityBarPlot(countrya, countryb):
    """
    Creates a seaborn distribution plot for the dancability of the
    two countries provided.

    Args:
        countrya, countryb (string): the two countries to compare
    """
    countryAcsv = get_country_csv(countrya)
    countryBcsv = get_country_csv(countryb)
    sns.distplot(countryAcsv['danceability'], label=countrya + ' Danceability',)
    sns.distplot(countryBcsv['danceability'], label=countryb + ' Danceability')
    plt.title(countrya + ' VS ' + countryb + ' danceability')
    plt.xlabel('Danceability')
    plt.legend()
    plt.show()


def makeLoudnessBarplot(countrya, countryb):
    """
    Creates a seaborn distribution plot for the loudness of the
    two countries provided.

    Args:
        countrya, countryb (string): the two countries to compare
    """
    countryAcsv = get_country_csv(countrya)
    countryBcsv = get_country_csv(countryb)
    sns.distplot(countryAcsv['loudness'], label=countrya + ' Loudness')
    sns.distplot(countryBcsv['loudness'], label=countryb + ' Loudness')
    plt.title(countrya + ' VS ' + countryb + ' loudness')
    plt.xlabel('Loudness')
    plt.legend()
    plt.show()

def create_yearly_features_dotplot(featurea, featureb):
    """
    Creates a dot plot outline of the features provided for all of the yearly data
    """
    all_data = pd.DataFrame()
    for year in GetTopYearly.top_playlists_per_year:
        year_pd = get_yearly_csv(year)
        year_pd["year"] = year
        all_data = pd.concat([year_pd, all_data])
        
    sns.set(style="whitegrid")
    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="year")
    plt.title("Yearly data " + featurea + ' VS ' + featureb )
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
    plt.show()

def create_country_features_dotplot(featurea, featureb):
    """
    Creates a dot plot outline of the features provided for all of the yearly data
    """
    all_data = pd.DataFrame()
    for country in GetTop50Country.top_playlists_per_country:
        country_pd = get_country_csv(country)
        country_pd["country"] = country
        all_data = pd.concat([country_pd, all_data])
        
    sns.set(style="whitegrid")
    sns.stripplot(x=featurea, y=featureb, data=all_data, hue="country")
    plt.title("Country data " + featurea + ' VS ' + featureb )
    plt.show()

if __name__ == "__main__":
    makeDanceabilityBarPlot("Australia", "UnitedStates")
    makeLoudnessBarplot("Australia", "UnitedStates")
    create_yearly_features_dotplot("loudness", "danceability")
    create_country_features_dotplot("loudness", "danceability")
