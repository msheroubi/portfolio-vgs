# Code base from geeksforgeeks.org

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('vgsales.csv', index_col='Rank')

comment_words = ''
stopwords = set(STOPWORDS)

Genre = 'Simulation'

df_genre = df.loc[df['Genre'] == Genre]

# iterate through the csv file
for idx, row in df_genre.iterrows():
	
	# typecaste each val to string
	val = str(row['Name'])

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.savefig(f'{Genre}.png')
# plt.show()
