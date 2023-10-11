import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Carica i dati da un file Excel
data = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_hofstede.xlsx')

# Verifica la presenza di valori NaN nelle colonne CV_1 a CV_9
columns_to_check = ['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6']

# Filtra le righe con valori NaN nelle colonne specificate
data = data.dropna(subset=columns_to_check)

# Rimuovi i valori outlier basati su un criterio (ad esempio, 3 deviazioni standard dalla media)
# Puoi utilizzare un altro criterio appropriato al tuo dataset
data = data[(np.abs(data['CV_1'] - data['CV_1'].mean()) / data['CV_1'].std()) < 3]
data = data[(np.abs(data['CV_2'] - data['CV_2'].mean()) / data['CV_2'].std()) < 3]
data = data[(np.abs(data['CV_3'] - data['CV_3'].mean()) / data['CV_3'].std()) < 3]
data = data[(np.abs(data['CV_4'] - data['CV_4'].mean()) / data['CV_4'].std()) < 3]
data = data[(np.abs(data['CV_5'] - data['CV_5'].mean()) / data['CV_5'].std()) < 3]
data = data[(np.abs(data['CV_6'] - data['CV_6'].mean()) / data['CV_6'].std()) < 3]


# Definisci le variabili indipendenti (CV_1 a CV_9) e la variabile dipendente (black)
X = data[['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6']]
y = data['black']

# Calcola la matrice di correlazione tra le variabili indipendenti
correlation_matrix = X.corr()

# Visualizza la matrice di correlazione come una heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Matrice di Correlazione tra Variabili Indipendenti')
plt.show()

# Calcola il VIF per ciascuna variabile indipendente
vif = pd.DataFrame()
vif["Variabile"] = X.columns
vif["VIF"] = [1 / (1 - np.corrcoef(X[col], y)[0, 1]**2) for col in X.columns]

# Visualizza i valori di VIF
print("Valori di VIF:")
print(vif)

# Aggiungi una costante per il termine noto (intercetta) nel modello
X = sm.add_constant(X)

# Crea il modello di regressione lineare
model = sm.OLS(y, X).fit()

# Stampa un riepilogo delle statistiche del modello
print(model.summary())
# Verifica le assunzioni della regressione lineare

# 1. Assunzione di linearità
for column in X.columns[1:]:
    sns.scatterplot(x=X[column], y=model.resid)
    plt.axhline(0, color='red', linestyle='--')  # Aggiungi la retta che passa per lo zero
    plt.xlabel(column)
    plt.ylabel('Residui')
    plt.title('Verifica di Linearità: ' + column)
    plt.show()


# 2. Assunzione di indipendenza degli errori
# (Questo controllo richiede dati raccolti in ordine temporale)

# 3. Assunzione di omoscedasticità degli errori
sns.scatterplot(x=model.predict(X), y=model.resid)
plt.axhline(0, color='red', linestyle='--')  # Aggiungi la retta che passa per lo zero
plt.xlabel('Previsioni')
plt.ylabel('Residui')
plt.title('Verifica di Omoscedasticità')
plt.show()

# 4. Assunzione di normalità degli errori
sm.qqplot(model.resid, line='s')
plt.title('Verifica di Normalità degli Errori')
plt.show()
