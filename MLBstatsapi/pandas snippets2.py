pandas snippets




# from csv string to 
https://stackoverflow.com/questions/53278358/convert-from-string-to-pandas-dataframe


from csv import reader
import pandas as pd
data=["a,b,c,d,\"x,y\",e,f"]
df=pd.DataFrame( list(reader(data)))
print df
Output:

   0  1  2  3    4  5  6
0  a  b  c  d  x,y  e  f






# convert string to integer pandas
https://www.geeksforgeeks.org/how-to-convert-string-to-integer-in-pandas-dataframe/

# import pandas library
import pandas as pd
 
# dictionary
Data = {'Name': ['GeeksForGeeks','Python'],
          'Unique ID': ['900','450']}
 
# create a dataframe object
df = pd.DataFrame(Data)
 
# convert string to an integer
df['Unique ID'] = df['Unique ID'].astype(int)
 
# show the dataframe
print (df)
print("-"*25)
 
# show the data types
# of each columns
print (df.dtypes)



# Mixed Type
# import pandas library
import pandas as pd
 
# dictionary
Data = {'Algorithm': ['Graph', 'Dynamic Programming',
                      'Number Theory',
                      ' Sorting And Searching'],
         
          'Problems': ['62', '110', '40', '55']}
 
# create a dataframe object
df = pd.DataFrame(Data)
 
# convert string to integer
df['Problems'] = df['Problems'].astype(int)
 
# show the dataframe
print (df)
print("-"*25)
 
# show the data type
# of each columns
print (df.dtypes)