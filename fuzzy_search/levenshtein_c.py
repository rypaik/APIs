import Levenshtein

import pandas as pd
import numpy as np
# from timeit import default_timer as timer
# import timeit
from functools import wraps
from ptimeit import timethis, Timer



df = pd.read_csv("Index_of_Place_Names_in_Great_Britain_(July_2016).csv")
cities = df["place15nm"].unique()
print(cities)

a = "londen"
# a_vec = np.asarray([ord(c) for c in a])

for b in cities: Levenshtein.distance(a,b)


# %timeit [Levenshtein.distance(a, b) for b in cities]
# timeit.Timer('for b in cities: Levenshtein.distance(a,b)').timeit()

#TODO: add a workign function timer


# @timethis()
# def time_levenshtein():
#     print(f"cities again: {cities}")
#     for b in cities: Levenshtein.distance(a,b)

# Timer.run()