from flask import Blueprint, request, render_template, redirect, url_for
from app.traveller.forms import TravellerDirect
from app.models import services
from app.Notifications.NotifyFunctions import sendNotification
from app.RepositoryService.travellerDto import travellerDto
from app.RepositoryService.travellerRepository import travellerRespository

traveller = Blueprint('traveller', __name__, url_prefix='/traveller')
traveller_name = ""

@traveller.route('/')
def travel():
    return render_template("traveller.html")


# @traveller.route('/signup', methods=['GET', 'POST'])
# def trasignup():
#     form = TRSignup(request.form)
#
#     if request.method == 'GET':
#         print("IN Get call")
#         return render_template("t_signup.html", form=form)
#
#     elif request.method == 'POST':
#         print("In post call ")
#         if form.validate_on_submit() is True:
#             td = models.travellersignup(form.name.data, form.email.data, form.password.data, form.sl.data, form.st.data,
#                                         form.dl.data)
#             db.session.add(td)
#             db.session.commit()
#             print("services commit")
#             return redirect('/rides')
#         return render_template("rides.html", form=form)


@traveller.route('/DirectTravel', methods=['GET', 'POST'])
def dtravel():
    form = TravellerDirect(request.form)
    traveller_repo = travellerRespository()

    if request.method == 'GET':
        print("In Get Call")
        return render_template("direct_travel.html", form=form)

    elif request.method == 'POST':
        print("In Post call")
        traveller_dto = travellerDto(form.name.data, form.email.data, form.phone.data,form.start_time.data)
        global traveller_name
        traveller_name = form.name.data

        traveller_repo.create_user(traveller_dto)
        if form.validate_on_submit() is True:
            print("IN form")
            rides = services.query.filter_by(start_location=form.start_location.data,
                                             drop_location=form.drop_location.data)
            return render_template("direct_index.html", r=rides)


@traveller.route('/rides', methods=['POST'])
def rides():
    if request.method == 'POST':
        drivers = request.form.getlist("selected_rides")
        driver = [x.encode('UTF8') for x in drivers]
        print(driver)
        print(traveller_name)
        sendNotification(driver, traveller_name)
        return redirect(url_for('home.home'))
        """How to Wait For Owner to Reply Back Then show Rider Details of Owner"""

    return render_template("traveller.html")
