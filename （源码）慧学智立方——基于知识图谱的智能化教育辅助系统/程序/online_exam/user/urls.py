from django.contrib import admin
from django.urls import path, include
from . import views
import flask
from flask import Flask, request, jsonify
import base64
import os
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import hmac
from urllib.parse import urlencode
import traceback
import json
import requests

urlpatterns = [
    path('user', views.user),
    path('login_check', views.login_check),
    path('register',views.register),
    path('change_password', views.change_password),
    path('get_users',views.get_user),
    path('edit_user',views.edit_user),
    path('del_user',views.del_user),
    path('login_out',views.login_out),
    path('personal',views.personal),
    path('modify_password',views.modify_password),
    path('student_face_login',views.student_face_login),
    path('student_sound_login',views.student_sound_login),
    path('upload_zuowen_photo/', views.upload_zuowen_photo, name='upload_zuowen_photo'),
# path('AIcourse/', views.course_list, name='course_list'),
# path('AIcourse/', views.course_list, name='course_list'),





    # path('get_scores',views.get_score ),

]
