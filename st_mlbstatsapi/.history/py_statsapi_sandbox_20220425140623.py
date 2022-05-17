import statsapi
import pandas as pd

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


# from ptimeit import timethis, Timer

# @timethis()
# def get_rookie_hr_leader():
#     rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2021, playerPool = 'rookies', limit=15)
#     print(rookie_hr_leaders)

# Timer.run(1)




from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func: {f.__name__}  args:{args},{kw} took{te-ts:2.4f} secs")
 
        # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
            # (f.__name__, args, kw, te-ts)
        return result
    return wrap


@timing
def get_rookie_hr_leader():
    rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2021, playerPool = 'rookies', limit=15)      # returns str
    rookie_hr_leaders = rookie_hr_leaders.split('\n')   
    print(type(rookie_hr_leaders))
    print(rookie_hr_leaders)
    
    
get_rookie_hr_leader()