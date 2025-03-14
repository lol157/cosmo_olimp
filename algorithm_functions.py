
def solve_algorithm(api_data):
    return {
        'main_page': {'days': int, 'credits': int},
        'path_points_info': {
            'точка_маршрута_1':  {'fuel': int, 'o2': int},
            'точка_маршрута_2': {'fuel': int, 'o2': int},
            'точка_маршрута_3': {'fuel': int, 'o2': int}
        },
        'days_info': {
            'день_1': {'fuel': int, 'o2': int, 'power_for_engine': int, 'power_for_electricity': int, 'T': int, 'sh': int},
            'день_2': {'fuel': int, 'o2': int, 'power_for_engine': int, 'power_for_electricity': int, 'T': int, 'sh': int}
        }
    }


if __name__ == '__main__':
    data = [[1, 8], [6, 8], [7, 24], [3, 8], [7, 56], [5, 24]]
    print(solve_algorithm(data))
