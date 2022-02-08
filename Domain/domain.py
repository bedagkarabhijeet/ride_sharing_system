from enum import Enum


class Human:
    def __init__(self, name, id_of_person):
        self._name = name
        self._id = id_of_person


class DriverStatus(Enum):
    FREE, DRIVING, TAKING_A_BREAK = 0, 1, 2


class RideRequest:
    def __init__(self):
        self.origin = None
        self.destination = None
        self.no_of_seats = None


class RideStatuses(Enum):
    WAITING, IN_PROGRESS, WITHDRAWN, CANCELLED, COMPLETED = 0, 1, 2, 3, 4


class Ride:
    def __init__(self, ride_status, ride_data):
        self.ride_status = ride_status
        self.ride_data = ride_data
