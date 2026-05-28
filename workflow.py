https://www.django-rest-framework.org/#requirements

Setup
====================================================>
create Travel_Fullstack_project folder in the desktop

create 2 folders one is for froent end and another one is for backend in the Travel_Fullstack_project folder
django for backend and react for frontend
djanog install and set up in teh django folder 
create a virtual environment in the django folder and install django in that virtual environment
PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django> python -m venv aenv-
C:\Users\Admin\AppData\Local\Programs\Python\Python310\
    
note : if we delete the virtual environment then we have to create it again and install the django and rest framework again in the virtual environment.    
    
to activate the virtual environment run the below command in the terminal
PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django> .\aenv\Scripts\activate                      
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django>     
    
    
    
install the django in the virtual environment
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django> pip install django
    
install the djangorestframework in the virtual environment    
pip install djangorestframework
    
    
    
now we have to create the project in the django folder :     
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django> django-admin startproject travels    
travels in the name of the project and it will create a folder with the name travels in the django folder and inside will have another travel folder with the same name and some files in it. 
Ex : settings.py ,
urls.py, 
wsgi.py,
asgi.py 
manage.py file in the django folder not in the travels folder.

note : 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

these are the default settings in the settings.py file and we have to add the rest framework in the installed apps to use the rest framework in our project.
so we have to add 'rest_framework' and 'rest_framework.authtoken'  in the INSTALLED_APPS list in the settings    

🧠 What is 'rest_framework.authtoken'?
👉 It is a Django app provided by Django REST Framework
👉 It gives you a Token model + database table + authentication system
🔥 Simple meaning
👉 When you add:
'rest_framework.authtoken'
Django will:
Create a Token table in database after adding this app and if we run the migrations 
Allow you to use:
Token.objects.get_or_create()
🧠 Without it (your case earlier)
You wrote:
token, created = Token.objects.get_or_create(user=user)
But Django said:
Token has no attribute 'objects'





now run the server to check if everything is working fine or not
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django>travels python manage.py runserver

output in console :
Run 'python manage.py migrate' to apply them.
April 28, 2026 - 21:56:47
Django version 5.2.13, using settings 'travels.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.    

now db.sqlite3 file is created in the django folder and we have to run the migrate command to create the tables in the database.

Starting development server at http://127.0.0.1:8000/
right clcik on this line and open in the browser to check if the server is running fine or not.
will get this output : The install worked successfully! Congratulations!

>>> exit() ==> will come out of the venv 
PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django> 

===============================================================>09:04 Create App
Create App : 
    
create an app in the travels project to create the models and views for the travel app
note: we have to create the app in the project folder not in the django folder because the manage.py file is in the project folder and we have to run the commands from the project folder.
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django\travels> 
python manage.py startapp bookings

admin.py , models.py , views.py, tests.py, apps.py files are created in the bookings folder.

===============================================================>

Models : features(buses , users,seats , login , registration) related schemas or properties we will create in the models.py file in the bookings folder.
    
add schema related to bus and seats models in the models.py file     

add the installed app in the installed_apps in the settings.py file i.e bookings

===============================================================>
superuser : 
    
by default in the urls.py file in the  travel project with this code :
          
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
]

note : pip install psycopg2-binary install this before migration 
👉 So Django now needs a bridge (driver) to talk to PostgreSQL 👉 That bridge = psycopg2

note : we have to create this bus_ticket_booking_system database in teh postgre sql database 1st 
add these deatils in the settings.py file before migrating table schema into the database : 
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'bus_ticket_booking_system',
        'USER':'postgres',
        'PASSWORD':'anil12345',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

now run the migrations : 
python manage.py makemigations
python manage.py migrate      


creating the superuser : 
    
python manage.py createsuperuser    

(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django\travels> python manage.py createsuperuser
Username (leave blank to use 'admin'): anil
Email address: anil@gmail.com
Password:1234 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(aenv) PS C:\Users\Admin\Downloads\Travel_FullStack_Project\django\travels> 



now using the above credentials we can login into the admin dashboard in this path 'admin/' in the project urls.py of the project folder 

now run the server : python manage.py runserver 
go into this url http://127.0.0.1:8000/admin/

it shows django administration 
username
passwiord

now after login we will see loout , change password 
groups , users add , change buttons will appear us but what ever the tables we crated those tables will not appear here 
the reason is we did not register those tables in the admin.py file in the bookings app folder 


from django.contrib import admin
from .models import Bus,Seats 

# Register your models here.
admin.site.register(Bus)
admin.site.register(Seats) 

now if we go to that admin page in ui will get the booking app realted tables like buss adn seatss so that is why we should create tables names with plural words 
now perform the crud oprations on the each table 

it will show like bus and bus object(1) if i created a single record int eh bus table now to appear the bus name , number , origin , destincatino 

we have to add this code in the models.py and admin.py files 


in models.py file 

# Create your models here.
# 💡 Instead of writing SQL like: CREATE TABLE Bus (...)
class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20,unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    features = models.TextField()
    start_time = models.TimeField()
    reach_time = models.TimeField()
    price = models.DecimalField(max_digits = 8 , decimal_places = 2)
    
    
    ### add this below code 
    def __str__(self):
        return f"{self.bus_name} {self.number} {self.origin} {self.destination}"
    
    __str__() ante object ni ela display cheyyalo define chestundi
“The __str__() method defines the human-readable representation of a model object, mainly used in admin panel
Volvo AP123 Hyderabad Bangalore
👉 __str__() tells Django:
“How should this object be displayed as text?”    
Without __str__() → ID card number only 🆔
With __str__() → Full name + details 👤
1️⃣ Django Admin Panel (VERY IMPORTANT)
In admin:
👉 Instead of:
Bus object (1)
👉 You see:
Volvo AP123 Hyderabad Bangalore
2️⃣ ForeignKey dropdowns
In your Seats model:
bus = models.ForeignKey('Bus', ...)
👉 When selecting bus:
Without __str__():
Bus object (1)
Bus object (2)
With __str__():
Volvo AP123 Hyderabad Bangalore
   
in admin.py file :
class BusAdmin(admin.ModelAdmin):
    list_display =('bus_name' , 'number','origin','destination')
    
# Register your models here.
admin.site.register(Bus,BusAdmin)       

all the models we created in the models.py file in the database those tables created like this one we apply the migrations
booking table ==> bookings_booking 
seat  table ==> bookings_seat
bus  table ==> bookings_bus
auth_user table is the deafult table created by django which stores the user details inlcuding the superuse also 
it contains fields like usrename,password,email,date_joined,last_login,is_superuser(true for superuser), is_staff(true for superuser) , is_active 


 
list_display in admin.py file  :  vs def __str__ in model.py : 

🧠 What is list_display?
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_name', 'number', 'origin', 'destination')
👉 It tells Django Admin:
“Show these columns in the admin list page from model”

🧠 Why __str__() exists
👉 It gives a human-readable name for ONE object   
🧪 Where __str__() is used (VERY important)
1. 🔗 ForeignKey dropdown (MOST IMPORTANT)
Imagine another model:
class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
In Django Admin form:
Without __str__():
Bus object (1)
Bus object (2)
===============================================================>
       
serializer : it reads the feilds from the djago model , knows how to convert into the json format
and validates the json data if you re saving  a new students based on the data types of the column given the table schema        
        
        
now we will create the serilizers in the bookings app by creating a file maually as serializers.py in the bookings app 
from rest_framework import serializers         
===============================================================>
signals : 
 no_of_seats = models.PositiveBigIntegerField()
    
  so howmmuch seat number we will decide to creat those many seat numbers
  in the seat model automatically for that we will creat a signal  

create signals.py : 
from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Bus , Seat

@receiver(post_save , sender = Bus)
def create_seats_for_bus(sender , instance , created , **kwargs):
    if created:
        for i in range(1,instance.no_of_seats + 1):
            Seat.objects.create(bus=instance , seat_number = f"s{i}") 
             
             
add the keyword in the bus model : no_of_seats 
    
in app.py file register that signal : 
def ready(self):
    import booking.signals        
    
    
 note : give the signal prompt to the chatgpt learn about it 

🧠 First understand the idea (very important)
You create a Bus
Bus has no_of_seats = 40
Instead of manually creating 40 seats ❌
Django will automatically create 40 Seat objects ✅

👉 This automatic action is done using signals

👉 A signal = “Hey Django, when something happens, do this extra work”
When a Bus is saved, automatically create seats
from django.db.models.signals import post_save

👉 Importing a signal called post_save
post_save means:
👉 “After saving an object”

from django.dispatch import receiver 
👉 This is a decorator (helper)
👉 It connects your function to the signal

@receiver(post_save , sender = Bus)
👉 Meaning:
“Whenever a Bus is saved, call the function below”
post_save → after saving
sender=Bus → only for Bus model

def create_seats_for_bus(sender , instance , created , **kwargs):
👉 This function runs automatically
Parameters:
sender → Bus model
instance → the actual Bus object/record created
created → True if new Bus, False if updated
**kwargs → extra unused data

Seat.objects.create(bus=instance , seat_number = f"s{i}")

👉 Creates seats like:

seat_number	bus
s1	Bus
s2	Bus
s3	Bus

👉 bus=instance → links seat to that bus

👉 f"s{i}" → generates:

s1, s2, s3...


📁 apps.py
def ready(self):
    import booking.signals

👉 This line is VERY IMPORTANT

👉 Without this:
❌ signals will NOT run

👉 Meaning:

Django loads your signals in the bookings app when app starts

===============================================================>        

authentication using the restframe work :  
    
in django we can create the default users with authentication 
we can implement the authenticatoin using the drf 

"django.contrib.admin" onbuiltly imported in settings.py file  ==> used for creating the superusers login , logout etc. functionalities 
but in the settings.py file "django.contrib.auth" model or middleware is imported inbuiltly
django.contrib.auth ==> using the this we can implement the user registration , 
login and log out functionalities easily without writting the code explicitely 




==> serilizers.py : below block is added in that : 
# when an object is initialized for this class tehn this log will gets executed  
# UserRegistrationSerializer class is inhereting from inheModelSerializer class to serialize(model object <-> json)     
class UserRegistrationSerializer(serializers.ModelSerializer):
    # write_only means we should not return it in the response 
    password = serializers.CharField(write_only = True)
    # meta tells whicc is the model and what are the fields to serialize(model object <-> json)
    class Meta:
        models = User  
        fields = ['username','email','password']
    # when .save() called this function will gets executed 
    # serializer = UserRegisterSerializer(data=request.data) 
    # if serializer.is_valid():
    #     serializer.save()    
    def create(self,data):
        user = User.create_user(
            username = data["username"],
            password = data["password"],
            email = data["email"]
        ) 
        return user
    
note : 
serializers.ModelSerializer is a Django REST Framework class that automatically creates serializer
fields based on a Django model, reducing manual work and helping convert data between JSON and 
database models efficiently.   

ModelSerializer = “automatic translator”

🔄 What it actually does
1. Converts model(object) → JSON
bus = Bus.objects.first()
serializer = BusSerializer(bus)

print(serializer.data)

👉 Output:

{
  "bus_name": "Express",
  "number": "AP02CD5678"
}
2. Converts JSON → model
data = {
  "bus_name": "Express",
  "number": "AP02CD5678"
}

serializer = BusSerializer(data=data)

if serializer.is_valid():
    serializer.save()

👉 Creates object in DB 
    
# ❓ Why?
# create() → stores plain password ❌ (danger)
# create_user() = secure user creation (password hashing)
# Serializer = gatekeeper 🚪

# class Meta:
# 👉 Used to tell serializer:

# Which model?
# Which fields to convert into the json format if we dont include some feilds
# in the fields key the in the view if we use those columns we will get the error?

# Takes input
# Validates
# Creates object safely 
# 👉 Runs when you do:

# serializer.save()
# def create(self, validated_data):




Serializer runs only when you call it in a view  
serializer = UserRegisterSerializer(data=request.data) 
if serializer.is_valid():
    serializer.save()
✅ Actual meaning
write_only=True means:
Accept input from user ✅
Do NOT return in API response ❌



===============================================================>

views : 
serializers.py  :    
class BookingSerializer(serializers.ModelSerializer):
    bus = serializers.StringRelatedField()
    seat = SeatSerializer
    user = serializers.StringRelatedField() 
    
    class Meta:
        models = Booking
        fields ='__all__'
        read_only_fields = ['user','bus','seat''booking_time']
                    
StringRelatedField = “show human-readable text instead of ID”
if this method is not defined in the model class : __str__()
👉 No, you will NOT get an error ❌
👉 But the output will be ugly / not useful 😄
like this  : 
<Seat: Seat object (1)>   
👉 Instead of showing bus ID, it shows:
Volvo AP123 Hyderabad Bangalore
👉 It uses __str__() method of Bus model 
  
7. Read-only fields
read_only_fields = ['user', 'booking_time', 'bus', 'seat']
👉 These fields:
Cannot be modified ❌
Cannot be sent from frontend ❌
Only shown in response ✅


read_only_fields : is used to prevent users from modifying important fields. These fields are automatically set by the backend (like logged-in user or booking time) and are only shown in the response, not accepted from the frontend, ensuring security and data integrity.
🔥 With read_only_fields
read_only_fields = ['user', 'booking_time']
👉 Now:
User CANNOT send these fields ❌
If they send → error 🚫  
🔐 Why this is IMPORTANT?
🚀 Real-World Example (VERY IMPORTANT)
🎫 Bus Ticket Booking App
Imagine:
You open app and book ticket:
You send request:
{
  "bus": 1,
  "seat": 5
}
❌ Problem if NO read_only_fields
User can cheat 😈:
{
  "user": "admin",
  "booking_time": "2000-01-01",
  "bus": 1,
  "seat": 5
}
👉 User is:
Changing user ❌
Changing time ❌
🔥 With read_only_fields
read_only_fields = ['user', 'booking_time']
👉 Now:
User CANNOT send these fields ❌
If they send → error 🚫
🧠 What happens internally?
Backend does:
booking.user = request.user
booking.booking_time = current_time
🔐 Why this is IMPORTANT?
👉 To protect your system


view.py : 
class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id = seat_id)
            if seat.is_booked:
                return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)

            seat.is_booked = True
            seat.save()

            bookings = Booking.objects.create(
                user = request.user,
                bus = seat.bus,
                seat = seat
            )
            serializer = BookingSerializer(bookings)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Seat.DoesNotExist:
            return Response({'error':'Invalid Seat ID'}, status=status.HTTP_400_BAD_REQUEST)
            

class BookingView(APIView):
    permission_classes = [IsAuthenticated]
    /
🔐 Authentication
permission_classes = [IsAuthenticated]
👉 Only logged-in users can access this API
❌ If user is NOT logged in
🔴 Response you will get
{
  "detail": "Authentication credentials were not provided."
}
👉 Status code:
401 Unauthorized
🧠 Key Concept
Booking.objects.create(
    user=request.user,   # object
    bus=seat.bus,        # object
    seat=seat            # object
)
👉 In Python → objects
👉 In database → IDs
request.user.id = 10
seat.bus.id = 3
seat.id = 5



class UserBookingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,user_id):
        if request.user.id != user_id :
            return Response({"error":"unauthorized"},status = status.HTTP_401_UNAUTHORIZED)
        bookings = Booking.objects.filter(user_id = user_id)
        serializer = BookingSerializer(bookings , many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)  
            
# class UserBookingView(APIView):
# 👉 This is a Django REST API view
# 👉 It is used to get all bookings of a specific user

# 🔐 Security part
# permission_classes = [IsAuthenticated]
# 👉 Only logged-in users can access this API  

# if request.user.id != user_id:
# 👉 This means:
# You can only see your own bookings
# You cannot access others' data👉 If not logged in → request will be rejected

# 👉 many=True means you are passing multiple objects (a list/queryset), not a single objec
# With many=True
# 👉 Serializer will loop through all records
# Like:
# for booking in bookings:
#     serialize(booking)
    
    
    
🧱 2. What is APIView?
class BookingView(APIView):
👉 APIView = manual control
You write logic yourself (get, post, etc.)
More flexible
More code  
except Seat.DoesNotExist: ✔ Yes, it is specific to Django models  
seat = Seat.objects.get(id=seat_id)
seat.is_booked = True
seat.save()
Save changes to database
Like clicking “Save” button
Claim offer
Let’s break your code in a very simple, real-world way so you clearly understand 👇
🧠 What is this class?
class UserBookingView(APIView):
👉 This is a Django REST API view
👉 It is used to get all bookings of a specific user
🔐 Security part
permission_classes = [IsAuthenticated]
👉 Only logged-in users can access this API
👉 If not logged in → request will be rejected
📥 What is the INPUT?
This API expects:
1. User must be logged in
Token / session authentication
2. user_id in URL
Example:
GET /api/bookings/5/
👉 Here 5 is user_id
⚠️ Important Check
if request.user.id != user_id:
👉 This means:
You can only see your own bookings
You cannot access others' data
✔ Example:
Logged-in user ID = 5 → allowed
Logged-in user ID = 3, trying to access /5/ → ❌ Unauthorized
⚙️ What happens inside?
bookings = Booking.objects.filter(user_id=user_id)
👉 Fetches all bookings from DB where:
user_id = given user_id
🔄 Serialization
serializer = BookingSerializer(bookings, many=True)
👉 Converts database data → JSON format
📤 What is the OUTPUT?
return Response(serializer.data)
👉 Output will be JSON list of bookings
Example Output:
[
  {
    "id": 1,
    "user": 5,
    "bus": 10,
    "seat": "A1",
    "date": "2026-05-03"
  },
  {
    "id": 2,
    "user": 5,
    "bus": 12,
    "seat": "B3",
    "date": "2026-05-04"
  }
]
❌ If Unauthorized
{
  "error": "Unauthorized"
}
🎯 Simple Real-Life Meaning
👉 “Show me my bookings, but don’t show others' bookings”
🧠 One-line Summary
👉 This API:
Takes user_id
Checks if logged-in user matches
Returns that user's bookings in JSON
If you want, I can also:
✅ Show URL config (urls.py)
✅ Show Postman testing steps
✅ Explain how this works internally in Django
Just tell me 👍
serializer = BookingSerializer(bookings, many=True)  hwere many Tgrue means what 
Good question—this is a very important DRF concept 👇
🧠 What does many=True mean?
serializer = BookingSerializer(bookings, many=True)
👉 many=True means you are passing multiple objects (a list/queryset), not a single object
📦 In your case
bookings = Booking.objects.filter(user_id=user_id)
👉 This returns:
A QuerySet (list of bookings)
Not just one booking
So you must tell serializer:
👉 “Hey, this is a collection (many items)”
🔄 What happens internally?
With many=True
👉 Serializer will loop through all records
Like:
for booking in bookings:
    serialize(booking)
📤 Output
[
  {"id": 1, "seat": "A1"},
  {"id": 2, "seat": "B2"}
]
👉 List of objects
❌ What if you DON’T use many=True?
serializer = BookingSerializer(bookings)
👉 Django will throw error like:
Expected a dictionary, but got QuerySet
Because:
👉 It expects one object, but you gave many
🧠 When to use many=True vs False
Case	Use
Single object	many=False (default)
Multiple objects (list/queryset)	many=True
📌 Simple analogy
👉 Think like this:
One student → normal serializer
Full classroom → many=True
🎯 Your exact case
✔ filter() → gives multiple bookings
✔ So → many=True is mandatory
If you want, I can also show:
👉 What happens inside serializer step-by-step
👉 Difference between .get() and .filter() (very important for interviews)
class BookingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id = seat_id)
            if seat.is_booked:
                return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
            seat.is_booked = True
            seat.save()
            bookings = Booking.objects.create(
                user = request.user,
                bus = seat.bus,
                seat = seat
            )
            serializer = BookingSerializer(bookings)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Seat.DoesNotExist:
            return Response({'error':'Invalid Seat ID'}, status=status.HTTP_400_BAD_REQUEST)  
can u explina the above code to me in a simple way to understand it very easily line by line each param what is hte meanign and use of the APIView wha is eh djenot restapi what is the difference between APIVIew , ListCreateAPIView , RetrieveUpdateDestroyAPIView among these in whic case each one is used  : 
what is eh intput and output of theb above class  
param and seat.save() means what   except Seat.DoesNotExist: means what will this method or prop can be applied on teh models only   
class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
what is eh meaning of the above classes  what si the input and output fot the above clases   
You’ve packed a lot of important concepts here—good. I’ll keep it simple, step-by-step, and tie everything to real meaning so it sticks.
🧠 1. What is Django REST API?
👉 Django REST Framework (DRF) lets you build APIs.
API = a way for frontend / mobile / Postman to talk to your backend
Example:
App sends request → “Book seat”
Backend responds → “Seat booked successfully”
🧱 2. What is APIView?
class BookingView(APIView):
👉 APIView = manual control
You write logic yourself (get, post, etc.)
More flexible
More code
🔐 Authentication
permission_classes = [IsAuthenticated]
👉 Only logged-in users can use this API
📥 INPUT of this API
Request type:
POST /booking/
Body (JSON):
{
  "seat": 5
}
👉 seat = seat ID
📜 Now line-by-line explanation
🔹 Get seat ID
seat_id = request.data.get('seat')
👉 Takes seat ID from request
👉 Example: 5
🔹 Get seat object from DB
seat = Seat.objects.get(id=seat_id)
👉 Fetch seat with ID = 5
❗ What is this?
except Seat.DoesNotExist:
👉 If seat not found in DB → this error happens
✔ This is a model-level exception
✔ Yes, it is specific to Django models
🔹 Check if already booked
if seat.is_booked:
👉 If already booked → stop
🔹 Return error
return Response({'error': 'Seat already booked'}, status=400)
🔹 Book the seat
seat.is_booked = True
seat.save()
👉 seat.save() means:
Save changes to database
Like clicking “Save” button
🔹 Create booking record
Booking.objects.create(
    user=request.user,
    bus=seat.bus,
    seat=seat
)
👉 New booking entry created in DB
🔹 Serialize data
serializer = BookingSerializer(bookings)
👉 Convert DB object → JSON
📤 OUTPUT
{
  "id": 1,
  "user": 5,
  "bus": 2,
  "seat": 5
}
🎯 Summary of BookingView
👉 Input:
seat ID
👉 Output:
booking details OR error
⚙️ 3. Difference between APIView vs Generic Views
🔹 1. APIView
👉 You write everything manually
Use when:
Custom logic (like seat booking logic)
🔹 2. ListCreateAPIView
class BusListCreateView(generics.ListCreateAPIView):
👉 Combines:
GET → list all buses
POST → create new bus
📥 Input
GET:
GET /buses/
POST:
{
  "name": "Express Bus",
  "number": "TS09AB1234"
}
📤 Output
GET:
[
  {"id": 1, "name": "Bus1"},
  {"id": 2, "name": "Bus2"}
]
POST:
{"id": 3, "name": "New Bus"}
🔹 3. RetrieveUpdateDestroyAPIView
class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
👉 Handles:
GET (single bus)
PUT/PATCH (update)
DELETE (delete)
📥 Input
GET /buses/1/
PUT /buses/1/
DELETE /buses/1/
📤 Output
GET:
{"id": 1, "name": "Bus1"}
🧠 Easy Analogy
APIView → Cook everything yourself 🍳
ListCreateAPIView → Ready-made combo 🍱
RetrieveUpdateDestroyAPIView → CRUD machine ⚙️
⚠️ Important Interview Point
👉 Use APIView when:
Logic is complex (like seat booking)
👉 Use Generic Views when:
Simple CRUD operations    
===============================================================>
urls : 
to consume the views/functions in the application we have to call route them in the urls.py file 
in the bookings app note : we have to manually create the urls.py file in the bookings application.       

==> 1st of all the just copy the urls.py file code from the main project to application becaz 
imports and structure only difference is paths and function names only

==> note : imp. we have to import all the views from the view.py file 

bookings/urls.py  : 
from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, UserBookingView, BookingView, BusDetailView

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='buslist'),
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('user/<int:user_id>/bookings/', UserBookingView.as_view(), name="user-bookings"),
    path('booking/', BookingView.as_view(), name="booking")
]


note:
🧠 Meaning of <int:user_id>
<int:user_id>
👉 It means:
int → type converter
user_id → variable name
🔥 What it actually does
👉 Django will:
Take value from URL
Convert it into integer
Pass it to your view


in travels/urls.py: we have to add these routes 
    path('api-token-auth/', obtain_auth_token), # to generate the login token 
    path('api/', include("bookings.urls")) #  connect all booking app routes 
    
    => below route is came defaultly while creating the project 
    path('admin/', admin.site.urls),
    
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include("bookings.urls"))
]
 

🧪 Example setup  : 
urls.py = traffic manager (police 🚦)
It decides which request have to foarward towards which path to process that requet with view logic:
“This request → go to admin”
“This request → go to booking app”
   
   
🧠 1. Import admin
from django.contrib import admin
👉 This imports Django’s admin panel
✔ URL like:
/admin/
✔ Used for:
Managing database (users, models, etc.)
Like a ready-made dashboard  

🧠 2. Import URL tools
from django.urls import path, include
👉 These are used to define routes
path() → create a URL
include() → connect another app’s URLs 


🧠 3. Import token authentication view
from rest_framework.authtoken.views import obtain_auth_token
👉 This is from Django REST Framework (DRF)
✔ Purpose:
Generate login token
🔐 What is token?
👉 Instead of login every time:
You get a token
Use it in requests
Example:
Authorization: Token abc123


🧠 4. URL patterns list
urlpatterns = [
👉 This is the main list of all routes


🔐 6. Token API
path('api-token-auth/', obtain_auth_token),
👉 This creates an API like:
POST /api-token-auth/
📥 Input:
{
  "username": "anil",
  "password": "1234"
}
📤 Output:
{
  "token": "abc123xyz"
}
👉 Use this token for authentication


🔗 7. Include app URLs
path('api/', include("booking.urls"))
👉 This connects your booking app URLs
✔ Meaning:
All URLs inside booking/urls.py
Will start with /api/
Example:
If inside booking.urls:
path('book/', BookingView.as_view())
👉 Final URL becomes:
/api/book/
===============================================================>
API Testing using the thunder client : 

==> sometimes we will see this warning message when we have to unapplied migrations in the terminal 
when we are trying to run the app using this command : python manage.py runserver 

note: this message only comes when we add/modify any models code in the models.py file not in the serializers.py file 

Warning message : You have 4 unapplied migration(s). Your project may not work properly until you apply 
the migrations for app(s): authtoken. Run 'python manage.py migrate' to apply them.
==> note: test the apis one by one in the postman we we are getting any error then ask the 
agent in the postman it explain very clearly the errors by clicking on the dubug with ai button in
the postman response window or best to copy the logs in the vscode terminal and give that logs to github copilot in teh vsocde 


note :
we have to install ==> pip install django-cors-headers 
corsheaders app we have to add in the settings.py file  : 
    'rest_framework',
    'bookings.apps.BookingsConfig',
    'rest_framework.authtoken',
    'corsheaders', ### add this ------------------>
 
👉 It controls:
“Which websites are allowed to call your backend API”  
👉 CORS = Cross-Origin Resource Sharing
👉 corsheaders is not useful for Postman, but it’s very important for frontend apps (browser).
❗ Problem without CORS

Imagine:
Frontend (React): http://localhost:3000
Backend (Django): http://127.0.0.1:8000

👉 React tries:
fetch("http://127.0.0.1:8000/api/register/")
❌ Browser blocks it
Error:
Access to fetch at 'http://127.0.0.1:8000/api/register/' 
from origin 'http://localhost:3000' 
has been blocked by CORS policy
👉 Even though API is correct
👉 Browser does NOT allow it
✅ Solution → corsheaders
When you add:
'corsheaders'
👉 You tell Django:
“Allow requests from other origins”
--------------------------------------------------------------->
1) /register api testing : 
url : http://127.0.0.1:8000/api/register/
method : post
payload : 
{
    "username": "samplelTest",
    "email": "sample@gmail.com",
    "password": "1234"
}
response : 
{
    "username": [
        "A user with that username already exists."
    ]
}
--------------------------------------------------------------->
1) /register api testing : 
url : http://127.0.0.1:8000/api/register/
method : post
payload : 
{
    "username": "Test5",
    "email": "test@gmail.com",
    "password": "1234"
}
response :
{
    "token": "f51a330bae2082511a40ea234dd7fab494b8ea70"
}
--------------------------------------------------------------->
2) /login api testing : 
url : http://127.0.0.1:8000/api/login/
method : post
payload : 
{
    "username": "Test5",
    "password": "1234"
}
response : 
{
    "token": "f51a330bae2082511a40ea234dd7fab494b8ea70",
    "user_id": 8
}
--------------------------------------------------------------->
3) /user/<int:user_id>/booking/ api testing : getting all user bookings based on the user_id   
url : http://127.0.0.1:8000/api/user/8/booking/
method : get
payload : 
headers = {
  'Authorization': 'Token f51a330bae2082511a40ea234dd7fab494b8ea70'
}

response : 
[
    {
        "id": 1,
        "bus": "apsrtc 4 Bobbili Vizag",
        "seat": {
            "id": 41,
            "seat_number": "s1",
            "is_booked": false
        },
        "user": "Test5",
        "booking_time": "2026-05-03T14:18:19.735894Z"
    },
    {
        "id": 2,
        "bus": "apsrtc 4 Bobbili Vizag",
        "seat": {
            "id": 42,
            "seat_number": "s2",
            "is_booked": false
        },
        "user": "Test5",
        "booking_time": "2026-05-03T14:18:33.770020Z"
    }
]

note we have to add this in the settings.py file : 

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.AllowAny',
            #   'rest_framework.permissions.IsAuthenticated', ==> opposite to the above one  AllowAny
    ],
     'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework.authentication.TokenAuthentication',
    ],
}

👉 This is a global configuration for DRF
👉 It applies to all your API views by default
🔐 1. DEFAULT_PERMISSION_CLASSES
'rest_framework.permissions.AllowAny'
👉 Meaning:
✔ Anyone can access your APIs
✔ No login required
✔ No restriction
🧪 Example
If you hit:
GET /api/buses/
👉 Even without token:
Response: 200 OK ✅
❗ If you change to:
'rest_framework.permissions.IsAuthenticated'
👉 Now:
GET /api/buses/
Without token:
401 Unauthorized ❌
With token:
200 OK ✅
🔑 2. DEFAULT_AUTHENTICATION_CLASSES
'rest_framework.authentication.TokenAuthentication'
👉 Meaning:
👉 DRF will check for token in request headers
🧪 Example request
GET /api/buses/
Authorization: Token 4870c73bffe49ea833251111b5adf200cce2f444
👉 DRF:
Reads token
Finds user
Sets request.user
🧪 Real use in your code
You wrote:
class BookingView(APIView):
    permission_classes = [IsAuthenticated]
👉 This overrides global setting
👉 So even if global = AllowAny
👉 This API = protected  
🎯 Final understanding
Setting	Meaning
AllowAny	Anyone can access
IsAuthenticated	Login required
TokenAuthentication	Use token system

-------------------------------------------->

note : in the settings.py file 1st TokenAuthentication is checked after the IsAuthenticated is checked ???? 
how request.user.id is came in this line : 
if request.user.id != user_id : 
in view.py file logic 


🧠 Step 1: Your request (client side)
You are sending:
headers = {
  'Authorization': 'Token f51a330bae2082511a40ea234dd7fab494b8ea70'
}

👉 This is the key thing
🧠 Step 2: Request reaches Django
Client → Django Server → DRF
Now DRF checks:
DEFAULT_AUTHENTICATION_CLASSES = [
  'rest_framework.authentication.TokenAuthentication',
]

🔐 Step 3: TokenAuthentication runs
DRF internally does something like:
token = "f51a330bae2082511a40ea234dd7fab494b8ea70"
Then:
Token.objects.get(key=token)
👉 From DB table:
authtoken_token


🧠 Step 4: Token → User mapping
In DB:
token  user_id
f51a33...  8
👉 DRF finds:
user = token.user

🔥 Step 5: DRF sets request.user
Now internally:
request.user = user   # User object
👉 So in your view:
request.user.id  →  8
1. Client sends token
2. DRF reads token (TokenAuthentication)
3. Finds user from DB
4. Sets request.user
5. Your view uses request. User









'rest_framework.permissions.IsAuthenticated'  

“Only logged-in users are allowed to access this API”


1. Authentication  → Who are you?
2. Permission      → Are you allowed?  


✅ Step 2: Permission (IsAuthenticated)
Now DRF checks:
request.user.is_authenticated  
if True : 
request.user.is_authenticated → True
👉 ✅ Access allowed  



🧪 Case 2: No token
👉 DRF sets:
request.user = AnonymousUser
👉 Then:
request.user.is_authenticated → False
👉 ❌ Access denied → 403 Forbidden
--------------------------------------------------------------->
1) /register api testing : 
url : 
method : post
payload : 
response : 
--------------------------------------------------------------->
1) /register api testing : 
url : 
method : post
payload : 
response : 
--------------------------------------------------------------->
1) /register api testing : 
url : 
method : post
payload : 
response : 
--------------------------------------------------------------->
1) /register api testing : 
url : 
method : post
payload : 
response : 

===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>


===============================================================>
👉 A virtual environment is a separate, isolated Python space for one project.  
Your system Python  → global (shared)
venv               → private (project-specific)  
🔥 Why we run apps inside venv?
2️⃣ No version conflicts
Different projects → different versions  
1️⃣ Dependency isolation
Each project has its own packages  
🎯 Why it exists (core problem it solves)
❌ Problem without venv
Imagine you have 2 projects:
Project A → needs Django 3.2
Project B → needs Django 5.0
If you install globally:
pip install django==3.2
pip install django==5.0
👉 One will overwrite the other ❌
👉 Projects will break
✅ Solution with venv
Project A → venv_A → Django 3.2
Project B → venv_B → Django 5.0
👉 No conflict ✅



🧠 1️⃣ Is venv only for Python?
👉 Yes — venv is specific to Python
But the concept (isolation) exists in other languages too:
Language	Tool
Python	venv, virtualenv
JavaScript (Node.js)	node_modules, npm, yarn
Java	Maven / Gradle
Ruby	rbenv, bundler
difference  between termnial , cmd , powershell
djanog vs djanog restframe work  
pip install -r requirements.txt  
pip install django djangorestframework psycopg2-binary
🧠 2️⃣ If I delete venv, do I need to install again?
👉 YES ✅
If you delete:
aenv/   ❌ (deleted)
👉 All installed packages are gone
👉 So you must reinstall:
pip install django djangorestframework psycopg2-binary
🔄 Full flow
Activate:
.\aenv\Scripts\activate
Deactivate:
deactivate
venv = temporary workspace 🏗️
Delete workspace → tools gone  


🧠 1️⃣ Deactivating venv
deactivate
👉 What it does:
Just exits the virtual environment
Your venv folder (aenv/) still exists
All installed packages are still there
✅ Example:
(aenv) → deactivate → normal terminal
👉 Next time:
.\aenv\Scripts\activate
👉 Everything works again (no reinstall needed)
🧠 2️⃣ Deleting venv
rm -r aenv        (Linux/Mac)
rmdir /s aenv     (Windows)
👉 What it does:
Completely removes the aenv folder ❌
All installed packages are gone ❌
👉 Next time:
python -m venv aenv
pip install ...
👉 You must reinstall everything again
===============================================================>
git status → shows current working directory and staging state
git branch → shows and manages branches ,  Current path
git log → shows commit history
The standard git log command shows the commit history for all contributors to the repository, not just your own
🔍 1. git status
💡 What it does
👉 Shows current situation of your project
🧠 Simple intuition
🧍‍♂️ “What am I doing right now?”
🚀 Example
git status
Output:
modified: file1.py
new file: file2.py
👉 Meaning:
file1 changed
file2 is new
🎯 Why we use it
Check before commit
Avoid mistakes
See what is staged / unstaged
🧠 Real-life analogy
📋 Like a to-do checklist
what is done
what is pending
🌳 2. git branch
💡 What it does
👉 Shows all branches and current branch
🧠 Simple intuition
🌳 “Which path am I working on?”
🚀 Example
git branch
Output:
* main
  feature-login
👉 * means current branch
🎯 Why we use it
Know current branch
Switch branches
Manage features
🧠 Real-life analogy
🚧 Like multiple roads in a project
main road (main)
side road (feature)
📜 3. git log
💡 What it does
👉 Shows history of commits
🧠 Simple intuition
🕰️ “What did I do in the past?”
🚀 Example
git log
Output:
commit abc123
Author: Anil
Message: added login feature
🎯 Why we use it
Track changes
Debug issues
See project history
🧠 Real-life analogy
📖 Like a diary/history book
what happened
when it happened

===============================================================>
🔍 If still not working, check this
Run:
git status
If you see:
No commits yet
👉 Then you must commit first.
✅ Step 1: Check branch name
Run:
git branch
👉 Output might be:
* master
🔍 If still not working, check this
Run:
git status
If you see:
No commits yet
👉 Then you must commit first.  
👉 Terminal = interface or window to talk to your computer using commands  
You type commands
Computer executes them
You → command → Terminal → OS → Result
👉 CMD (Command Prompt) = old Windows command-line tool
 👉 PowerShell = advanced version of CMD  
❌ Problem without terminal
Imagine doing everything with mouse:
Create 100 folders → click 100 times 😩
mkdir project\app\templates
mkdir f1 f2 f3

===============================================================>

from rest_framework import serializers
from .models import Bus , Seat
from django.test import TestCase
from django.shortcuts import render 

id = models.AutoField(primary_key = True) 
note : id column is deafultly created in the every model in the django
 # “Automatically set current date & time when object is CREATED”
# “When booking is created → store current time automatically”
booking_time = models.DateTimeField(auto_now_add = True)
==> admin.py : 
from django.contrib import admin
from .models import Bus,Seat
class BusAdmin(admin.ModelAdmin):
    list_display =('bus_name' , 'number','origin','destination')
class SeatAdmin(admin.ModelAdmin):
    list_display =('bus' , 'seat_number' , 'is_booked')
# Register your models here.
admin.site.register(Bus,BusAdmin)
admin.site.register(Seat,SeatAdmin)
==> app.py : 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bus , Seat
@receiver(post_save , sender = Bus)
def create_seats_for_bus(sender , instance , created , **kswargs):
    if created:
        for i in range(1,instance.no_of_seats + 1):
            Seat.objects.create(bus=instance , seat_number = f"s{i}")
