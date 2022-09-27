import requests
import numpy as np
import pandas as pd

def Pdf_Downloader(pdf_url, pdf_name, http_headers):
    r = requests.get(pdf_url, headers=http_headers)
    if r.status_code == 200:
        with open(r"C:\Users\rohit\Downloads\Capstone Data Files\\" + pdf_name + ".pdf", 'wb') as f:
            f.write(r.content)
    else:
        print("We have the following error"+response.status_code)

if __name__ == "__main__":
    Excel_sheet = pd.read_excel('Official Statements.xlsx',sheet_name="Hospitals")
    n_rows = len(df)
    http_headers = {
            "User-Agent": "Edg/91.0.864.59",
        }
    for i in range(0,n_rows):
        pdf_url=df['Rating Links'][i] #links column in excel
        pdf_name=df['Rating Issuer'][i] #Column to name the files based on who issued the ratings
        try:
            Pdf_Downloader(pdf_url, pdf_name.replace('/',"_").replace('"',""), http_headers)
        except Exception as e:
            print(e)
