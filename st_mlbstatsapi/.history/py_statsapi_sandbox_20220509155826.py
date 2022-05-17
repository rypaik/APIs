import statsapi
import pandas as pd
import io
# import matplotlib as plot
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
 
 
# @timethis()
def get_rookie_hr_leader():
    # returns a str of search
    rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2021, playerPool = 'rookies', limit=15)
    
    # print(rookie_hr_leaders)
    # print(f"Return type: {type(rookie_hr_leaders)}")    
    rookies_pd = io.StringIO(rookie_hr_leaders)
    df = pd.read_csv(rookies_pd, sep='\t')
    df.select_dtypes(include='int')
    df.info()
    print(df["Rank Name                 Team                    Value"])
    
    
    # df.plot.bar()
    # get column names
    print(df.columns)
    
    
    
    # print(df.dtypes)
    # print(df.info())
    
    # access rows using .iloc[]
    # teams = df.iloc[10]
    # print(teams)
    # print(df)
    # return df
    
    # print(df)
    # data_top = df.head()
    # print(data_top)
#    for column in df.columns:
#        print(pd.api.types.infer_dtype(df[column]))
#        df[column] = df[column].apply(lambda x: pd.to_numeric(x, errors = 'ignore'))
#        df[column][df[column].apply(lambda x: isinstance(x, type))]
    
    # converts hr str into ints - type conversion in pandas
    # for col in df.columns:
    #     print(col)            
    # df.select_dtypes(include='int')
    
# Timer.run(1)




#from functools import wraps
#from time import time
#
#def timing(f):
#    @wraps(f)
#    def wrap(*args, **kw):
#        ts = time()
#        result = f(*args, **kw)
#        te = time()
#        print(f"func: {f.__name__}  args:{args},{kw} took{te-ts:2.4f} secs")
# 
#        # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
#            # (f.__name__, args, kw, te-ts)
#        return result
#    return wrap
#

#@timing
#def get_rookie_hr_leader():
#    rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2021, playerPool = 'rookies', limit=15)      # returns str
#    rookie_hr_leaders = rookie_hr_leaders.split('\n')                   # converts to list
#    df = pd.DataFrame(rookie_hr_leaders)
#    print(type(rookie_hr_leaders))
#    print(rookie_hr_leaders)
#    print(df)
#    
    
    
rookie_hr_leader = get_rookie_hr_leader()


# dicitonary to pandas

# or formatted text to pandas




# what can streamlit print??
# list?
# dictionary?




def rookie_hr_leader_dict():
    rookie_hr_leaders_d = statsapi.league_leader_data('homeRuns', season=2021, playerPool='rookies', limit= 15)
    print(rookie_hr_leaders_d)
    return rookie_hr_leaders_d

def hr_leader_pandas(hr_list):
    df = pd.DataFrame(hr_list)
    # df = df.transpose()
    df.columns = ['Rank', 'Player','Teams', 'HR' ]
    print(df)

list_r_hr_leaders = rookie_hr_leader_dict()
hr_leader_pandas(list_r_hr_leaders)