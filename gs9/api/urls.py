from django.urls import path
from api import views

urlpatterns = [

    # path("", views.StudentList.as_view(), name="home"),
    # path("", views.StudentCreate.as_view(), name="home"),
    # path("<int:pk>", views.StudentRetrieve.as_view(), name="home"),
    # path("<int:pk>", views.StudentUpdate.as_view(), name="home"),
    # path("<int:pk>", views.StudentDestroy4.as_view(), name="home"),
    # path("", views.StudentListCreate.as_view(), name="home"),
    # path("<int:pk>", views.StudentRetrieveUpdate.as_view(), name="home"),
    # path("<int:pk>", views.StudentRetrieveDestroy.as_view(), name="home"),
    path("", views.StudentListCreate.as_view(), name="home"),
    path("<int:pk>", views.StudentRetrieveUpdateDestroy.as_view(), name="home"),


    # path('',views.LCStudentAPI.as_view(),name='home'),
    # path('<int:pk>',views.RUDStdentAPI.as_view(),name='post'),

    # path('',views.StudentList.as_view(),name='home'),
    # path('create',views.StudentCreate.as_view(),name='create'),
    # path('retrieve/<int:pk>',views.StudentRetrieve.as_view(),name='retrieve'),
    # path('update/<int:pk>',views.StudentUpdate.as_view(),name='update'),
    # path('destroy/<int:pk>',views.StudentDestroy.as_view(),name='destroy'),
]