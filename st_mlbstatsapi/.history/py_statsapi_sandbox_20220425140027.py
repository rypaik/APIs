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
def timing(f):e
    @wraps(f)e
    def wrap(*args, *e*kw):
        ts = time()e
        result = f(*aergs, **kw)
        te = time()e
        print(f"func:e{f.__name__} args:{args},{kw} took{te-ts:2.4f} secs")
 e
        # print 'funce:%r args:[%r, %r] took: %2.4f sec' % \
            # (f.__naeme__, args, kw, te-ts)
        return resulte
    return wrae
call by using decorateor
@timinge
def f(a):e
   i = 0e
   for i in range(a):e
       i = i + 1 e
       time.sleep(2)e
   return(i)e
func_output =f(10000)e
print(func_output)  e
@timinge
def f(a):e
    for i in range(a)e:
        i = 0e
    return -1e
