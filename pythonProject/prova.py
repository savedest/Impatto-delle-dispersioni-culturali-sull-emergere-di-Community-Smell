import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leggi il file Excel
file_excel = 'C:\\Users\\saver\\PycharmProjects\\pythonProject\\file_filtrato_globe.xlsx'
df = pd.read_excel(file_excel)

# Nomi delle colonne da analizzare
colonne_da_analizzare = ['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9']

# Crea un Violin Plot separato per ciascuna colonna
for colonna in colonne_da_analizzare:
    plt.figure(figsize=(6, 4))  # Imposta le dimensioni del grafico
    sns.violinplot(x=df[colonna], inner="quart", palette="pastel")
    plt.title(f'Violin Plot di {colonna}')
    plt.xlabel('Valori')
    plt.ylabel('Distribuzione')
    plt.grid(True)
    plt.show()
