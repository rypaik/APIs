import statsapi
import pandas as pd
from ptimeit import timethis, Timer

# logging
import logging
logger = logging.getLogger('statsapi')
logger.setLevel(logging.DEBUG)
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)8s - %(name)s(%(thread)s) - %(message)s")
ch.setFormatter(formatter)
rootLogger.addHandler(ch)
from ptimeit import timethis, Timer
@timethis()
def get_rookie_hr_leader():
    rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2021, playerPool = 'rookies', limit=15)
    print(rookie_hr_leaders)

Timer.run()