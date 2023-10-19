from django.shortcuts import render

from ninja import Router, Form
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ninja import NinjaAPI

api = NinjaAPI(title="postapi")
@api.post("/register")
def register(request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return {"message": "User registered successfully"}
    except Exception as e:
        return {"error": str(e)}

@api.post("/login")
def user_login(request, email: str = Form(...), password: str = Form(...)):
    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
        return {"message": "Login successful"}
    else:
        return {"error": "Invalid credentials"}

@api.get("/profile")
@login_required
def get_profile(request):
    user = request.user
    return {"username": user.username, "email": user.email}

@api.post("/change-password")
@login_required
def change_password(request, new_password: str = Form(...)):
    user = request.user
    user.set_password(new_password)
    user.save()
    return {"message": "Password changed successfully"}
