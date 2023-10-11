import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Carica il tuo dataframe
df = pd.read_excel('C:\\Users\\saver\\PycharmProjects\\Community_smell\\black_cloud\\black_cloud_metrics_globe.xlsx')  # Sostituisci con il tuo file CSV o Excel

# Specifica la variabile dipendente e indipendenti
variabile_dipendente = 'black'
variabili_indipendenti = ['CV_1', 'CV_2', 'CV_3', 'CV_4', 'CV_5', 'CV_6', 'CV_7', 'CV_8', 'CV_9']

# Esegui un'analisi ANOVA per ciascuna variabile indipendente
for variabile_independente in variabili_indipendenti:
    formula = f'{variabile_dipendente} ~ {variabile_independente}'
    model = ols(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(f"Analisi ANOVA per {variabile_independente}:")
    print(anova_table)
