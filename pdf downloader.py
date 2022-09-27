import requests
import numpy as np
import pandas as pd

def download_pdf(url, file_name, headers):
    # Send GET request
    r = requests.get(url, headers=headers)
    # Save the PDF
    if r.status_code == 200:
        with open(r"C:\Users\rohit\Downloads\Data\\" + file_name + ".pdf", 'wb') as f:
            f.write(r.content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    df = pd.read_excel('assignment.xlsx',sheet_name="Rating")
    row_count = len(df)
    headers = {
            "User-Agent": "Chrome/51.0.2704.103",
        }
    for i in range(0,row_count):
        url=df['Rating Links'][i] #links column in excel
        file_name=df['Rating Issuer'][i] #Column to name the files based on who issued the ratings
        try:
            download_pdf(url, file_name.replace('/',"_").replace('"',""), headers)
        except Exception as e:
            print(e)
