#TODO: Move Pandas Links to Craft
# PANDAS LINKS
[pandas.read_json — pandas 1.4.2 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)









[Endpoints · toddrob99/MLB-StatsAPI Wiki](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints)
Enpoints are used in statsapi.get(Endpoints)



[Function - Schedule](https://github.com/toddrob99/MLB-StatsAPI/wiki/Function:-schedule)














# LINKS
## MLB-StatsAPI

[GitHub - toddrob99/MLB-StatsAPI: Python wrapper for MLB Stats API](https://github.com/toddrob99/MLB-StatsAPI)
[MLB-StatsAPI · PyPI](https://pypi.org/project/MLB-StatsAPI/)


[Statsapi module Documentation](https://github.com/toddrob99/MLB-StatsAPI/wiki)

[Using the MLB Stats API to Get Daily Data | by Austin L.E. Krause | Better Programming](https://betterprogramming.pub/using-the-mlb-stats-api-to-get-daily-data-88f48266656c) 

[Intro to MLB-StatsAPI — Part 2. Showing you how to use a couple of new… | by Austin L.E. Krause | Better Programming](https://betterprogramming.pub/intro-to-mlb-stats-api-part-2-f47564651d01)


## MLB DATA API
[MLB - Sign In](https://mlb.okta.com/) 


[MLB Data API](https://appac.github.io/mlb-data-api-docs/#header-1.-request-structure) 
[MLB Stats, Scores, History, & Records | Baseball-Reference.com](https://www.baseball-reference.com/) 
[pandas - Python Data Analysis Library](https://pandas.pydata.org/) 
[How to Deploy a Python + Flask API on Heroku | by Debbie | Level Up Coding](https://levelup.gitconnectedcom/how-to-deploy-a-python-flask-api-on-heroku-2e5ddfd943ef) 
[baseball-scraper · PyPI](https://pypi.org/project/baseball-scraper/) 
## Baseball-reference API
[Sportsipy: A free sports API written for python — sportsipy 0.1.0 documentation](https://sportsreference.readthedocs.io/en/stable/) 
[Swagger UI](https://api.blaseball-reference.com/docs#/Stat%20Leaders/get_v2_stats_leaders) 



-------
## ENDPOINTS
[ENDPOINTS](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints)



[meta](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapivervenues)
[team](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapiverteamsteamidleaders)
[team leaders](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapiverteamsteamidleaders)


[team roster](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapivervenues)

[transactions](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapivertransactions)

[venue](https://github.com/toddrob99/MLB-StatsAPI/wiki/Endpoints#url-httpsstatsapimlbcomapivervenues)















# import statsapi

get_division_standings([league], [division]) -> standings: df
league = AL, NL
division :  west, central, east
**df headers**
['name', 'div_rank', 'gb', 'w', 'l', 'elim_num', 'wc_rank', 'wc_gb', 'wc_elim_num']




get_division_standings(103,201)     # AL EAST
get_division_standings(103,202)     # AL CENTRAL
get_division_standings(103,200))     # AL WEST
get_division_standings(104,203))     # NL WEST
get_division_standings(104,204))     # NL EAST
get_division_standings(104,205))     # NL CENTRAL



ctags:



TODO: (need to make parameterized functions with team input, date)
num_wins()







