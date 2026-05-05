from django.shortcuts import render, get_object_or_404
from .forms import MyForm
from django.http import HttpResponse
from .models import Product
from django.middleware.csrf import get_token


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_detail.html', {'product': product})

# def handler404(request, exception):
#     return render(request, '404.html', status=404)

# def handler500(request):
#     return render(request, '500.html', status=500)

# def home(request):
#     a = "Divyansh"
#     return HttpResponse(f"""
#         <html>
#             <head>
#                 <title>Welcome</title>
#                 <style>
#                     body {{
#                         font-family: Arial, sans-serif;
#                         background-color: #f4f4f4;
#                         text-align: center;
#                         margin-top: 50px;
#                     }}
#                     h1 {{
#                         color: red;
#                     }}
#                 </style>
#             </head>
#             <body>
#                 <h1>Hello, world!</h1>
#                 <h1>Welcome! {a}</h1>
#                 <p>It's my Django app.</p>
#             </body>
#         </html>
#     """)

# def form1(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "Guest")
#         email = request.POST.get("email", "No email provided")
#         return HttpResponse(f"<h2>Thank You, {name}!</h2><p>Your email: {email}</p><p>Your Contact: {email}</p>")

#     # Generate CSRF token manually
#     csrf_token = get_token(request)
    
#     return HttpResponse(f"""
#         <html>
#         <head><title>Simple Form</title></head>
#         <body>
#             <h2>Contact Form</h2>
#             <form method="POST">
#                 <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 <label for="name">Name:</label><br>
#                 <input type="text" id="name" name="name"><br>
#                 <label for="email">Email:</label><br>
#                 <input type="email" id="email" name="email"><br>
#                 <label for="contact">Phone Number:</label><br>
#                 <input type="number" id="contact" name="contact"><br>
#                 <input type="submit" value="Submit">
#             </form>
#         </body>
#         </html>
#     """)

# def destinations_list(request):
#     return render(request, 'destinations_list.html')

# def destination_detail(request, destination_id):
#     destinations = {
#         1: {'name': 'Paris', 'description': 'Paris, the capital of France, is renowned for its art, fashion, gastronomy, and culture. The city is home to iconic landmarks such as the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum. Stroll along the Seine River, explore charming neighborhoods like Montmartre, and indulge in exquisite French cuisine.'},
#         2: {'name': 'New York', 'description': 'New York City, often called "The Big Apple," is the largest city in the USA. It is famous for its skyline dominated by skyscrapers like the Empire State Building and One World Trade Center. Visit Central Park, Times Square, Broadway theaters, and world-class museums. Experience the diverse culture and vibrant energy of this bustling metropolis.'},
#         3: {'name': 'Tokyo', 'description': 'Tokyo, the capital of Japan, is a city where modernity meets tradition. Discover the bustling streets of Shibuya and Shinjuku, visit historic temples like Senso-ji, and enjoy the tranquility of the Imperial Palace gardens. Tokyo offers a unique blend of cutting-edge technology, fashion, and rich cultural heritage.'}
#     }
#     destination = destinations.get(destination_id, {'name': 'Unknown', 'description': 'No description available.'})
#     return render(request, 'destination_detail.html', {'destination': destination})

