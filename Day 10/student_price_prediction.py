import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "hours": [1,2,3,4,5,6,7,8,9],
    "marks": [10,20,30,40,50,60,70,80,90]
}

df=pd.DataFrame(data)
print(df)

x =df[['hours']]
y = df['marks']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# 1,3,4,5,6,7,9
print("Training data:")
print(x_train)

# 2,8
print("Testing data:")
print(x_test)

#10,30,40,50,60,70,90
print("Training labels:")
print(y_train)

# 20,80
print("Testing labels:")
print(y_test)
model =LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Predicted values:", y_pred)

new_data = pd.DataFrame([[15]], columns=["hours"])
prediction = model.predict(new_data)
print("Predicted marks for 15 hours of study:", prediction)