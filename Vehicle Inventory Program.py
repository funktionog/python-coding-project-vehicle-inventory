#Vehicle Inventory Program; Create automobile class; attributes .make, .model, .color, .year, .mileage
#methods included: constructor, add a new vehicle, remove vehicle, update vehicle attributres
#output to text file
class Automobile:

    def __init__(self):
        self.make = " "
        self.model = " "
        self.color = " "
        self.year = 0
        self.mileage = 0


    def add_vehicle(self):
        self.year = int(input("Vehicle Year: "))
        self.make = input("Vehicle Make: ")
        self.model = input("Vehicle Model: ")
        self.color = input("Vehicle Color: ")
        self.mileage = int(input("Vehicle Mileage: "))

    def __str__(self):
        return('%d %s %s Color: %s Mileage: %d' %
              (self.year, self.make, self.model, self. color,
               self.mileage))

vehicle_list = []

def edit(vehicle_list):
    pos = int(input('Enter the position of the vehicle to edit: '))
    new_vehicle = car.add_vehicle()
    new_vehicle = car.__str__()
    vehicle_list[pos-1] = new_vehicle
    print('Vehicle Updated')

user=True
while user:
    print ("""
    1.Add Vehicle
    2.Delete Vehicle
    3.View Inventory
    4.Update Inventory
    5.Export To Text File
    6.Exit Program
    """)
    answer=input("What would you like to do? ")
    if answer=="1":
        car = Automobile()
        car.add_vehicle()
        vehicle_list.append(car.__str__())


    elif answer=="2":
        for i in vehicle_list:
            vehicle_list.pop(int(input('\nEnter position of vehicle to remove: ')))
            print('Vehicle Removed.')
    elif answer=="3":
        print(vehicle_list)
    elif answer=="4":
        edit(vehicle_list)
    elif answer=='5':
        f = open('inventory.txt', 'w')
        f.write(str(vehicle_list))
        f.close()
    elif answer=='6':
        print('Goodbye.')
        quit()
