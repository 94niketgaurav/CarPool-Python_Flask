import requests
import json
from app.models import traveller_direct, Users, services

URL = "http://api.treebohotels.com/v1/notification/email/"
"""
param:Parameters
Datastore:json data to be sent

Consists of Notification services 
1.Traveller Details
2.Owner Details
3.Confirmation To Both

"""


def sendNotification(owner_mail, traveller_name):
    param = []
    print(owner_mail)

    for rides in owner_mail:
        user = Users.query.filter(Users.id == rides)
        for value in user:
            param.append(value.email)
    body = "http://127.0.0.1:5000/booking/final_booking/" + str(traveller_name) + "\n You Have A Rider"
    datastore = {
        "data": {
            "subject": "CarPool-App",
            "sender": "niket.gaurav@treebohotels.com",
            "receivers": {
                "to": param,
                "cc": [],
                "bcc": []
            },
            "consumer": "prowl",
            "attachments": [],
            "body_text": body
        }
    }
    Json_data = json.dumps(datastore)
    headers = {'content-type': 'application/json'}
    r = requests.post(url=URL, data=Json_data, headers=headers)
    print(r.json())
    return


def sendverified(traveller_email):
    param = []
    param.append(traveller_email)
    print(param)
    param = [x.encode('UTF8') for x in param]
    print(param)
    body = {'name': '', 'email': '', 'phone': ''}

    pr = traveller_direct.query.all()
    for values in pr:
        print(values.name)
        body['name'] = values.name
        print(values.email)
        body['email'] = values.email
        print(values.phone)
        body['phone'] = values.phone

    message = "Thanks Owner for Your Concern\n " + " " + "Rider Details:\n" + str(body['name']) + "\n  " + str(
        body['email']) + "\n  " + str(body['phone'])
    print(message)

    datastore = {
        "data": {
            "subject": "CarPool-App",
            "sender": "niket.gaurav@treebohotels.com",
            "receivers": {
                "to": param,
                "cc": [],
                "bcc": []
            },
            "consumer": "prowl",
            "attachments": [],
            "body_text": message
        }
    }
    Json_data = json.dumps(datastore)
    headers = {'content-type': 'application/json'}
    r = requests.post(url=URL, data=Json_data, headers=headers)
    print(r.json())
    return


def sendRider(ridr_email):
    ridr_email = ridr_email.encode('UTF8')
    print("In Rider")
    print(ridr_email)

    body = {'name': '', 'email': '', 'Phone Number': '', 'Car model': '', 'Car Number': '', 'seats': '', 'type': ''}
    user = Users.query.filter_by(email=ridr_email).first()
    print(user)
    body['name'] = user.name
    body['email'] = user.email
    id = user.id

    service = services.query.filter_by(id=id).first()
    body['Phone Number'] = service.phone_number
    body['Car model'] = service.car_model
    body['Car Number'] = service.car_number
    body['seats'] = service.seats
    body['type'] = service.type

    message = "Your Ride has been Confirmed\n " + " " + "Owner  Details:\n " + str(body['name']) + "\n  " + str(
        body['email']) + "\n  " + str(body['Phone Number']) + "\n  " + str(body['Car model']) + "\n  " + str(
        body['Car Number']) + " " + str(
        body['seats']) + "\n  " + str(body['type'])

    param = []
    traveller = traveller_direct.query.all()
    for values in traveller:
        param.append(values.email)

    datastore = {
        "data": {
            "subject": "CarPool-App",
            "sender": "niket.gaurav@treebohotels.com",
            "receivers": {
                "to": param,
                "cc": [],
                "bcc": []
            },
            "consumer": "prowl",
            "attachments": [],
            "body_text": message
        }
    }
    Json_data = json.dumps(datastore)
    headers = {'content-type': 'application/json'}
    r = requests.post(url=URL, data=Json_data, headers=headers)
    print(r.json())
    return
