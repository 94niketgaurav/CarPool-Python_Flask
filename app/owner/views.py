from flask import Blueprint, request, render_template, g, redirect, url_for
from app import app
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Users, services
from app.owner.forms import signupForm, service, Login
from app.RepositoryService.AuthService import AuthService, InvalidUserException, UserExistsException
from app.RepositoryService.UserDto import UserDto
from app.RepositoryService.DatabaseDto import DatabaseDto
from app.RepositoryService.DatabaseRepository import databaseRespository

own = Blueprint('owner', __name__, url_prefix='/owner')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def before_request():
    g.user = current_user


@own.route('/')
def ownerhome():
    return render_template("owner.html")


@own.route('/signup', methods=['GET', 'POST'])
def signup():
    auth_service = AuthService()
    form = signupForm(request.form)
    print("in signup")

    if request.method == 'GET':
        print("IN GEt call")
        return render_template("owner_signup.html", form=form)

    elif request.method == 'POST':
        print("In POST call")

        if form.validate_on_submit() is True:
            print("In validated section")
            user_dto = UserDto(form.email.data, form.password.data, form.name.data)
            try:
                auth_service.create_user(user_dto)
                return redirect(url_for('owner.owner_service'))
            except UserExistsException:
                return render_template("owner_signup.html", form=form)


@own.route('/services', methods=['GET', 'POST'])
def owner_service():
    database_repo = databaseRespository()
    form = service(request.form)

    if request.method == 'GET':
        print("IN Get call")
        return render_template("services.html", form=form)

    elif request.method == 'POST':
        print("In post call ")

        if form.validate_on_submit() is True:
            database_dto = DatabaseDto(
                form.phone_number.data, form.start_location.data, form.start_time.data, form.drop_location.data,
                form.car_model.data, form.car_number.data, form.seats.data, form.type.data)
            database_repo.create_service_database(database_dto)
            return redirect(url_for('home.home'))
    return render_template("services.html", form=form)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(str(id))


@own.route('/login', methods=['GET', 'POST'])
def login():
    auth_service = AuthService()
    form = Login(request.form)

    if request.method == 'GET':
        print("In Get Method")
        return render_template('Owner_login.html', form=form)

    elif request.method == 'POST':
        print("In Post Method")
        user_dto = UserDto(form.email.data, form.password.data)
        try:
            registered_user = auth_service.load_user(user_dto)
            login_user(registered_user)
            return redirect(request.args.get('next') or url_for('owner.index'))
        except InvalidUserException:
            return redirect(url_for('owner.login'))


@own.route('/index', methods=['GET'])
@login_required
def index():
    user = g.user
    print("in index " + str(user.id))
    owner_service = services.query.filter_by(id=user.id)
    return render_template("owner_index.html", p=owner_service)


@own.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('owner.ownerhome'))
