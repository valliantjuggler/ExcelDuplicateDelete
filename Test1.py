import os
import shutil
import pandas as pd
from datetime import datetime
import time
today = datetime.today().strftime('%Y%m%d')
file_name = 'Test_'+today+'.xlsx'
path = 'C:\\Users\\ajayd\\Desktop\\Python\\'+file_name
dest = 'C:\\Users\\ajayd\\Desktop\\Python\\Destination\\'
if os.path.exists(path):
    data = pd.read_excel(path)
    d = data.drop_duplicates(subset=["Coloumn1", "Coloumn2"], keep="first")
    f = "Output_" + (time.strftime("%Y%m%d") + ".xlsx")
    d1 = d.to_excel(f, index=False)
    shutil.move(f,dest)
else:
    print("file not found")

