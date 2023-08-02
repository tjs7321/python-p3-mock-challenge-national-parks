from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return [*set([trip.national_park for trip in self.trips()])]
