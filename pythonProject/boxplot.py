import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leggi il file Excel
file_excel = 'C:\\Users\\saver\\PycharmProjects\\pythonProject\\file_filtrato_globe.xlsx'  # Sostituisci con il percorso del tuo file Excel
df = pd.read_excel(file_excel)

# Nomi delle colonne da analizzare
colonne_da_analizzare = ['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9']

# Crea un boxplot per ciascuna colonna
for colonna in colonne_da_analizzare:
    # Rimuovi i valori NaN dalla colonna
    colonna_senza_nan = df[colonna].dropna()

    # Crea il boxplot per la colonna senza NaN
    plt.figure()  # Crea una nuova figura per ciascuna colonna
    plt.boxplot(colonna_senza_nan, vert=False)
    plt.title(f'Boxplot della colonna {colonna}')
    plt.xlabel('Colonna')
    plt.ylabel('Valori')
    plt.show()