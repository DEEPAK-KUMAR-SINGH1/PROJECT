import numpy as np
import pandas as pd
movies = pd.read_csv('tmdb_5000_movies.csv.zip')
credits = pd.read_csv('tmdb_5000_credits.csv.zip')
movies.head()

credits.head(1)['crew'].values
movies = movies.merge(credits,on='title')
movies.head()

movies['original_language'].value_counts
movies.info()
movies=(movies[['movie_id','title','overview','genres','keywords','cast','crew']])
movies.head()

movies.isnull().sum()
movies.dropna(inplace=True)
movies.duplicated().sum()
movies.iloc[0].genres
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

import ast
movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
print(movies.head)

def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    
    return L

#print(movies['cast'].apply(convert3))
def fatch_Director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            
            L.append(i['name'])
            break
    
    return L
#print(movies['crew'][0])
movies['crew'] = (movies['crew'].apply(fatch_Director))
print(movies.head)


movies['overview'] = movies['overview'].apply(lambda x:x.split())
print(movies.head())