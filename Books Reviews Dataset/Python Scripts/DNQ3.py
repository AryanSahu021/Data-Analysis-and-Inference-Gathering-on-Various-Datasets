import pandas as pd
df_ratings=pd.read_csv(r"C:\Users\aryan\Downloads\goodbooks-10k-master\goodbooks-10k-master\ratings.csv")
df_books=pd.read_csv(r"C:\Users\aryan\Downloads\goodbooks-10k-master\goodbooks-10k-master\books.csv")
df_tags=pd.read_csv(r"C:\Users\aryan\Downloads\goodbooks-10k-master\goodbooks-10k-master\tags.csv")
df_tagid=pd.read_csv(r"C:\Users\aryan\Downloads\goodbooks-10k-master\goodbooks-10k-master\book_tags.csv")
df_nobooks=df_ratings.drop(['book_id'],axis=1)
y=df_nobooks.value_counts()
print(y)