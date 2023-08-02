from classes.trip import Trip


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

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
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return [*set([trip.visitor for trip in self.trips()])]

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        max_visitor = None
        max_visits = 0
        for v in self.visitors():
            v_visits = len([t for t in self.trips() if t.visitor == v])
            if v_visits > max_visits:
                max_visits = v_visits
                max_visitor = v
        return max_visitor

    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda p: p.total_visits())
