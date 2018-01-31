from app import models, db
from app.models import services


class databaseRespository:

    def create_service_database(self, database_dto):
        service = models.services(database_dto.phone_number, database_dto.start_location, database_dto.start_time,
                                  database_dto.drop_location, database_dto.car_model, database_dto.car_number,
                                  database_dto.seats, database_dto.type)
        db.session.add(service)
        db.session.commit()
        print("services commit")
