#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    jim = Visitor('Jim')
    jam = Visitor('Jam')
    zion = NationalPark('Zion')
    yosemite = NationalPark('Yosemite')
    new_trip = Trip(jim, zion, '6', '9')
    new_trip2 = Trip(jam, yosemite, '5', '6')
    new_trip3 = Trip(jim, zion, '5', '6')
    new_trip4 = Trip(jim, yosemite, '5', '6')

    ipdb.set_trace()
