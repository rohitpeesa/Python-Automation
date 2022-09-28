import requests
import numpy as np
import pandas as pd

def Pdf_Downloader(pdf_url, pdf_name, http_headers):
    r = requests.get(pdf_url, headers=http_headers)
    # status code 200 signifies success
    if r.status_code == 200:
        # Directory to store files
        # wb indicates writing in binary, it has been used so that it won't change any info in the files
        with open(r"C:\Users\rohit\Downloads\Capstone Data Files\\" + pdf_name + ".pdf", 'wb') as f:
            f.write(r.content)
    else:
        print("We have the following error"+response.status_code)
# file and respective sheet name
Excel_sheet = pd.read_excel('Official Statement.xlsx',sheet_name="Hospitals")
http_headers = {
            "User-Agent": "Edg/91.0.864.59",
        } #I prefer edge so I have used edge agent you can use chrome ("Chrome/51.0.2704.103")

for i in range(0,len(Excel_sheet)):
    pdf_url=Excel_sheet['Link'][i] #links column in excel
    pdf_name=Excel_sheet['Issuer Name'][i] #Column to name the files based on who issued it
    try:
        Pdf_Downloader(pdf_url, pdf_name.replace('/',"_").replace('"',""), http_headers) 
        # replace has been used because file names in windows cannot contain / or "
    # If there was some issue with downloading file such as FileNot found errors would be raised below.
    except Exception as e:
        print(e)
