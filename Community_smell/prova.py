import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carica i dati da un file Excel
df = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_globe.xlsx')  # Sostituisci 'tuo_file_excel.xlsx' con il percorso del tuo file

# Escludi le righe con valori NaN nelle colonne CV_1 a CV_9 e 'black'
df = df.dropna(subset=['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9', 'black'])


# Seleziona le colonne CV_1 a CV_9 come feature e 'black' come variabile dipendente
X = df[['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9']]
y = df['black']

# Crea un modello di regressione lineare
model = LinearRegression()

# Addestra il modello sulla variabile dipendente 'black'
model.fit(X, y)

# Ora puoi ottenere i coefficienti della regressione
coefficients = model.coef_
intercept = model.intercept_

print("Coefficients:", coefficients)
print("Intercept:", intercept)

# Calcola i residui
residuals = y - model.predict(X)

# Grafico dei residui rispetto alla variabile prevista
plt.scatter(model.predict(X), residuals)
plt.xlabel('Valori previsti')
plt.ylabel('Residui')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Grafico dei residui vs. Valori previsti')
plt.show()

# Grafico di dispersione dei residui rispetto alle variabili indipendenti
for col in X.columns:
    plt.scatter(X[col], residuals, alpha=0.5, label=col)
    plt.xlabel('Valore di ' + col)
    plt.ylabel('Residui')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title('Grafico di dispersione dei residui vs. ' + col)
    plt.show()

# Grafico QQ-plot per verificare la normalità degli errori
import scipy.stats as stats
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('QQ-Plot degli errori')
plt.show()
