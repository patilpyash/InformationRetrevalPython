import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['first text','second text','third text','this is first text?']
vectorizer=CountVectorizer()
X=vectorizer.fit_transform(corpus)
print("Fit transfer is")
print(X.toarray())
df=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
print("the genearated data frame is")
print(df)
alldata=df[(df['this']==1) & (df['first']==1)]
print("Indices where both 'this' and 'first' terms are present are",alldata.index.tolist())
ordata=df[(df['this']==1) | (df['first']==1)]
print("Indices where either 'this' or 'first' terms are present are",ordata.index.tolist())
notdata=df[(df['and']!=1)]
print("indices where AND term is not present",notdata.index.tolist())          
