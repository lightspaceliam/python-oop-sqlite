import sqlite3
from ._abstract.BaseRepository import BaseRepository
from Entities.Vehicle import Vehicle


class VehicleRepository(BaseRepository):

    def addVehicle(self, vehicle):

        cursor = self.getConn()
        cursor.execute(
            '''
                CREATE TABLE 
                IF NOT EXISTS 
                Vehicles (
                    id INTEGER PRIMARY KEY
                    , vin TEXT NOT NULL
                    , created TEXT NOT NULL
                );
            '''
        )
        print('{0},{1}'.format(vehicle.vin, vehicle.created))

        insertStatment = 'INSERT INTO Vehicles (vin, created) VALUES (?,?)'

        cursor.execute(insertStatment, (vehicle.vin, vehicle.created))

        self.close()
