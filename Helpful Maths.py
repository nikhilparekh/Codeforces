import pandas as pd
from sklearn.linear_model import LinearRegression

data = {"Mileage":[22,25,30,45,50,60],"Price":[1000,1200,1400,3000,6000,10000]}
test = [20,30,25]
df = pd.DataFrame.from_dict(data)
lm= LinearRegression()
X=df[["Mileage"]]
Y=df[["Price"]]
lm.fit(X,Y)
predict = lm.predict(X)
print(predict)
print(lm.coef_)
print(lm.intercept_)