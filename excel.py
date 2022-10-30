from email import header
import pandas as pd
import json

filename_json = 'data/' + 'test.json'
filename_excel = 'data/' + 'test.xlsx'

def appendJsonToExcel(filename_json,filename_excel,sheet_name):
    # Get data from .json file
    with open(filename_json) as json_file:
        data = json.load(json_file)

    # Json to Dataframe
    df = pd.json_normalize(data)

    # Append to Excel File:
    with pd.ExcelWriter(filename_excel,mode='a',if_sheet_exists='overlay',engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name,startrow=writer.sheets[sheet_name].max_row,header=None)

if __name__ == '__main__':
    appendJsonToExcel(filename_json,filename_excel,'testSheet')