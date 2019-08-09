from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from blogpost.models import Blogger, Blog


@csrf_exempt
def user_login(request):
    if request.method == "GET":
        return render(request, 'user_login.html', {'user': request.user})
    else:
        username = request.POST['username']
        password = request.POST['password']
        fetched_user = User.objects.filter(username=username)
        if fetched_user.exists():
            print("in if block")
            user = authenticate(request, username=username, password=password)

            if user:

                usr_obj = User.objects.get(username=username)
                all_blogger_data = Blogger.objects.exclude(blogger=usr_obj)
                blogger_obj = Blogger.objects.get(blogger=usr_obj)
                follow_list = []
                for i in blogger_obj.following.all():
                    follow_list.append(i.id)

                print("in 2nd if")
                login(request, user)
                return render(request, 'dashboard.html', {'user': user, 'all_blogger': all_blogger_data,
                                                          'img_path': blogger_obj.profile_photo,
                                                          'followers_list': follow_list})
            else:
                return render(request, 'user_login.html', {'messege': 'Incorrect username or password. Please try again.'})
        else:
            return render(request, 'user_login.html', {'messege': 'User Does Not Exists. Please try again.'})



@csrf_exempt
def user_register(request):
    if request.method == "GET":
        return render(request, 'user_add.html', {'user': ''})
    elif request.method == "POST":
        # blogger = request.user
        full_name = request.POST['full_name']
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                print("in try block")
                User.objects.get(username=username)
                messages.error(request, "The account is alredy exist with this Username {}")
                return HttpResponseRedirect("/register/")
            except:
                print("in except block")
                usr_obj = User.objects.create_user(username=username, email=email, first_name=first_name,
                                                   last_name=last_name)
                usr_obj.set_password(password)
                usr_obj.save()
                phone_no = request.POST['contact']
                post_code = request.POST['postcode']
                blogger_group = request.POST['group']
                photo = request.FILES['file']
                bloger_obj = Blogger.objects.create(blogger=usr_obj, post_code=post_code, phone_no=phone_no,
                                                            blogger_group=blogger_group, profile_photo=photo)
                bloger_obj.save()
                return render(request, "user_add.html", {'message': 'User is Registered Successfully'})
        else:
            messages.error(request, "confirmed password is not matched")
            return HttpResponseRedirect("/register/")
    else:
        pass


@csrf_exempt
@login_required(login_url='/admin/login/')
def blog_post(request):
    if request.method == 'GET':
        return render(request, "blog_post.html", {'usr': request.user})
    elif request.method == 'POST':
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        content = request.POST['content']
        blg_create = Blog.objects.create(blogger=blogger_obj, content=content)
        blg_create.save()
        messages.success(request, "blog_posted Successfully")
        return HttpResponseRedirect('/post/blog/')

    else:
        return HttpResponse(" {} method not allowed".format(request.method))




@csrf_exempt
@login_required(login_url='/login/')
def follow_blogger(request, id=None):
    if request.method == "GET" and id != None:
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        try:

            Blogger.objects.get(id=id)
            blogger_obj.following.add(id)

        except:
            pass
        return HttpResponseRedirect('/blogger/list/')


@csrf_exempt
@login_required(login_url='/login/')
def unfollow_blogger(request, id=None):
    if request.method == "GET" and id != None:
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        try:
            Blogger.objects.get(id=id)
            blogger_obj.following.remove(id)
        except:
            pass
        return HttpResponseRedirect('/blogger/list/')



@csrf_exempt
@login_required(login_url='/login/')
def blogger_list(request):
    if request.method == 'GET':
        usr_obj = User.objects.get(username=request.user)
        all_blogger_data = Blogger.objects.exclude(blogger=usr_obj)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        follow_list = []
        for i in blogger_obj.following.all():
            follow_list.append(i.id)
        return render(request, 'dashboard.html',
                      {'all_blogger': all_blogger_data, 'img_path': blogger_obj.profile_photo,
                       'followers_list': follow_list})



@csrf_exempt
@login_required(login_url='/login/')
def blogger_details(request, id=None):
    if request.method == 'GET':
        return render(request, "user_details.html")


@csrf_exempt
@login_required(login_url='/login/')
def blog_list(request):
    if request.method == "GET":
        return render(request, "blog_list.html")
    else:
        pass