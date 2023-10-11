import json
import pandas as pd
import numpy as np

# Specifica il percorso del tuo file JSON
file_path = 'C:\\Users\\saver\\PycharmProjects\\Community_smell\\trompenaars.json'

# Apri il file JSON e carica i dati in una variabile
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

df_json = pd.DataFrame(json_data)

# Leggi un file Excel in un dataframe
df_dataset = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\radio_silence\\radio.xlsx')

df_excel = df_json[["country", "Universalism/Particularism", "Individualism/Communitarianism", "Specific/Diffuse", "Neutral/Affective", "Achievement/Ascription", "Past,Present,Future", "Sequential/Synchronic", "Internal/External"]]


# Aggiungi una colonna vuota al dataframe df_dataset per i risultati
df_dataset['Universalism/Particularism'] = "" #a
df_dataset['Individualism/Communitarianism'] = ""#b
df_dataset['Specific/Diffuse'] = "" #c
df_dataset['Neutral/Affective'] = ""#d
df_dataset['Achievement/Ascription'] = ""#e
df_dataset['Past,Present,Future'] = ""#f
df_dataset['Sequential/Synchronic'] = "" #g
df_dataset['Internal/External'] = ""#h

# Itera attraverso le righe di df_dataset, estrai i paesi e cerca i valori corrispondenti in df_excel (case-insensitive)
for index, row in df_dataset.iterrows():
    countries = row['countries'].split(',')  # Divide il campo "country" in una lista di paesi

    # Inizializza delle liste per accumulare i valori corrispondenti
    a_values = []
    b_values = []
    c_values = []
    d_values = []
    e_values = []
    f_values = []
    g_values = []
    h_values = []

    for country in countries:
        country_lower = country.strip().lower()

        match = df_excel[df_excel['country'].str.lower() == country_lower]

        if not match.empty:

            if not match.empty:
                a_value = str(match['Universalism/Particularism'].values[0])
                b_value = str(match['Individualism/Communitarianism'].values[0])
                c_value = str(match['Specific/Diffuse'].values[0])
                d_value = str(match['Neutral/Affective'].values[0])
                e_value = str(match['Achievement/Ascription'].values[0])
                f_value = str(match['Past,Present,Future'].values[0])
                g_value = str(match['Sequential/Synchronic'].values[0])
                h_value = str(match['Internal/External'].values[0])

                if a_value != "#NULL!":
                    a_values.append(a_value)
                if b_value != "#NULL!":
                    b_values.append(b_value)
                if c_value != "#NULL!":
                    c_values.append(c_value)
                if d_value != "#NULL!":
                    d_values.append(d_value)
                if e_value != "#NULL!":
                    e_values.append(e_value)
                if f_value != "#NULL!":
                    f_values.append(f_value)
                if e_value != "#NULL!":
                    g_values.append(g_value)
                if f_value != "#NULL!":
                    h_values.append(h_value)
            else:
                a_value = 0
                b_value = 0
                c_value = 0
                d_value = 0
                e_value = 0
                f_value = 0





    # Assegna le liste di valori alle colonne corrispondenti in df_dataset
    df_dataset.at[index, 'Universalism/Particularism'] = ', '.join(a_values)
    df_dataset.at[index, 'Individualism/Communitarianism'] = ', '.join(b_values)
    df_dataset.at[index, 'Specific/Diffuse'] = ', '.join(c_values)
    df_dataset.at[index, 'Neutral/Affective'] = ', '.join(d_values)
    df_dataset.at[index, 'Achievement/Ascription'] = ', '.join(e_values)
    df_dataset.at[index, 'Past,Present,Future'] = ', '.join(f_values)
    df_dataset.at[index, 'Sequential/Synchronic'] = ', '.join(g_values)
    df_dataset.at[index, 'Internal/External'] = ', '.join(h_values)



# Funzione per calcolare la deviazione standard solo se la cella non è vuota
def calc_std(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values) if values else np.nan

def calc_CV(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.std(values)/np.mean(values) if values else np.nan

def calc_med(row, column_name):
    values = [float(val) for val in row[column_name].split(', ') if val.strip() != '']
    return np.mean(values) if values else np.nan

# Calcola la deviazione standard
df_dataset['med_UP'] = df_dataset.apply(lambda row: calc_med(row, 'Universalism/Particularism'), axis=1)
df_dataset['dev_UP'] = df_dataset.apply(lambda row: calc_std(row, 'Universalism/Particularism'), axis=1)
df_dataset['CV_1'] = df_dataset.apply(lambda row: calc_CV(row, 'Universalism/Particularism'), axis=1)

df_dataset['med_IC'] = df_dataset.apply(lambda row: calc_med(row, 'Individualism/Communitarianism'), axis=1)
df_dataset['dev_IC'] = df_dataset.apply(lambda row: calc_std(row, 'Individualism/Communitarianism'), axis=1)
df_dataset['CV_2'] = df_dataset.apply(lambda row: calc_CV(row, 'Individualism/Communitarianism'), axis=1)

df_dataset['med_Sp'] = df_dataset.apply(lambda row: calc_med(row, 'Specific/Diffuse'), axis=1)
df_dataset['dev_Sp'] = df_dataset.apply(lambda row: calc_std(row, 'Specific/Diffuse'), axis=1)
df_dataset['CV_3'] = df_dataset.apply(lambda row: calc_CV(row, 'Specific/Diffuse'), axis=1)

df_dataset['med_NA'] = df_dataset.apply(lambda row: calc_med(row, 'Neutral/Affective'), axis=1)
df_dataset['dev_NA'] = df_dataset.apply(lambda row: calc_std(row, 'Neutral/Affective'), axis=1)
df_dataset['CV_4'] = df_dataset.apply(lambda row: calc_CV(row, 'Neutral/Affective'), axis=1)

df_dataset['med_AA'] = df_dataset.apply(lambda row: calc_med(row, 'Achievement/Ascription'), axis=1)
df_dataset['dev_AA'] = df_dataset.apply(lambda row: calc_std(row, 'Achievement/Ascription'), axis=1)
df_dataset['CV_5'] = df_dataset.apply(lambda row: calc_CV(row, 'Achievement/Ascription'), axis=1)

df_dataset['med_PPF'] = df_dataset.apply(lambda row: calc_med(row, 'Past,Present,Future'), axis=1)
df_dataset['dev_PPF'] = df_dataset.apply(lambda row: calc_std(row, 'Past,Present,Future'), axis=1)
df_dataset['CV_6'] = df_dataset.apply(lambda row: calc_CV(row, 'Past,Present,Future'), axis=1)

df_dataset['med_SS'] = df_dataset.apply(lambda row: calc_med(row, 'Sequential/Synchronic'), axis=1)
df_dataset['dev_SS'] = df_dataset.apply(lambda row: calc_std(row, 'Sequential/Synchronic'), axis=1)
df_dataset['CV_7'] = df_dataset.apply(lambda row: calc_CV(row, 'Sequential/Synchronic'), axis=1)

df_dataset['med_IE'] = df_dataset.apply(lambda row: calc_med(row, 'Internal/External'), axis=1)
df_dataset['dev_IE'] = df_dataset.apply(lambda row: calc_std(row, 'Internal/External'), axis=1)
df_dataset['CV_8'] = df_dataset.apply(lambda row: calc_CV(row, 'Internal/External'), axis=1)

df_dataset = df_dataset.dropna(subset=['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'radio'])

# Salva il dataframe aggiornato nel file Excel
df_dataset.to_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\radio_silence\\radio_silence_metrics_trompenaars.xlsx', index=False)
df_dataset.to_csv('C:\\Users\\saver\\PycharmProjects\\Community_smell\\radio_silence\\radio_silence_metrics_trompenaars.csv', index=False, sep=';')

