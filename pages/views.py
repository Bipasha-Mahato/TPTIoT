from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import sensor_data, node_details
from .forms import UserUpdateForm, ProfileUpdateForm
from django.db.models import Max
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
@login_required(login_url='login')
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "dashboard.html", {})

def login_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Login Page</h1>")
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
    test = "hello world"
    context = {
    "test": test
    }
    return render(request, 'signin.html', context)
    #return render(request, "signin.html", {})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url='login')
def editProfile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            #messages.success(request, f'Your account has been updated!')
            return redirect('/profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_form' : update_form,
        'profile_form' : profile_form
    }
    return render(request, "edit_profile.html", context)

def register_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Register Page</h1>")
    return render(request, "register.html", {})

@login_required(login_url='login')
def dashboard_view(request, *args, **kwargs):
    queryset = node_details.objects.all()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM pages_sensor_data a WHERE Id = (SELECT MAX(id) FROM pages_sensor_data WHERE a.node_id_id = node_id_id) ORDER BY node_id_id''')
    result = cursor.fetchall()
    #print(result)
    context = {
            "object_list": queryset,
            "data_list": result
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='login')
def report_all(request):
    if request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # print(from_date)
        # print(to_date)
    else:
        from_date = "null"
        to_date = "null"
    if from_date and to_date != "null":
        result_list = []
        hum_result_list = []
        cursor = connection.cursor()
        cursor.execute(''' SELECT DISTINCT node_id_id FROM pages_sensor_data ''')
        node_ids = cursor.fetchall()
        for id in node_ids:
            nid = id[0]
            # print(nid)
            cursor.execute('''SELECT temperature FROM pages_sensor_data WHERE node_id_id=%s ''', [nid])
            result = cursor.fetchall()
            result_list.append(result)
        for id in node_ids:
            nid = id[0]
            # print(nid)
            cursor.execute('''SELECT humidity FROM pages_sensor_data WHERE node_id_id=%s ''', [nid])
            hum_result = cursor.fetchall()
            hum_result_list.append(hum_result)
        # print(result_list)
        temp_data = sensor_data.objects.filter(date_inserted__range=(from_date, to_date))
        number_of_nodes = node_details.objects.all()
    else:
        temp_data = "No Data Available"
    temperature_list = []
    humidity_list = []
    label_list = []
    if temp_data != "No Data Available":
        for item in temp_data:
            temperature_list.append(item.temperature)
            humidity_list.append(item.humidity)
            label_list.append(item.date_inserted.strftime('%d/%m/%Y, %H:%M:%S'))
    # print(temperature_list)
    # print(label_list)
    # for id in node_ids:
    temp_list = []
    hum_list = []

    for list in result_list:
        list_items = [item for t in list for item in t]
        temp_list.append(list_items)
        # print(list_items)
    for list in hum_result_list:
        hum_list_items = [item for t in list for item in t]
        hum_list.append(hum_list_items)

    # print(hum_list)
    context = {
        "temperature":temp_list,
        "humidity":hum_list,
        "label":label_list,
    }

    return render(request, "report_by_date.html", context)

@login_required(login_url='login')
def devices(request, *args, **kwargs):
    queryset = node_details.objects.all()

    for node in queryset:
        #print(node.node_id)
        result = sensor_data.objects.filter(node_id=node.node_id).last()
        #print(result.date_inserted)
        if result != None:
            node.last_active = result.date_inserted
            node.save()

    context = {
            "object_list": queryset
    }
    return render(request, "devices.html", context)

@login_required(login_url='login')
def device_details(request, node_id):
    obj = get_object_or_404(sensor_data, id=node_id)
    context = {
        "node_id":node_id,
        "object": obj
    }
    return render(request, "device_details.html", context)


@login_required(login_url='login')
def report(request):

    #return redirect('Report-View')
    return render(request, "report.html")




def get_data(request, *args, **kwargs):

    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


#view to fetch Temperature
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, node_id, format=None):
        #node_id = 2
        temp_data = sensor_data.objects.filter(node_id=node_id).order_by('-id')[0]
        #print(temp_data.temperature)
        time_data = sensor_data.objects.filter(node_id=node_id).order_by('-id')[0]
        print(time_data.date_inserted)
        #print(last_record)
        labels = time_data.id
        default_items = temp_data.temperature
        data = {
                "labels": labels,
                "default": default_items,
        }
        print(labels)
        return Response(data)
#End of Temperature fetch view


#View to fetch Humidity
class ChartData1(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, node_id, format=None):
        #node_id = 2
        temp_data = sensor_data.objects.filter(node_id=node_id).order_by('-id')[0]
        #print(temp_data)
        time_data = sensor_data.objects.filter(node_id=node_id).order_by('-id')[0]
        #print(time_data)
        #print(last_record)
        labels = time_data.id
        default_items = temp_data.humidity

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
#End of Humidity fetch view


#View to fetch Report
class Report(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, from_date, to_date, format=None):
        #node_id = 2
        temp_data = sensor_data.objects.filter(created_at__range=(start_date, end_date))
        #print(temp_data)
        time_data = sensor_data.objects.filter(created_at__range=(start_date, end_date))
        #print(time_data)
        #print(last_record)
        labels = time_data.id
        default_items = temp_data.humidity

        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
#End of Report fetch view
