import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data= {
      "experience": [5,8,12,15,20,25,30,35,40],
      "salary": [30000,35000,40000,45000,50000,55000,60000,65000,70000]
}

df=pd.DataFrame(data)
print(df)

x = df[["experience"]]
y = df["salary"]

plt.plot(x, y, marker="o")
plt.title("Experience vs Salary")
plt.xlabel("Experience (years)")
plt.ylabel("Salary (USD)")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)
print("Training data:")
print(x_train)

print("Testing data:")
print(x_test)

print("Training labels:")
print(y_train)

print("Testing labels:")
print(y_test)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Predicted values:",np.round(y_pred))