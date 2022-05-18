import statsapi
import pandas as pd
from pprint import pprint


import logging
logger = logging.getLogger('statsapi')
logger.setLevel(logging.DEBUG)
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)8s - %(name)s(%(thread)s) - %(message)s")
ch.setFormatter(formatter)
rootLogger.addHandler(ch)




# statsapi.schedule(date=None, start_date=None, end_date=None, team="", opponent="", sportId=1, game_id=None)

# dict_keys(['game_id', 'game_datetime', 'game_date', 'game_type', 'status', 'away_name', 'home_name', 'away_id', 'home_id', 'doubleheader', 'game_num', 'home_probable_pitcher', 'away_probable_pitcher', 'home_pitcher_note', 'away_pitcher_note', 'away_score', 'home_score', 'current_inning', 'inning_state', 'venue_id', 'venue_name', 'winning_team', 'losing_team', 'winning_pitcher', 'losing_pitcher', 'save_pitcher', 'summary'])





# games_list = statsapi.schedule(start_date='05/16/2022',end_date='05/16/2022')
# # print(games_list[0].keys())
# for games in games_list:
#     print(f"Game id: {games['game_id']}: {games['away_name']} vs {games['home_name']}")
    
    