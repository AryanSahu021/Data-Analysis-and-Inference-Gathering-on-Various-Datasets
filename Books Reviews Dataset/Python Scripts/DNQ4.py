import pandas as pd

df_ratings=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
df_books=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")
df_tags=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")
df_tagid=pd.read_csv(r"https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv")
x=df_books['authors'].value_counts()
print(x.head(10))
