from Repositories.VehicleRepository import VehicleRepository
from Entities.Vehicle import Vehicle
import datetime


def main():
    print('Main')

    vehicle = Vehicle()
    vehicle.vin = 'Firetruck'
    vehicle.created = datetime.datetime.now()

    print(f'{vehicle.vin} - {vehicle.created}')

    repo = VehicleRepository()
    repo.addVehicle(vehicle)


if __name__ == "__main__":
    main()
