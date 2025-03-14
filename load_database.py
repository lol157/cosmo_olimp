from requests_api import RequestsCollector
from database_manager import DatabaseManager
from algorithm_functions import solve_algorithm


if __name__ == '__main__':
    rc = RequestsCollector()

    with DatabaseManager() as db:
        db.create_database()

        api_data = rc.get_path()

        db.add_data(api_data)
