import pandas as pd

# get info about dataframe
# df.info()




# Basic syntax:
dataframe = pd.DataFrame.from_dict(json_data, orient="index")




# Example usage:
import json
import pandas as pd

# Make json-formatted string:
json_string = '{ "name":"John", "age":30, "car":"None" }'
your_json = json.loads(json_string)
print(your_json)


# Reading simple JSON from URL
URL = 'http://raw.githubusercontent.com/BindiChen/machine-learning/master/data-analysis/027-pandas-convert-json/data/simple.json'

df = pd.read_json(URL)


# get info about dataframe
df.info()


# Nested JSON Data to Pandas

{
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}


import json
# load data using Python JSON module
with open('nested_array.json','r') as f:
    data = json.loads(f.read())# Flatten data
df_nested_list = pd.json_normalize(data, record_path =['students'])

# To include school_name and class
df_nested_list = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=['school_name', 'class']
)






## FALTTENIGN NESTED LIST AND DICT IN JSON

{
    "school_name": "local primary school",
    "class": "Year 1",
    "info": {
      "president": "John Kasich",
      "address": "ABC road, London, UK",
      "contacts": {
        "email": "admin@e.com",
        "tel": "123456789"
      }
    },
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}


import json
# load data using Python JSON module
with open('data/nested_mix.json','r') as f:
    data = json.loads(f.read())
    
# Normalizing data
df = pd.json_normalize(data, record_path =['students'])

df = pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=[
        'class',
        ['info', 'president'], 
        ['info', 'contacts', 'tel']
    ]
)




## Extracting a single Value from deeply Nested JSON

"""
{
    "school_name": "local primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "grade": {
            "math": 60,
            "physics": 66,
            "chemistry": 61
        }
  
    },
    {
        "id": "A002",
        "name": "James",
        "grade": {
            "math": 89,
            "physics": 76,
            "chemistry": 51
        }
        
    },
    {
        "id": "A003",
        "name": "Jenny",
        "grade": {
            "math": 79,
            "physics": 90,
            "chemistry": 78
        }
    }]
}
"""



from glom import glom
df = pd.read_json('data/nested_deep.json')
df['students'].apply(lambda row: glom(row, 'grade.math'))


# 0    60
# 1    89
# 2    79
# Name: students, dtype: int64




# get  LIST of column Names 
my_list = list(df)  

# faster version
my_list = df.columns.values.tolist()




# pandas timing example
from timeit import default_timer
import pandas as pd

data = {'Name': ['Bill','Maria','David','James','Mary'],
        'Age': [32,45,27,59,37],
        'Country': ['Spain','Canada','Brazil','UK','France']
        }

df = pd.DataFrame(data)

beginning = default_timer()
my_list = list(df)
ending = default_timer()

print((ending - beginning)*1000)