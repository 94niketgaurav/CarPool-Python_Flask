from app import models, db


class travellerRespository:

    def create_user(self, traveller_dto):
        user = models.traveller_direct(traveller_dto.name, traveller_dto.email, traveller_dto.phone,
                                       traveller_dto.start_time)
        db.session.add(user)
        db.session.commit()
