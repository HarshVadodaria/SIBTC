"""DjangoNewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoNewApp import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_required(views.BoardListView.as_view()), name='home'),
    path('board/new/', login_required(views.NewBoardView.as_view() ), name='new_board'),
    path('board/<int:pk>/',login_required(views.TopicListView.as_view()) , name='board_topic'),
    path('board/<int:pk>/new/',login_required(views.NewTopicView.as_view()) , name='new_topic'),
    # path('board/<int:pk>/new/',login_required(views.new_topic), name='new_topic'),
    path('board/<int:pk>/topic/<int:topic_pk>/delete', login_required(views.DeleteTopicView.as_view()), name='delete_topic'),
    path('board/<int:pk>/topic/<int:topic_pk>/', login_required(views.PostListView.as_view()), name='topic_posts'),
    path('board/<int:pk>/topic/<int:topic_pk>/reply/', login_required(views.ReplyTopicView.as_view()), name='reply_topic'),
    path('board/<int:pk>/topic/<int:topic_pk>/posts/<int:post_pk>/edit/', login_required(views.PostUpdateView.as_view()), name='edit_post'),

    #authentication links provided below......
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
]
