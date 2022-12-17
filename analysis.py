import pandas as pd
import matplotlib.pyplot as plt

# Initialize dataframe
df = pd.read_csv('vgsales.csv', index_col='Rank')


# Group by Genre 					--------------------------------------------------
df_genre = df[['Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Genre'])

# # Sum / Total Sales
# print(df_genre.sum())

# # Max
# print(df_genre.max())

# # Min - returns a table of zeros
# print(df_genre.min())

# # Count
# print(df_genre[['Global_Sales']].count())


# # Group by Publisher				----------------------------------------------

# df_pub = df[['Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Publisher'])

# # Sum / Total Sales
# print(df_pub.sum().sort_values('Global_Sales', ascending=False))

# # Max
# print(df_pub.max().sort_values('Global_Sales', ascending=False))

# # Min
# print(df_pub.min().sort_values('Global_Sales', ascending=False))

# # Count
# print(df_pub.count().sort_values('Global_Sales', ascending=False)['Global_Sales'])


# # Group by Publisher and Genre	----------------------------------------------

# df_genre_pub = df[['Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Genre', 'Publisher'])

# # How much each publisher made per genre
# print(df_genre_pub.sum().sort_values('Global_Sales', ascending=False).to_string())

# # How many games did each publisher make per genre
# print(df_genre_pub.size().to_string())

# # Is it more profitable to specialize or diversify?
# df_pub2 = df[['Publisher', 'Genre', 'Global_Sales']].groupby(['Publisher'])

# pub2_nun = df_pub2.agg({'Genre': pd.Series.nunique, 'Global_Sales': pd.Series.sum})
# print(pub2_nun.sort_values('Global_Sales', ascending=False).to_string())

# # Number of games and total sales - Here you can see each publisher's profitablity by game
# pub2_games = df_pub2['Global_Sales'].agg(['sum', 'count'])
# pub2_games['sum/count'] = pub2_games['sum'] / pub2_games['count']
# print(pub2_games.sort_values('sum/count', ascending=False).to_string())


# Group by Platform				----------------------------------------------

df_plat = df[['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Platform'])

# Total sales by platform
print(df_plat.sum().sort_values('Global_Sales', ascending=False).to_string())

# Group by Platform and Genre
df_plat_gen = df[['Platform', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Platform', 'Genre'])

# Number of Games per Platform and Genre
print(df_plat_gen.size().to_string())

# # Group By Year					----------------------------------------------

df_year = df[['Year', 'Publisher', 'Platform', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby(['Year'])
print(df_year.sum().to_string())

dfsum = df_year.sum()
dfsum.plot(color=['r','b','g','y','m'])
plt.show()