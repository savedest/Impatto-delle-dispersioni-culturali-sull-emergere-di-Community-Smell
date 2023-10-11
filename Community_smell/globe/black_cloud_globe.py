import json
import pandas as pd
import numpy as np

# Specifica il percorso del tuo file JSON
file_path = 'C:\\Users\\saver\\PycharmProjects\\Community_smell\\globe.json'

# Apri il file JSON e carica i dati in una variabile
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

df_json = pd.DataFrame(json_data)

# Leggi un file Excel in un dataframe
df_dataset = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black.xlsx')

df_excel = df_json[["country", "A1","A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"]]


# Aggiungi una colonna vuota al dataframe df_dataset per i risultati
df_dataset['A1'] = "" #a
df_dataset['A2'] = ""#b
df_dataset['A3'] = "" #c
df_dataset['A4'] = ""#d
df_dataset['A5'] = ""#e
df_dataset['A6'] = ""#f
df_dataset['A7'] = "" #g
df_dataset['A8'] = ""#h
df_dataset['A9'] = ""


# Itera attraverso le righe di df_dataset, estrai i paesi e cerca i valori corrispondenti in df_excel (case-insensitive)
for index, row in df_dataset.iterrows():
    countries = row['countries'].split(',')  # Divide il campo "country" in una lista di paesi

    # Inizializza delle liste per accumulare i valori corrispondenti
    A1_values = []
    A2_values = []
    A3_values = []
    A4_values = []
    A5_values = []
    A6_values = []
    A7_values = []
    A8_values = []
    A9_values = []


    for country in countries:
        country_lower = country.strip().lower()

        match = df_excel[df_excel['country'].str.lower() == country_lower]

        if not match.empty:

            if not match.empty:
                A1_value = str(match['A1'].values[0])
                A2_value = str(match['A2'].values[0])
                A3_value = str(match['A3'].values[0])
                A4_value = str(match['A4'].values[0])
                A5_value = str(match['A5'].values[0])
                A6_value = str(match['A6'].values[0])
                A7_value = str(match['A7'].values[0])
                A8_value = str(match['A8'].values[0])
                A9_value = str(match['A9'].values[0])




                A1_values.append(A1_value)

                A2_values.append(A2_value)

                A3_values.append(A3_value)

                A4_values.append(A4_value)

                A5_values.append(A5_value)

                A6_values.append(A6_value)

                A7_values.append(A7_value)

                A8_values.append(A8_value)
                A9_values.append(A9_value)

            else:
                A1_value = 0
                A2_value = 0
                A3_value = 0
                A4_value = 0
                A5_value = 0
                A6_value = 0





    # Assegna le liste di valori alle colonne corrispondenti in df_dataset
    df_dataset.at[index, 'A1'] = ', '.join(A1_values)
    df_dataset.at[index, 'A2'] = ', '.join(A2_values)
    df_dataset.at[index, 'A3'] = ', '.join(A3_values)
    df_dataset.at[index, 'A4'] = ', '.join(A4_values)
    df_dataset.at[index, 'A5'] = ', '.join(A5_values)
    df_dataset.at[index, 'A6'] = ', '.join(A6_values)
    df_dataset.at[index, 'A7'] = ', '.join(A7_values)
    df_dataset.at[index, 'A8'] = ', '.join(A8_values)
    df_dataset.at[index, 'A9'] = ', '.join(A9_values)




# Funzione per calcolare la deviazione standard solo se la cella non è vuota
def calc_CV(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values)/np.mean(values) if values else np.nan

def calc_med(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.mean(values) if values else np.nan

def calc_devst(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values) if values else np.nan

# Calcola la deviazione standard
df_dataset['med_1'] = df_dataset.apply(lambda row: calc_med(row, 'A1'), axis=1)
df_dataset['devst_1'] = df_dataset.apply(lambda row: calc_devst(row, 'A1'), axis=1)
df_dataset['CV_1'] = df_dataset.apply(lambda row: calc_CV(row, 'A1'), axis=1)

df_dataset['med_2'] = df_dataset.apply(lambda row: calc_med(row, 'A2'), axis=1)
df_dataset['devst_2'] = df_dataset.apply(lambda row: calc_devst(row, 'A2'), axis=1)
df_dataset['CV_2'] = df_dataset.apply(lambda row: calc_CV(row, 'A2'), axis=1)

df_dataset['med_3'] = df_dataset.apply(lambda row: calc_med(row, 'A3'), axis=1)
df_dataset['devst_3'] = df_dataset.apply(lambda row: calc_devst(row, 'A3'), axis=1)
df_dataset['CV_3'] = df_dataset.apply(lambda row: calc_CV(row, 'A3'), axis=1)

df_dataset['med_4'] = df_dataset.apply(lambda row: calc_med(row, 'A4'), axis=1)
df_dataset['devst_4'] = df_dataset.apply(lambda row: calc_devst(row, 'A4'), axis=1)
df_dataset['CV_4'] = df_dataset.apply(lambda row: calc_CV(row, 'A4'), axis=1)

df_dataset['med_5'] = df_dataset.apply(lambda row: calc_med(row, 'A5'), axis=1)
df_dataset['devst_5'] = df_dataset.apply(lambda row: calc_devst(row, 'A5'), axis=1)
df_dataset['CV_5'] = df_dataset.apply(lambda row: calc_CV(row, 'A5'), axis=1)

df_dataset['med_6'] = df_dataset.apply(lambda row: calc_med(row, 'A6'), axis=1)
df_dataset['devst_6'] = df_dataset.apply(lambda row: calc_devst(row, 'A6'), axis=1)
df_dataset['CV_6'] = df_dataset.apply(lambda row: calc_CV(row, 'A6'), axis=1)

df_dataset['med_7'] = df_dataset.apply(lambda row: calc_med(row, 'A7'), axis=1)
df_dataset['devst_7'] = df_dataset.apply(lambda row: calc_devst(row, 'A7'), axis=1)
df_dataset['CV_7'] = df_dataset.apply(lambda row: calc_CV(row, 'A7'), axis=1)

df_dataset['med_8'] = df_dataset.apply(lambda row: calc_med(row, 'A8'), axis=1)
df_dataset['devst_8'] = df_dataset.apply(lambda row: calc_devst(row, 'A8'), axis=1)
df_dataset['CV_8'] = df_dataset.apply(lambda row: calc_CV(row, 'A8'), axis=1)

df_dataset['med_9'] = df_dataset.apply(lambda row: calc_med(row, 'A9'), axis=1)
df_dataset['devst_9'] = df_dataset.apply(lambda row: calc_devst(row, 'A9'), axis=1)
df_dataset['CV_9'] = df_dataset.apply(lambda row: calc_CV(row, 'A9'), axis=1)

df_dataset = df_dataset.dropna(subset=['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9', 'black'])
# Salva il dataframe aggiornato nel file Excel
df_dataset.to_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_globe.xlsx', index=False)
df_dataset.to_csv('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_globe.csv', index=False, sep=';')


# # # Calcola la deviazione standard per ciascuna riga e assegna i risultati alle colonne "dev_pdi", "dev_idv", ecc.
# df_dataset['dev_pdi'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['pdi'].split(', ')]), axis=1)
# df_dataset['dev_idv'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['idv'].split(', ')]), axis=1)
# df_dataset['dev_mas'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['mas'].split(', ')]), axis=1)
# df_dataset['dev_uai'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['uai'].split(', ')]), axis=1)
# df_dataset['dev_ltowvs'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['ltowvs'].split(', ')]), axis=1)
# df_dataset['dev_ivr'] = df_dataset.apply(lambda row: np.std([float(val) for val in row['ivr'].split(', ')]), axis=1)
# Calcola la deviazione standard solo se la cella non è vuota