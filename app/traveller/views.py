from flask import Blueprint, request, render_template, redirect, url_for

from app.Repository.TravellerRepository import TravellerRespository
from app.models import RegistrationDetail
from app.notifications.NotifyFunctions import send_notification
from app.traveller import TravellerDto
from app.traveller.forms import Travellerdirect

travel = Blueprint('traveller', __name__, url_prefix='/traveller')
traveller_name = ""
form = ""


@travel.route('/')
def travelhome():
    return render_template("traveller.html")


@travel.route('/DirectTravel', methods=['GET', 'POST'])
def direct_travel():
    """
    Traveller Details and Repo Creation:
    """

    global form
    form = Travellerdirect(request.form)

    if request.method == 'GET':
        print("In Get Call")
        return render_template("direct_travel.html", form=form)


@travel.route('/DirectTravel', methods=['POST'])
def post_direct_travel():
    traveller_repo = TravellerRespository()
    form = Travellerdirect(request.form)
    if request.method == 'POST':
        print("In Post call")
        travellerdto = TravellerDto(form.name.data, form.email.data, form.phone.data, form.start_time.data)

        global traveller_name
        traveller_name = form.name.data

        traveller_repo.create_traveller(travellerdto)
        if form.validate_on_submit() is True:
            rides = RegistrationDetail.query.filter_by(start_location=form.start_location.data,
                                                       drop_location=form.drop_location.data)
            return render_template("direct_index.html", r=rides)


@travel.route('/rides', methods=['POST'])
def rides():
    """
    Final confirmation
    :return:
    """
    if request.method == 'POST':
        drivers = request.form.getlist("selected_rides")
        driver = [x.encode('UTF8') for x in drivers]
        print(driver)
        print(traveller_name)
        send_notification(driver, traveller_name)
        return redirect(url_for('home.home'))

    return render_template("traveller.html")
