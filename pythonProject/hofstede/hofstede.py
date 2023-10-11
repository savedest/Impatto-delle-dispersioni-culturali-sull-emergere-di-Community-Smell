import json
import pandas as pd
import numpy as np

# Specifica il percorso del tuo file JSON
file_path = 'C:\\Users\\saver\\PycharmProjects\\pythonProject\\hofstede\\hofstede.json'

# Apri il file JSON e carica i dati in una variabile
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

df_json = pd.DataFrame(json_data)

# Leggi un file Excel in un dataframe
df_dataset = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\pythonProject\\0-25.xlsx')

df_excel = df_json[["country", "pdi", "idv", "mas", "uai", "ltowvs", "ivr"]]


# Aggiungi una colonna vuota al dataframe df_dataset per i risultati
df_dataset['pdi'] = ""
df_dataset['idv'] = ""
df_dataset['mas'] = ""
df_dataset['uai'] = ""
df_dataset['ltowvs'] = ""
df_dataset['ivr'] = ""

# Itera attraverso le righe di df_dataset, estrai i paesi e cerca i valori corrispondenti in df_excel (case-insensitive)
for index, row in df_dataset.iterrows():
    countries = row['countries'].split(',')  # Divide il campo "country" in una lista di paesi

    # Inizializza delle liste per accumulare i valori corrispondenti
    pdi_values = []
    idv_values = []
    mas_values = []
    uai_values = []
    ltowvs_values = []
    ivr_values = []

    for country in countries:
        country_lower = country.strip().lower()

        match = df_excel[df_excel['country'].str.lower() == country_lower]

        if not match.empty:


            if not match.empty:
                pdi_value = str(match['pdi'].values[0])
                idv_value = str(match['idv'].values[0])
                mas_value = str(match['mas'].values[0])
                uai_value = str(match['uai'].values[0])
                ltowvs_value = str(match['ltowvs'].values[0])
                ivr_value = str(match['ivr'].values[0])

                if pdi_value != "#NULL!":
                    pdi_values.append(pdi_value)
                if idv_value != "#NULL!":
                    idv_values.append(idv_value)
                if mas_value != "#NULL!":
                    mas_values.append(mas_value)
                if uai_value != "#NULL!":
                    uai_values.append(uai_value)
                if ltowvs_value != "#NULL!":
                    ltowvs_values.append(ltowvs_value)
                if ivr_value != "#NULL!":
                    ivr_values.append(ivr_value)
            # else:
                # pdi_value = 0
                # idv_value = 0
                # mas_value = 0
                # uai_value = 0
                # ltowvs_value = 0
                # ivr_value = 0


    # Assegna le liste di valori alle colonne corrispondenti in df_dataset
    df_dataset.at[index, 'pdi'] = ', '.join(pdi_values)
    df_dataset.at[index, 'idv'] = ', '.join(idv_values)
    df_dataset.at[index, 'mas'] = ', '.join(mas_values)
    df_dataset.at[index, 'uai'] = ', '.join(uai_values)
    df_dataset.at[index, 'ltowvs'] = ', '.join(ltowvs_values)
    df_dataset.at[index, 'ivr'] = ', '.join(ivr_values)



# Funzione per calcolare la deviazione standard solo se la cella non è vuota
def calc_std(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values) if values else np.nan

def calc_CV(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values) / np.mean(values) if values else np.nan

def calc_med(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.mean(values) if values else np.nan

# Calcola la deviazione standard
df_dataset['med_pdi'] = df_dataset.apply(lambda row: calc_med(row, 'pdi'), axis=1)
df_dataset['dev_pdi'] = df_dataset.apply(lambda row: calc_std(row, 'pdi'), axis=1)
df_dataset['CV_pdi'] = df_dataset.apply(lambda row: calc_CV(row, 'pdi'), axis=1)

df_dataset['med_idv'] = df_dataset.apply(lambda row: calc_med(row, 'idv'), axis=1)
df_dataset['dev_idv'] = df_dataset.apply(lambda row: calc_std(row, 'idv'), axis=1)
df_dataset['CV_idv'] = df_dataset.apply(lambda row: calc_CV(row, 'idv'), axis=1)

df_dataset['med_mas'] = df_dataset.apply(lambda row: calc_med(row, 'mas'), axis=1)
df_dataset['dev_mas'] = df_dataset.apply(lambda row: calc_std(row, 'mas'), axis=1)
df_dataset['CV_mas'] = df_dataset.apply(lambda row: calc_CV(row, 'mas'), axis=1)

df_dataset['med_uai'] = df_dataset.apply(lambda row: calc_med(row, 'uai'), axis=1)
df_dataset['dev_uai'] = df_dataset.apply(lambda row: calc_std(row, 'uai'), axis=1)
df_dataset['CV_uai'] = df_dataset.apply(lambda row: calc_CV(row, 'uai'), axis=1)

df_dataset['med_ltowvs'] = df_dataset.apply(lambda row: calc_med(row, 'ltowvs'), axis=1)
df_dataset['dev_ltowvs'] = df_dataset.apply(lambda row: calc_std(row, 'ltowvs'), axis=1)
df_dataset['CV_ltowvs'] = df_dataset.apply(lambda row: calc_CV(row, 'ltowvs'), axis=1)

df_dataset['med_ivr'] = df_dataset.apply(lambda row: calc_med(row, 'ivr'), axis=1)
df_dataset['dev_ivr'] = df_dataset.apply(lambda row: calc_std(row, 'ivr'), axis=1)
df_dataset['CV_ivr'] = df_dataset.apply(lambda row: calc_CV(row, 'ivr'), axis=1)


# Salva il dataframe aggiornato nel file Excel
df_dataset.to_excel('deviazione_standard_hofstede_final_second.xlsx', index=False)

