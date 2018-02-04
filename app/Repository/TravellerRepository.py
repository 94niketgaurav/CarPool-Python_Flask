from app import models, db


class TravellerRespository:

    def create_traveller(self, travellerdto):
        user = models.TravellerDirect(travellerdto.name, travellerdto.email, travellerdto.phone,
                                      travellerdto.start_time)
        db.session.add(user)
        db.session.commit()
