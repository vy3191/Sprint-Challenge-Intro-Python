# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class for all the classes here
class Vehicle:
  pass

class FlightVehicle(Vehicle):
  pass

class Starship(FlightVehicle):
  pass

class Airplane(Starship):
  pass

class GroundVehicle(Vehicle):
  pass

class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass

#This file assignment is done. Did not write any unnecessary comments as it straight forward.