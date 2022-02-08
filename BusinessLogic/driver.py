

class Driver:
    def __init__(self, driver_data_access):
        self._driver_data_access = driver_data_access

    def add_driver(self, driver_data):
        new_driver = self._driver_data_access.add(driver_data)
        return new_driver
