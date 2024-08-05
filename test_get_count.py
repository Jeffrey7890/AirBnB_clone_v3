#!/usr/bin/python3
from models import storage
from models.state import State
from models.amenity import Amenity


first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
print(storage.count(Amenity))
