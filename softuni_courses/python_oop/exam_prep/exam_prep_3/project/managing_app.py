from typing import List

from project2.route import Route
from project2.user import User
from project2.vehicles.base_vehicle import BaseVehicle
from project2.vehicles.cargo_van import CargoVan
from project2.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name, last_name, driving_license_number):
        for i in self.users:
            if i.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in ('PassengerCar', 'CargoVan'):
            return f"Vehicle type {vehicle_type} is inaccessible."

        for i in self.vehicles:
            if i.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == 'PassengerCar':
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))
        else:
            self.vehicles.append(CargoVan(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        for i in self.routes:
            if i.start_point == start_point and i.end_point == end_point and i.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif i.start_point == start_point and i.end_point == end_point and i.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif i.start_point == start_point and i.end_point == end_point and i.length > length:
                i.is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):
        user = [i for i in self.users if i.driving_license_number == driving_license_number][0]
        vehicle = [i for i in self.vehicles if i.license_plate_number == license_plate_number][0]
        route = [i for i in self.routes if i.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count):
        result = sorted([i for i in self.vehicles if i.is_damaged], key=lambda x: (x.brand, x.model))

        for i in range(min(count, len(result))):
            result[i].is_damaged = False
            result[i].recharge()

        return f"{min(count, len(result))} vehicles were successfully repaired!"

    def users_report(self):
        result = ['*** E-Drive-Rent ***']

        for i in sorted(self.users, key=lambda x: x.rating, reverse=True):
            result.append(str(i))

        return '\n'.join(result)


app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
