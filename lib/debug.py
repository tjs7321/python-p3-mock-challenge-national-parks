#!/usr/bin/env python3
import ipdb
from classes.national_park import NationalPark
from classes.trip import Trip
from classes.visitor import Visitor

if __name__ == "__main__":
    p1 = NationalPark("Yosemmette")
    p2 = NationalPark("Rocky Mountain")
    vis = Visitor("Tom")
    t_1 = Trip(vis, p1, "May 5th", "May 9th")
    t_2 = Trip(vis, p1, "January 5th", "January 20th")
    t_3 = Trip(vis, p2, "January 5th", "January 20th")
    t_4 = Trip(vis, p2, "Feb 12th", "Feb 18th")
    t_5 = Trip(vis, p1, "April 9th", "April 14th")

    ipdb.set_trace()
