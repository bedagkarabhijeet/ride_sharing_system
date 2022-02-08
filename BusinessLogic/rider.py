

class Rider:
    def __init__(self, rider_data_access):
        self._rider_data_access = rider_data_access

    def add_rider(self, rider_data):
        new_rider = self._rider_data_access.add(rider_data)
        return new_rider
