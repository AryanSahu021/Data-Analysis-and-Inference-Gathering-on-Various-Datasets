import pandas as pd
df_ratings=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
df_books=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")
df_tags=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")
df_tagid=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv")
years_no=df_books['original_publication_year'].value_counts().rename_axis('Year').to_frame('counts')
x=years_no.loc[years_no['counts']>=100]

y=x.sort_values('Year',ascending=True)
print(y)
y.plot(kind='bar')