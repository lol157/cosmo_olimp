from colorama import Fore
from database_manager import DatabaseManager
from requests_api import RequestsCollector
from algorithm_functions import solve_algorithm


def test(func, data_type, *args):
    try:
        if isinstance(func(*args), data_type):
            print(f'{Fore.GREEN} TEST COMPLETED SUCCESSFULLY')
        else:
            print(f'{Fore.RED} TEST FAILED')
    except:
        print(f'{Fore.RED} TEST FAILED')


rc = RequestsCollector()

test(rc.get_path, list)
test(solve_algorithm, dict, [[3, 8], [6, 8], [7, 24], [3, 8], [7, 56], [5, 24]])
test(solve_algorithm, dict, [[2, 8], [2, 8], [4, 56], [7, 24]])
test(solve_algorithm, dict, [[4, 8], [6, 8], [3, 24], [5, 56], [3, 24]])
test(solve_algorithm, dict, [[5, 8], [3, 56], [7, 24]])

