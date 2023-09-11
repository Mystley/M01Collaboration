"""
This is a programm that takes user information about a vehicle type and display them back to the user using a super class
"Vehicle" called again in "Automobile" class.

Padley Perard
"""

# Class definitions
class Vehicle:
    valid_types = ["car", "truck", "plane", "boat", "broomstick"]
    vehicle_type = input("Vehicle type: ")

    while vehicle_type not in valid_types:                 # Making sure the user type the right type of vehicle
        vehicle_type = input("Please enter a valid Vehicle type (car, truck, plane, boat, broomstick): ")

class Automobile(Vehicle):
    year = int(input("Vehicle year: "))
    make = input("Vehicle make: ")
    model = input("Vehicle model: ")

    doors = int(input("Vehicle doors (2 or 4): "))
    while doors != 2:                                      # Making sure the user type the right numbers
        if doors == 4:
            break
        else:
            doors = int(input("Only '2' or '4' is accepted\n Vehicle doors: "))
    
    roof = input("Vehicle roof ('solid' or 'sun roof'): ")
    while roof != "solid":                                 # Making sure the user type the right type of roof
        if roof == "sun roof":
            break
        else:
            print("Only 'solid' or 'sun roof' is accepted in all lowercase")
            roof = input("Vehicle roof ('solid' or 'sun roof'): ")
    

    

# Instances
vehicle_type_entry = Automobile.vehicle_type
year_entry = Automobile.year
make_entry = Automobile.make
model_entry = Automobile.model
doors_entry = Automobile.doors
roof_entry = Automobile.roof

# Output
print("\n")
print(f'Vehicle type:{vehicle_type_entry.rjust(13)}')
print(f'Year:{year_entry:>21}')
print(f'Make:{make_entry.rjust(21)}')
print(f'Model:{model_entry.rjust(20)}')
print(f'Doors:{doors_entry:>20}')
print(f'Roof:{roof_entry.rjust(21)}')