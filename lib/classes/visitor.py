from classes.trip import Trip


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    def __repr__(self):
        return f'Visitor:{{"{self._name}"}}'

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))

    def total_trips_to(self, national_park):
        return [trip for trip in Trip.all if trip.visitor == self and trip.national_park == national_park]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else: raise Exception("Name must be string between 1 and 15 characters.")
