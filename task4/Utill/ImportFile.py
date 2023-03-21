from ast import Constant
import traceback
import pandas as pd

def getData():
    try:
        data = []
        df = pd.read_excel('input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
        data = df.values.tolist()
        print("getData thanh cong")
        return data
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("getData that bai")
        return None
            
def importData(conn, data):
    try:
        with conn.cursor() as cursor:
            for row_data in data:
                cursor.execute(Constant.ADD_SQL, row_data)
                conn.commit()
        print("importData thanh cong")
    except:
        if conn is not None:
            conn.rollback()
            conn.close()
        traceback.print_exc()
        print("importData that bai")