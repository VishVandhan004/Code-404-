import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
ds=pd.read_csv(r"C:\Users\guna5\OneDrive\Documents\covid_worldwide.csv")
df=pd.DataFrame(ds)
print(df)
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
print(x)
print(y)
print(df.isnull().sum())
df1=df.copy()
print("Before:",df1.shape)
df1.dropna(inplace=True)
print("After:",df1.shape)
df2=df.copy()
df2.fillna(df2.mean(),inplace=True)
print(df2.isnull().sum())
print(df2)
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
df2['Country']=labelencoder.fit_transform(df2['Country'])
print(df2['Country'].unique())
print(df2)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
print(X_train)
print(y_train)
type(X_train)
from sklearn.preprocessing import StandardScaler
sta=StandardScaler()
X_train[:,3:]=sta.fit_transform(X_train[:,3:])
X_test[:,3:]=sta.transform(X_test[:,3:])
print(X_train[:,3:])
print(X_test[:,3:])