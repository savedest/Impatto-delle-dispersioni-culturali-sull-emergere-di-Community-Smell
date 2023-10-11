import pandas as pd
import re

# Carica il file Excel
file_path = 'C:\\Users\\saver\\PycharmProjects\\pythonProject\\hofstede\\deviazione_standard_hofstede_final_second.xlsx'  # Sostituisci con il percorso del tuo file Excel
df = pd.read_excel(file_path)

# Funzione per verificare se ci sono almeno 2 numeri interi nel formato "x, y" in una cella
def contiene_almeno_due_numeri_interi(cell_value):
    numeri_interi = re.findall(r'\d+', cell_value)
    return len(numeri_interi) >= 2

# Filtra il DataFrame
df_filtrato = df[df['pdi'].apply(lambda x: isinstance(x, str) and contiene_almeno_due_numeri_interi(x))]

# Salva il risultato in un nuovo file Excel
output_file = 'file_filtrato_hofstede.xlsx'
df_filtrato.to_excel(output_file, index=False)

print(f'Righe filtrate salvate in {output_file}')
