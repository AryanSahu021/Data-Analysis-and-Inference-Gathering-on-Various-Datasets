import pandas as pd
df_ratings=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
df_books=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")
df_tags=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")
df_tagid=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv")
df_joined=df_tags.set_index('tag_id').join(df_tagid.set_index('tag_id'))
gbid=df_books['goodreads_book_id'].loc[df_books['authors']=='J.K. Rowling']
a=df_joined['tag_name'].loc[df_joined['goodreads_book_id'].isin(gbid)] 
x=a.value_counts()
print(x)

