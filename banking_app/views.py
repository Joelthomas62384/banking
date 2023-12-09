from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import *
from django.contrib.auth.decorators import login_required



@login_required(login_url="register")
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone_number")
        mail_id = request.POST.get("mail_id")
        address = request.POST.get("address")
        district_id = request.POST.get("district")
        branch_name = request.POST.get("branch")
        account_type = request.POST.get("account_type")
        materials_provided = request.POST.getlist("materials_provided")

        try:
            # Use get_object_or_404 to get the Branch instance
            branch = get_object_or_404(Sub_Branches, name=branch_name)

            # Create a UserProfile instance
            user_profile = UserProfile.objects.create(
                name=name,
                dob=dob,
                gender=gender,
                phone_number=phone_number,
                mail_id=mail_id,
                address=address,
                district_id=district_id,
                branch=branch,
                account_type=account_type
            )

            # Save materials provided by the user
            for material_name in materials_provided:
                material = Material.objects.create(name=material_name, user_profile=user_profile)

            messages.success(request, "Accepted")
        except Sub_Branches.DoesNotExist:
            messages.error(request, "Failed: Branch does not exist")

    context = {
        "branches": Branches.objects.all()
    }
    return render(request, "index.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("done this much")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("Login successfull")
            messages.success(request, 'User login successfully!')
            return redirect("home")
    context = {
        "branches":Branches.objects.all()
    }
    return render(request,"login.html",context)

def register_page(request):
    if request.method == "POST":
        # Get user input from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            # Handle the case where the username is taken
            return render(request, "register.html", {'error': 'Username is already taken'})

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'User registered successfully!')

      
        return redirect("login")  
    context = {
        "branches":Branches.objects.all()
    }

    return render(request, "register.html",context)


def get_user(request,username):
    username_exists = User.objects.filter(username=username).exists()
    return JsonResponse({'exists': username_exists})


login_required("register")
def logout_page(request):
    logout(request)
    return redirect("login")

def get_branches(request, district):
    try:
        district = Branches.objects.get(id=district)
        main_branches = Sub_Branches.objects.filter(main_branch=district)
        branches_list = []
        for i in main_branches:
            branches_list.append(i.name)
        return JsonResponse({'branches': branches_list})
    except Branches.DoesNotExist:
        return JsonResponse({'error': 'District not found'}, status=404)