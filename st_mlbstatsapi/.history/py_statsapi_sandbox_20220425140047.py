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

Timer.run(1)




from functools import wraps
from time import time
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__} args:{args},{kw} took{te-ts:2.4f} secs")
 
        # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
            # (f.__name__, args, kw, te-ts)
        return result
    return wra
call by using decorator
@timing
def f(a):
   i = 0
   for i in range(a):
       i = i + 1 
       time.sleep(2)
   return(i)
func_output =f(10000)
print(func_output)  
@timing
def f(a):
    for i in range(a):
        i = 0
    return -1
