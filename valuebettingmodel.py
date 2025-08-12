import requests, pandas as pd 
import tensorflow as tf 
import numpy as np 
import pytorch
import pybetfair 
import Selenium
import requests 
from sportsipy.nfl.teams import Teams
import polars as pl
import pyMC, statsmodels
import XGBoost as xgb
from sklearn.metric import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

#Fetch data for all NFL teams 
teams = Teams()

#Collect data for each team 
team_data = []
for team in teams:
    team_data.append({
        "name": team.name,
        "wins": team.wins,
        "losses:": team.losses, 
        "points_for": team.points_for,
        "points_against": team.points_against,
        "yards": team.total_yards,
        "turnovers": team.turnovers
    })
    
#Convert to a DataFrame for data analysis
import pandas as pd 
team_df = pd.DataFrame(team_data)
print(team_df.head())

# Check if the data includes the latest season
latest_season_data = []
for team in teams:
    latest_season_data.append({
        "name": team.name,
        "season": team.season,
        "wins": team.wins,
        "losses": team.losses,
        "points_for": team.points_for,
        "points_against": team.points_against
        "yars_gained": team.total_yards, 
        "turnovers": team.turnovers, 
        "tuples": team.tuples, 
        "interceptions": team.interceptions,
        "yars_per_play": team.yards_per_play,
        "completion_percentage": team.completion_percentage,
        "red_zone_efficiency": team.red_zone_efficiency,
        "third_down_efficiency": team.third_down_efficiency,
    })

# Convert to DataFrame and filter for 2025 season
#Check if data for the latest season is available
latest_season_df = pd.DataFrame(latest_season_data)
season_2025_data = latest_season_df[latest_season_df['season'] == 2025]
#Filter for the last 5 seasons to predict the 2025 season 
season_2024_data = 2024-Season_df[2024_season_df['season'] == 2024]
season_2023_data = 2023-Season_df[2023_season_df['season'] == 2023]
season_2022_data = 2022-Season_df[2022_season_df['season'] == 2022]
season_2021_data = 2021-Season_df[2021_season_df['season'] == 2021]
season_2020_data = 2020-Season_df[2020_season_df['season'] == 2020]
#Combine data for model training 
pd.concat([season_2025_data, season_2024_data, season_2023_data, season_2022_data, season_2021_data, season_2020_data], ignore_index=True)

if not season_2025_data.empty:
    print("Data for the 2025 season is available:")
    print(season_2025_data.head())
else:
    print("Data for the 2025 season is not available in the sportsipy library.")
#Train a machine learning model to predict game outcomes
from sklearn.model_selection import train_test_split
# Prepare features and labels
x = team_df[[]]