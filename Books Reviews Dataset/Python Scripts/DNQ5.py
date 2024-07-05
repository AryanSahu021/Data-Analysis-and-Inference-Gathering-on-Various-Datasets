import pandas as pd
import matplotlib.pyplot as plt
df_ratings=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
df_books=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")
df_tags=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")
df_tagid=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv")
print('Total number of ratings given to all the books published in the years:')
x=[]
y=[]
for i in range(1990,2017):
    z=df_books['ratings_count'].loc[df_books['original_publication_year']==float(i)].sum()
    print(i,'-->',z)
    x.append(i)
    y.append(z)
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Number of total ratings (x10^7)')
plt.show()