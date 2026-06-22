from django.contrib.auth.models import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import Transcation
from django.http import JsonResponse
import json
import io
import base64
from home.views import *# from datetime import date, datetime
import os
import threading
import time
from django.contrib.auth import views as auth_views
import datetime


def your(request):
    now = datetime.datetime.now()
    print("Date: " + now.strftime("%Y-%m-%d"))
    return render(request, "your.html")


def export_data_as_json(request):
    data = list(Transcation.objects.values())
    print(json.dumps(data))
    a = json.dumps(data)

    return JsonResponse(data, safe=False)


def export_data_as_json_by_id(request, id):
    data = Transcation.objects.values(
        "id", "date_t", "amount_t", "category_t", "description_t"
    ).get(id=id)
    print(json.dumps(data))
    return JsonResponse(data, safe=False)


class TranscationViewSet(viewsets.ModelViewSet):
    queryset = Transcation.objects.all()
    serializer_class = TranscationSerializer


# def export_data_as_text(request):
#     data = list(Transcation.objects.values())
#     with open("data.json", "w") as file:
#         json.dump(data, file, default=str)

#     return JsonResponse({"message": "ok"})


def delete_file_after_delay(file_path, delay_seconds=300):
    """Delete file after specified delay using threading"""

    def delete_file():
        time.sleep(delay_seconds)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File {file_path} deleted successfully")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    thread = threading.Thread(target=delete_file)
    thread.daemon = True
    thread.start()


import plotly.express as px
import pandas as pd
import numpy as np
import pandas as pd
import csv
from . import *


def plot_transactions(request):
    # Sample data

    # Data
    df = pd.read_csv("p.csv")
    fig = px.line(
        df,
        x="date_t",
        y="amount_t",
        color="date_t",
        line_group="date_t",
        hover_name="amount_t",
        line_shape="spline",
        render_mode="svg",
    )
    fig.show()

    # Important: close the figure to free memo
    return render(request, "plot_transactions.html")

    data = {
        "Date": pd.to_date(["2023-01-01", "2023-01-02", "2023-01-03"]),
        "Value": [10, 12, 8],
    }
    df = pd.DataFrame(data)

    fig = px.line(df, x="Date", y="Value", title="Time Series Example")
    fig.show()


def view_data(request):

    # search = []  # Initialize search results

    return render(request, "view_data.html")


def view_transcation(request):
    if request.method == "POST":
        form = request.POST
        start = form.get("start")
        end = form.get("end")

        if not start or not end:
            return JsonResponse(
                {"error": "Start and end dates are required"}, status=400
            )

        try:
            d = list(Transcation.objects.filter(date_t__range=[start, end]).values())

            with open("d.json", "w") as file:
                json.dump(d, file, default=str, indent=2)

            table(request)

            return JsonResponse({"message": "ok", "count": len(d)})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "view_transcations.html")


def table(request):
    json_file_path = "D:/django_code/core/d.json"
    try:
        with open(json_file_path, "r") as file:
            d = json.load(file)
            print(d)
            delete_file_after_delay(json_file_path, 60)
    except FileNotFoundError:
        d = {}

    return render(request, "table.html", {"d": d})


def all_data(request):
    json_file = "D:/django_code/core/data.json"

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # search = []  # Initialize search results

    return render(request, "all_data.html", {"data": data})


def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            messages.info(request, "check password")
            print("password is not matching")
            return redirect("/register/")

        elif User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("/register/")
        else:
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password),
            )
        return redirect("/login/")

    queryset = User.objects.all()
    context = {"User": queryset}

    return render(request, "register.html", context)


@login_required(login_url="/login/")
def dashboard(request):
    queryset = Transcation.objects.all()
    context = {"Transcation": queryset}

    return render(request, "dashboard.html", context)


def add_transcation(request):
    if request.method == "POST":
        form = request.POST
        date_t = form.get("date_t")
        amount_t = form.get("amount_t")
        category_t = form.get("category_t")
        description_t = form.get("description_t")

        Transcation.objects.create(
            date_t=date_t,
            amount_t=amount_t,
            category_t=category_t,
            description_t=description_t,
        )

        # export_data_as_text(request)
        send_data_to_jsonbin(request)
        
        return redirect("/dashboard/")

    return render(request, "add_transcation.html")


# Make sure this import exists


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")
        # if not User.objects.filter(password=password).exists():
        #     messages.error(request, "Invalid password")
        #     return redirect("/login/")
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")

        else:
            messages.error(request, "something wrong")
            return redirect("/login/")

    queryset = User.objects.all()
    context = {"User": queryset}
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("/login/")


def home(request):
    return render(request, "home.html")


def password_reset_confirm(request):
    return render(request, "password_reset_confirm.html")



import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Constants from your JSONBin.io dashboard
JSONBIN_API_KEY = os.environ.get("JSONBIN_API_KEY")  # Replace with your Master Key
# Optional: Include if you want to group bins under a specific collection
COLLECTION_ID = "YourCollectionID" 

@csrf_exempt
def send_data_to_jsonbin(request):
    # 1. Prepare your Django data structure (e.g., dictionary)
    my_django_data = {
        "app": "Django Transcation",
        "status": "active",
        "metrics": {
            "total_users": 1050,
            "server_health": "good"
        }
    }
    
    # 2. Serialize data into a JSON string using json.dumps()
    # Note: Use json.dumps() to format your payload as a string
    serialized_payload = json.dumps(my_django_data)
    
    # 3. Configure the HTTP headers required by JSONBin.io
    headers = {
        'Content-Type': 'application/json',
        'X-Master-Key': JSONBIN_API_KEY,
        # 'X-Collection-Id': COLLECTION_ID  # Uncomment if saving to a specific collection
    }
    
    # 4. Push data to create a new "Bin"
    endpoint_url = "https://jsonbin.io/transcation"
    
    try:
        response = requests.post(endpoint_url, data=serialized_payload, headers=headers)
        response_data = response.json()
        
        if response.status_code == 200:
            # Successfully saved! JSONBin returns a unique 'id' for the bin
            bin_id = response_data['metadata']['id']
            return JsonResponse({"status": "success", "bin_id": bin_id, "data": response_data})
        else:
            return JsonResponse({"status": "failed", "error": response_data}, status=response.status_code)
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)