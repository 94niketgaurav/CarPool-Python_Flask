from app import models, db

class AuthRespository:

    def get_user(self, user_dto):
        user = models.Users.query.filter_by(email=user_dto.email).first()
        if user is not None:
            return user

    def create_user(self, user_dto):

        user = models.Users(user_dto.name, user_dto.email, user_dto.password)
        db.session.add(user)
        db.session.commit()
