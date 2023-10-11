import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

df = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_globe.xlsx')
df = df.dropna(subset=['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9', 'black'])

X = df[['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9']]
y = df['black']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

y_pred = linear_regression.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("RMSE:", rmse)
print("R²:", r2)

plt.scatter(y_test, y_pred)
plt.xlabel("Valori osservati")
plt.ylabel("Valori predetti")
plt.title("Valori osservati vs Valori predetti")
plt.show()


residuals = y_test - y_pred
sns.histplot(residuals, kde=True)
plt.xlabel("Residui")
plt.title("Distribuzione dei residui")
plt.show()

plt.scatter(y_pred, residuals)
plt.xlabel("Valori predetti")
plt.ylabel("Residui")
plt.title("Valori predetti vs Residui")
plt.show()

