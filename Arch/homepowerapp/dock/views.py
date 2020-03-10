from django.shortcuts import render
from django.http import JsonResponse
from twilio.rest import Client as TwilioRestClient
from django.contrib.auth.models import User
from django.conf import settings
from .models import userAccount, Residence, Unit
import time
# Create your views here.
def Send(request):

    if request.method == "GET" and request.GET["type"] == "power":
        state = request.GET["state"]
        to = '+'+str("+27626412910")
        # to = '+'+str("+27630547090")
        fromNum = "+18704740315"
        message =  state
        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        ms = client.messages.create(body=message, to=to, from_=fromNum)
        sent_message = ms.sid

        time.sleep(10)

        saved_message = client.messages.list(limit=1)
        print("saved message " + saved_message[0].sid)
        print("sent message " + sent_message)
        print("sent status "+ ms.status)
        print("saved status "+ saved_message[0].status)

        #change unit status
        unit = Unit.objects.get(cell_no="+27626412910")
        if state == "ClearRD0" and saved_message[0].status == "delivered":
            unit.status  = True
            unit.save()

        if state == "SetRD0" and saved_message[0].status == "delivered":
            unit.status  = False
            unit.save()

        response = JsonResponse({"Response":"state is "+state, "sms_status":saved_message[0].status})
    
    elif request.method == "GET" and request.GET["type"] == "login":
        pass_ =   request.GET["pass"]
        username = request.GET["username"]
        user = User.objects.filter(username=username)
        is_password = user[0].check_password(pass_)

        if is_password == True:
            response = JsonResponse({"authenticated":"user is authenticated","username":username})
        else:
            response = JsonResponse({"authenticated":"user is not authenticated"})

    elif  request.method == "GET" and request.GET["type"] == "getResidence":
        username = request.GET["username"]
        user = User.objects.get(username=username)
        user_acc = userAccount.objects.get(user=user)
        residence = Residence.objects.filter(user_account=user_acc)

        residence_array = []
        for r in residence:
            data = {"name":r.residence_name,"id":r.id}
            residence_array.append(data)

        response = JsonResponse({"data":residence_array[:5]})

    elif request.method == "GET" and request.GET["type"]=="getUnit":
        res=request.GET["id"]
        residence=Residence.objects.get(id=res)
        unit=Unit.objects.filter(residence=residence)
        
        unit_array=[]
        for u in unit:
            unitdata={"unum":u.unit_no,"id":u.id,"cell":u.cell_no,"status":u.status,"res_id":u.residence.id}
            unit_array.append(unitdata)

        response=JsonResponse({"unitdata":unit_array[:5]})
    



    return response