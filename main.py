import pandas as pd
import json

def main(myList):
    data = pd.read_csv(myList)
    return data

def toJSON(data):
    alteracao = data.to_dict('records')
    json_data = json.dumps(alteracao, indent=4)
    return json_data

def carregandoArq(json_data, DadosJson):
    with open(DadosJson, 'w') as f:
        f.write(json_data)

def etl_pipeline(entrada, saida):
    data = main(entrada)
    json_data = toJSON(data)
    carregandoArq(json_data, saida)

etl_pipeline('myList.csv', 'saidaDados.json')