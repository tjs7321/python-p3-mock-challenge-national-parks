from classes.trip import Trip


class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    def __repr__(self):
        return f'NationalPark:{{"{self._name}"}}'

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))

    def total_visits(self):
        return len([v.visitor for v in Trip.all if v.national_park == self])

    def best_visitor(self):
        from classes.visitor import Visitor
        best_visitor = Visitor.all[0]
        for visitor in Visitor.all:
            if len(visitor.total_trips_to(self)) > len(best_visitor.total_trips_to(self)):
                best_visitor = visitor
        return best_visitor

    @classmethod
    def most_visited(cls):
        most_visited = cls.all[0]
        for park in cls.all:
            if park.total_visits() > most_visited.total_visits():
                most_visited = park
        return most_visited

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception('Cannot reassign name.')
        elif isinstance(name, str):
            self._name = name
        else: raise Exception('Name must be a string.')
