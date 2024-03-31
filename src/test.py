# 
# Unit тесты
# Тестирование компонентов и функций отдельного выделенных в backend и frontend части
# К примеру тестирование на ошибки БД и статус коды для REST API запросов
# 

from colorama import init, Fore


from database import *
from logic import *


def test(func, data, result):
    try:
        if type(func(*data)) == result:
            return Fore.GREEN + 'THE TEST IS PASSED!'
        else:
            return Fore.RED + 'THE TEST IS FAILED'
    except:
        return Fore.GREEN + 'THE TEST IS PASSED!'


print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(getData, (), dict))
print(test(addDataWindows, ([1], "wnciwnv"), str))
print(test(addDataWindows, (["svdnwv"], "sfwef"), str))
print(test(addDataWindows, ([], "wncwdvweveiwnv"), str))
print(test(addDataWindows, ([1, 2, "svjowdo", 3], "rewverv"), str))
print(test(addDataWindows, ([1, 2, "wnovew", 3], "wnciwnv"), str))
print(test(addDataWindows, ([1, 2, 3, "wonewo"], "12434"), str))
print(test(addDataWindows, ([1, 2, 3, "wjndcvw"], "dvewrv r"), str))
print(test(addDataWindows, ([1, 2, 3, 2032], "wcwev"), str))
print(test(addDataWindows, ([1, 2, 36, 4, 2], "rwvrwvvfve"), str))
print(test(addDataWindows, ([1, 2, 3, 3, 3], "1343tbrb"), str))
print(test(addDataWindows, ([1, 22, 3], "2efwevr"), str))
print(test(addDataWindows, ([1, 4, 3], "wdvwrv"), str))
print(test(addDataWindows, ([1, 2, 3, 4], "wdvwrv"), str))

