from app import models, db
from app.models import RegistrationDetail


class RegistrationRepo:

    def register_details(self, detail_dto):
        detail = models.RegistrationDetail(detail_dto.phone_number, detail_dto.start_location,
                                           detail_dto.start_time,
                                           detail_dto.drop_location, detail_dto.car_model, detail_dto.car_number,
                                           detail_dto.seats, detail_dto.car_type)
        db.session.add(detail)
        db.session.commit()
        print("services commit")
        return
