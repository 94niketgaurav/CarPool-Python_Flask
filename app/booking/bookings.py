from flask import Blueprint, request, render_template

from app.booking.forms import BookingForm
from app.notifications.NotifyFunctions import send_verified, send_rider

final_book = Blueprint('booking', __name__, url_prefix='/booking')
"""
Owner Page Confirmation
Redirected to Notification Api 
"""
form = ""


@final_book.route('/final_booking/<variable>', methods=['GET'])
def final_booking(variable):
    """
    For Owner to confirm the ride
    :param variable:
    :return:
    """
    global form
    form = BookingForm(request.form)
    print(variable)
    if request.method == 'GET':
        return render_template("submisson_form.html", form=form)


@final_book.route('/final_booking/<variable>', methods=['POST'])
def post_final_booking(variable):
    """
    After Confirmation
    :param variable:
    :return:
    """
    global form
    form = BookingForm(request.form)
    count = 0
    print(variable)
    if request.method == 'POST':
        response_re = request.form.getlist("response")
        feed_response = [x.encode('UTF8') for x in response_re]
        print(feed_response)
        print(form.email.data)
        print(count)

        if feed_response[0] == 'Yes':
            if count == 0:
                print("IN RESPONSE")
                count = count + 1
                print(count)
                send_verified(form.email.data)
                send_rider(form.email.data)
                return render_template("confirmation.html")

            elif count != 0:
                return render_template("Deny.html")
