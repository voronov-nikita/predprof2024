# 
# Файл, содержащий основные надстройки проекта
# Запускает и подгружает основные компоненты всего приложения
# Импорт библиотек и их связь в единую схему
# 

from database import *
from logic import *


def main():
    createDatabase()

    for data in getAllData():
        data1 = data['date']
        data2 = data['flats_count']
        data3 = data['windows']
        data4 = data['windows_for_flat']
        
        addDataDate(data1['data'], data1['description'])
        addDataRooms(data2['data'], data2['description'])
        addDataWindows(data3['data'], data3['description'])
        addDataFloors(data4['data'], data4['description'])


# запустить только при исходном файле
if __name__=="__main__":
    main()
    
    print(getAallData())