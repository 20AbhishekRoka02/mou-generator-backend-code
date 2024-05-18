from datetime import datetime
import pytz
import os
import shutil

def mediaSaver(logo):
    try:
        os.chdir("uploadedFiles")
        # path=f"{logo.filename}"
        logo_name_splitted=str(logo.filename).split(".")
        now_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d_%H-%M-%S-%f')
        path= "".join(logo_name_splitted[:-1:]) + now_time + "." + logo_name_splitted[-1]
        
        with open(path,"wb") as file:
            shutil.copyfileobj(logo.file, file)
        os.chdir("..")
        return path
    except Exception as e:
        return None
