from flask import Blueprint, request, render_template
from app.FinalBooking.forms import BookingForm
from app.Notifications.NotifyFunctions import sendverified, sendRider

final_book = Blueprint('booking', __name__, url_prefix='/booking')
"""
Owner Page Confirmation
Redirected to Notification Api 
"""

@final_book.route('/final_booking/<variable>', methods=['GET', 'POST'])
def final_booking(variable):
    form = BookingForm(request.form)
    print("in Booking")
    print(variable)
    count = 0

    if request.method == 'GET':
        print("In Get")
        return render_template("submisson_form.html", form=form)

    elif request.method == 'POST':
        response_re = request.form.getlist("response")
        F_response = [x.encode('UTF8') for x in response_re]
        print(F_response)
        print(form.email.data)
        print(count)

        if F_response[0] == 'Yes':
            if count == 0:
                print("IN RESPONSE")
                count = count + 1
                print(count)
                sendverified(form.email.data)
                sendRider(form.email.data)
                return render_template("confirmation.html")

            elif count != 0:
                return render_template("Deny.html")
