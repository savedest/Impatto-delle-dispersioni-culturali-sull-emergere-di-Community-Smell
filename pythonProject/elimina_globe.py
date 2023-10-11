import pandas as pd
import re

# Carica il file Excel
file_path = 'C:\\Users\\saver\\PycharmProjects\\pythonProject\\deviazione_standard_globe_second.xlsx'  # Sostituisci con il percorso del tuo file Excel
df = pd.read_excel(file_path)

# Funzione per verificare se ci sono almeno 2 numeri in una cella
def contiene_almeno_due_numeri(cell_value):
    numeri = re.findall(r'\d+\.\d+', cell_value)
    return len(numeri) >= 2

# Filtra il DataFrame
df_filtrato = df[df['Universalism/Particularism'].apply(lambda x: isinstance(x, str) and contiene_almeno_due_numeri(x))]

# Salva il risultato in un nuovo file Excel
output_file = 'file_filtrato_globe.xlsx'
df_filtrato.to_excel(output_file, index=False)

print(f'Righe filtrate salvate in {output_file}')
