from fuzzywuzzy import fuzz as fuzzywuzzy_fuzz, process as fuzzywuzzy_process
from rapidfuzz import fuzz as rapidfuzz_fuzz, process as rapidfuzz_process
import Levenshtein

import pandas as pd
import numpy as np
from timeit import default_timer as timer
from functools import wraps
import ipywidgets as widgets

def print_timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        t0 = timer()
        try:
            return f(*args, **kwargs)
        finally:
            print(f"\n{f.__name__} finished in {1e3*(timer()-t0):.1f} ms")
    return inner




df = pd.read_csv("Index_of_Place_Names_in_Great_Britain_(July_2016).csv")
cities = df["place15nm"].unique()

@print_timing
def interact_cities(input_text):
    if not input_text: return
    for city, score, _ in rapidfuzz_process.extract(input_text, cities, limit=10):
        print(f"{city:60}{score:3.2f}")

# widgets.interact(interact_cities, input_text="");




# USING FUZZYWUZZY LIBRARY
# 


# "Fuzzy" (approximate) string matching looks for strings that are similar to a given string. Here are some great libraries you can use for this task in Python:

#     fuzzywuzzy, a fuzzy text matching library ported to many languages, including JS (https://github.com/seatgeek/fuzzywuzzy)
#     rapidfuzz, a performance-oriented version of fuzzywuzzy (GitHub)
#     difflib from Python standard library (docs)


fuzzywuzzy_fuzz.ratio("Tokyo and Osaka", "Tokio and Osaka")
print(fuzzywuzzy_fuzz.ratio("Tokyo and Osaka", "Tokio and Osaka")) 


words = ["knight", "knuth", "nigh", "ignite", "knighthood", "knead", "the"]
fuzzywuzzy_process.extract("knigth", words)

print(fuzzywuzzy_process.extract("knigth", words))



# HOW DO THESE ALGORITHMS WORK
"mancesther" == "manchester"