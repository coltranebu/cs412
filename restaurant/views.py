# restaurant/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-17
# This file is responsible for the python calculations run before each page is
# loaded. It creates item lists and calculates prices, among other
# responsibilities.

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Used to generate a random Daily Special and a random time of readiness
import random
# Used in the process of generating a time of readiness
import time

def generate_special():
    """Randomly return a string of one of three Daily Specials."""
    x = random.randint(0,2)
    # Spaghetti code to select one of the Specials
    if x == 0:
        return "Blenheim Mineral Springs Water"
    elif x == 1:
        return "God's Acre Healing Springs Water"
    else:
        return "Coker Spring Water"

# --------- VIEWS ---------

def main(request):
    """Return a static homepage."""
    template_name = "restaurant/main.html"
    return render(request, template_name)

def order(request):
    """Return an order page with a random Daily Special."""
    template_name = "restaurant/order.html"
    context = {
        "daily_special": generate_special(),
    }
    return render(request, template_name, context)

def confirmation(request):
    """Return a page that either confirms an order or provides an error
    signifying incompletion of the form."""
    template_name = "restaurant/confirmation.html"

    # Only return confirmation page if order placed
    if request.POST:

        # Empty order list to be filled later
        order = []
        # Cost initialized to zero before being added to
        cost = 0.00
        # Set instructions, name, phone #, and email to the values
        # input in the form
        special_instructions = request.POST['special_instructions']
        customer_name = request.POST['customer_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']

        # Error handling variables:
        # True if no items purchased
        no_order = False
        # True if not all three contact forms are filled out
        no_info = False

        # Generates a time between 30 and 60 minutes from the present
        time_ready = time.asctime(time.localtime((time.time()) + \
            random.randint(1800, 3600)))

        # If hot_purchase is checked, then add it, followed by its quantity
        # parentheses, to order. Also increment cost
        if request.POST.get('hot_purchase', False) == 'hot_purchase':
            order.append("Old #3 Hot Ginger Ale")
            # Spaghetti code checking for the quantity specified in the form
            if request.POST['hot_qty'] == '1':
                order[len(order) - 1] += ' (1)'
                cost += 3.00
            elif request.POST['hot_qty'] == '6':
                order[len(order) - 1] += ' (6)'
                cost += 12.00
            elif request.POST['hot_qty'] == '12':
                order[len(order) - 1] += ' (12)'
                cost += 22.00
            elif request.POST['hot_qty'] == '24':
                order[len(order) - 1] += ' (24)'
                cost += 41.00
        
        # If mild_purchase is checked, then add it, followed by its quantity
        # parentheses, to order. Also increment cost
        if request.POST.get('mild_purchase', False) == 'mild_purchase':
            order.append("#5 Not As Hot Ginger Ale")
            # Spaghetti code checking for the quantity specified in the form
            if request.POST['mild_qty'] == '1':
                order[len(order) - 1] += ' (1)'
                cost += 3.00
            elif request.POST['mild_qty'] == '6':
                order[len(order) - 1] += ' (6)'
                cost += 12.00
            elif request.POST['mild_qty'] == '12':
                order[len(order) - 1] += ' (12)'
                cost += 22.00
            elif request.POST['mild_qty'] == '24':
                order[len(order) - 1] += ' (24)'
                cost += 41.00

        # If diet_purchase is checked, then add it, followed by its quantity
        # parentheses, to order. Also increment cost
        if request.POST.get('diet_purchase', False) == 'diet_purchase':
            order.append("#9 Diet Ginger Ale")
            # Spaghetti code checking for the quantity specified in the form
            if request.POST['diet_qty'] == '1':
                order[len(order) - 1] += ' (1)'
                cost += 3.00
            elif request.POST['diet_qty'] == '6':
                order[len(order) - 1] += ' (6)'
                cost += 12.00
            elif request.POST['diet_qty'] == '12':
                order[len(order) - 1] += ' (12)'
                cost += 22.00
            elif request.POST['diet_qty'] == '24':
                order[len(order) - 1] += ' (24)'
                cost += 41.00
        
        # Check, for each possible Daily Special, to see if it is checked for
        # purchase. If it is being purchased, add it to order and increment
        # cost by 2.00
        if request.POST.get('special_purchase', False) == \
            "Blenheim Mineral Springs Water":
            order.append("Blenheim Mineral Springs Water")
            cost += 2.00
        elif request.POST.get('special_purchase', False) == \
            "God's Acre Healing Springs Water":
            order.append("God's Acre Healing Springs Water")
            cost += 2.00
        elif request.POST.get('special_purchase', False) == \
            "Coker Spring Water":
            order.append("Coker Spring Water")
            cost += 2.00
        
        # If no Blenheim is purchased and a Daily Special is not purchased, set
        # no_order to true
        if (request.POST.get('hot_purchase', False) != 'hot_purchase'
            and request.POST.get('mild_purchase', False) != 'mild_purchase'
            and request.POST.get('diet_purchase', False) != 'diet_purchase'
            and request.POST.get('special_purchase', False) != \
            "Blenheim Mineral Springs Water"
            and request.POST.get('special_purchase', False) != \
            "God's Acre Healing Springs Water"
            and request.POST.get('special_purchase', False) != \
            "Coker Spring Water"):
            no_order = True

        # If not all contact information is given, set no_info to true
        if customer_name == "" or phone_number == "" or email_address == "":
            no_info = True

        # Set context
        context = {
            'order': order,
            'cost': cost,
            'special_instructions': special_instructions,
            'customer_name': customer_name,
            'phone_number': phone_number,
            'email_address': email_address,
            'no_order': no_order,
            'no_info': no_info,
            'time_ready': time_ready
        }
        return render(request, template_name=template_name, context=context)

    # Redirect to order form if no form had just been submitted
    else:
        return redirect('order')
