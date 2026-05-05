from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect
from .models import MyModel
# Create your views here.


def default_home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Django 🚀</title>
            <style>
                /* Background Styling */
                body {
                    font-family: 'Arial', sans-serif;
                    text-align: center;
                    padding: 50px;
                    background: linear-gradient(135deg, #1e3c72, #2a5298);
                    color: white;
                    margin: 0;
                }
                h1 {
                    font-size: 38px;
                    margin-bottom: 10px;
                    text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                }
                p {
                    font-size: 18px;
                    margin: 10px 0;
                }
                .container {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
                    width: 60%;
                    margin: auto;
                }
                
                /* Grid Layout */
                .links-container {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr); /* 3 per row */
                    gap: 20px;
                    padding: 20px 0;
                }

                /* Button Styling */
                .links a {
                    text-decoration: none;
                    font-size: 18px;
                    color: white;
                    background: linear-gradient(135deg, #ff9966, #ff5e62);
                    padding: 15px;
                    border-radius: 10px;
                    transition: all 0.3s ease-in-out;
                    display: block;
                    text-align: center;
                    font-weight: bold;
                    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
                }

                /* Hover Effects */
                .links a:hover {
                    background: linear-gradient(135deg, #ffcc70, #ff6699);
                    color: #1e3c72;
                    transform: scale(1.1);
                    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.5);
                }

                /* Footer */
                .footer {
                    margin-top: 20px;
                    font-size: 14px;
                    opacity: 0.9;
                }

                /* Responsive Design */
                @media (max-width: 768px) {
                    .links-container {
                        grid-template-columns: repeat(2, 1fr);
                    }
                }
                @media (max-width: 480px) {
                    .links-container {
                        grid-template-columns: repeat(1, 1fr);
                    }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Congratulations! Django is Set Up 🚀</h1>
                <p>Here are the available pages on your site:</p>
                <div class="links-container links">
                    <a href="/admin/">Go to Admin Panel</a>
                    <a href="/hello/">Hello Page</a>
                    <a href="/menuitems/">MenuItems Page</a>
                    <a href="/greet/Divyansh/">Greeting Page</a>
                    <a href="/menuitems1/Pizza/">MenuItems1 Page</a>
                    <a href="/menuitems2/Pizza/">MenuItems2 Page</a>
                    <a href="/err404/">Error 404 Page</a>
                    <a href="/err500/">Error 500 Page</a> 
                    <a href="/queryParameter/?firstParameter=5&secondParameter=3&operation=*">Query Parameter Page</a>  
                    <a href="/user/divyansh/">Regular Expressions Characters Page</a>  
                    <a href="/userNumber/100/">Regular Expressions Numbers Page</a>    
                    <a href="/form1">Form Page</a>    
                    <a href="/destinations">Destinations</a>   
                    <a href="/set_cookie/">Set Cookie</a>   
                    <a href="/get_cookie/">Get Cookie</a>   
                    <a href="/delete_cookie/">Delete Cookie</a>   
                    <a href="/set_session/">Set Session</a>   
                    <a href="/get_session/">Get Session</a>   
                    <a href="/delete_session/">Delete Session</a>
                    <a href="/my_model/">Model List</a>
                    <a href="/my_model/create/">Model Create</a>
                    <a href="/my_model/update">Model Update</a>
                </div>
                <p class="footer">✨ Crafted with ❤️ using Django ✨</p>
            </div>
        </body>
        </html>
    """)


def hello(request):
    m = "divyansh";
    pizza = 251;
    coke = 51;
    burger = 111;
    return HttpResponse(f"""
                        <h2 style='color: blue; font-family:Algerian;'>Hello Django</h2>
                        <h2 style='color: red;'>ITEMS</h2>
                        <h2 style='color: blue;'>Pizza: {pizza}</h2>
                        <h2 style='color: blue;'>Coke: {coke}</h2>
                        <h2 style='color: blue;'>Burger: {burger}</h2>
                        """)


def menuitems(request):
    items={
        'Pizza':'Pizza costs Rs 500',
        'Burger':'Burger costs Rs 25',
        'Noodles':'Noodles costs Rs 40'
    }
    content = '<h1>Menu items</h1>'
    for item,description in items.items():
        content+=f'<li>{item}:{description}</li>'
    return HttpResponse(content)


def greet(request, name):
    
    return HttpResponse(f"Hello {name}! Welcome to our Website.")


def menuitems1(request, dish):
    items={
        'Pizza':'Pizza costs Rs 500',
        'Burger':'Burger costs Rs 25',
        'Noodles':'Noodles costs Rs 40'
    }
    description = items[dish]
    context = {
        'title': 'MenuItems1 Page',
        'content': f"Item: {description}"
    }
    return render(request, 'base_template.html', context)


def menuitems2(request, dish):
    items={
        'Pizza':'Pizza costs Rs 500',
        'Burger':'Burger costs Rs 25',
        'Noodles':'Noodles costs Rs 40'
    }
    if dish in items:
        description = items[dish]
        context = {
            'title': 'MenuItems2 Page',
            'content': f"{dish}: {description}"
        }
        return render(request, 'base_template.html', context)
    else:
        context = {
            'title': 'MenuItems1 Page',
            'content': f"{dish}"+": Item not Found"
        }
        return render(request, 'base_template.html', context)
        return HttpResponse(f"<h2>{dish}</h2>"+"Item not Found")



def queryParameter(request):
    firstParameter = request.GET.get('firstParameter')
    secondParameter = request.GET.get('secondParameter')
    operation = request.GET.get('operation')
    num1 = float(firstParameter)
    num2 = float(secondParameter)
    result = 0

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    loop = 0
    for i in range(int(num1) + 1):
        loop += i

    context = {
        'title': 'Query Parameter Result',
        'content': f"The First parameter is {firstParameter}, Second parameter is {secondParameter} and Operation is '{operation}'. Result = {result}. Loop result sum of firstParameter = {loop}.",
    }

    return render(request, 'base_template.html', context)



def user_profile(request, username):
    context = {
        'title': 'User Profile',
        'content': f"Username: {username}"
    }
    return render(request, 'base_template.html', context)


def user_profile_number(request, number):
    context = {
        'title': 'User Number',
        'content': f"Number: {number}"
    }
    return render(request, 'base_template.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def form1(request):
    if request.method == "POST":
        name = request.POST.get("name", "Guest")
        email = request.POST.get("email", "No email provided")
        contact = request.POST.get("contact", "No contact provided")
        return HttpResponse(f"<h2>Thank You, {name}!</h2><p>Your email: {email}</p><p>Your Contact: {contact}</p>")

    # Generate CSRF token manually
    csrf_token = get_token(request)
    
    return HttpResponse(f"""
        <html>
        <head><title>Simple Form</title>
        </head>
        <body>
            <h2>Contact Form</h2>
            <form method="POST">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email"><br>
                <label for="contact">Phone Number:</label><br>
                <input type="tel" id="contact" name="contact"><br>
                <input type="submit" value="Submit">
            </form>
            <a href="/" class="btn">⬅ Go Back</a>
        </body>
        </html>
    """)

def destinations_list(request):
    return render(request, 'destinations_list.html')

def destination_detail(request, destination_id):
    destinations = {
        1: {'name': 'Paris', 'description': 'Paris, the capital of France, is renowned for its art, fashion, gastronomy, and culture. The city is home to iconic landmarks such as the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum. Stroll along the Seine River, explore charming neighborhoods like Montmartre, and indulge in exquisite French cuisine.'},
        2: {'name': 'New York', 'description': 'New York City, often called "The Big Apple," is the largest city in the USA. It is famous for its skyline dominated by skyscrapers like the Empire State Building and One World Trade Center. Visit Central Park, Times Square, Broadway theaters, and world-class museums. Experience the diverse culture and vibrant energy of this bustling metropolis.'},
        3: {'name': 'Tokyo', 'description': 'Tokyo, the capital of Japan, is a city where modernity meets tradition. Discover the bustling streets of Shibuya and Shinjuku, visit historic temples like Senso-ji, and enjoy the tranquility of the Imperial Palace gardens. Tokyo offers a unique blend of cutting-edge technology, fashion, and rich cultural heritage.'}
    }
    destination = destinations.get(destination_id, {'name': 'Unknown', 'description': 'No description available.'})
    return render(request, 'destination_detail.html', {'destination': destination})

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('my_cookie', 'Django', max_age=3600)  # Cookie expires in 1 hour
    return response

def get_cookie(request):
    cookie_value = request.COOKIES.get('my_cookie', 'Cookie not set')
    return HttpResponse(f"Cookie Value: {cookie_value}")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('my_cookie')
    return response

def set_session(request):
    request.session['my_session_key'] = 'Django_Session'
    return HttpResponse("Session Set")

def get_session(request):
    session_value = request.session.get('my_session_key', 'Session not set')
    return HttpResponse(f"Session Value: {session_value}")

def delete_session(request):
    try:
        del request.session['my_session_key']
    except KeyError:
        pass
    return HttpResponse("Session Deleted")

def my_model_list(request):
    my_models = MyModel.objects.all()
    context = {
        'title': 'My Model List',
        'my_models': my_models
    }
    return render(request, 'my_model_list.html', context)

def my_model_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        MyModel.objects.create(name=name, description=description)
        return redirect('my_model_list')  # Redirect to the list view after creating the model instance
    return render(request, 'my_model_create.html')

def my_model_update(request, id):
    my_model = get_object_or_404(MyModel, id=id)
    if request.method == "POST":
        my_model.name = request.POST.get("name")
        my_model.description = request.POST.get("description")
        my_model.save()
        return redirect('my_model_list')
    return render(request, 'my_model_update.html', {'my_model': my_model})


