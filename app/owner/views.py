from flask import Blueprint, request, render_template, g, redirect, url_for
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required

from app import app
from app.owner.RegistrationDto import RegistrationDto
from app.Repository.RegistrationRepo import RegistrationRepo
from app.models import Users, RegistrationDetail
from app.owner.AuthService import AuthService, InvalidUserException, UserExistsException
from app.owner.UserDto import UserDto
from app.owner.forms import SignupForm, RegistrationDetails, Login

own = Blueprint('owner', __name__, url_prefix='/owner')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
form = ""


@app.before_request
def before_request():
    g.user = current_user


@own.route('/')
def owner_home():
    return render_template("owner.html")


@own.route('/signup', methods=['GET'])
def signup():
    """
    For Signup of new users
    :return:
    """
    global form
    form = SignupForm(request.form)
    if request.method == 'GET':
        print("IN GEt call")
        return render_template("owner_signup.html", form=form)


@own.route('/signup', methods=['POST'])
def post_signup():
    """
    Post Signup
    :return:
    """
    auth_service = AuthService()
    form = SignupForm(request.form)

    if form.validate_on_submit() is True:
        print("In validated section")
        user_dto = UserDto(form.email.data, form.password.data, form.name.data)

        try:
            auth_service.create_user(user_dto)
            return redirect(url_for('owner.registration_service'))
        except UserExistsException:
            return render_template("owner_signup.html", form=form)


@own.route('/registration', methods=['GET'])
def registration_service():
    global form
    form = RegistrationDetails(request.form)

    if request.method == 'GET':
        print("IN Get call")
        return render_template("services.html", form=form)


@own.route('/registration', methods=['POST'])
def post_registration_service():
    """
    For Car Details with Owner Further Details
    :return:
    """
    registration_repo = RegistrationRepo()

    form = RegistrationDetails(request.form)

    if form.validate_on_submit() is True:
        print("in validation")
        details_dto = RegistrationDto(
            form.phone_number.data, form.start_location.data, form.start_time.data, form.drop_location.data,
            form.car_model.data, form.car_number.data, form.seats.data, form.car_type.data)
        registration_repo.register_details(details_dto)
        return redirect(url_for('owner.login'))



@login_manager.user_loader
def load_user(id):
    return Users.query.get(str(id))


@own.route('/login', methods=['GET'])
def login():
    """
    Login Manager And Car Details
    :return:
    """
    global form
    form = Login(request.form)

    if request.method == 'GET':
        return render_template('owner_login.html', form=form)


@own.route('/login', methods=['POST'])
def post_login():
    auth_service = AuthService()
    global form
    form = Login(request.form)
    if request.method == 'POST':
        user_dto = UserDto(form.email.data, form.password.data)
        try:
            registered_user = auth_service.load_user(user_dto)
            login_user(registered_user)
            return redirect(request.args.get('next') or url_for('owner.details'))
        except InvalidUserException:
            return redirect(url_for('owner.login'))


@own.route('/details', methods=['GET'])
@login_required
def details():
    user = g.user
    owner_detail = RegistrationDetail.query.filter_by(id=user.id)
    return render_template("owner_details.html", p=owner_detail)


@own.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('owner.owner_home'))
