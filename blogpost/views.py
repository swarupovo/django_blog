from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

from blogpost.models import Blogger, Blog, BlogImage, Comments, Share


@csrf_exempt
def user_login(request):
    if request.method == "GET":
        return render(request, 'new_login.html', {'user': request.user})
    else:
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        fetched_user = User.objects.filter(username=username)
        print(fetched_user)
        if fetched_user.exists():
            print("in if block")
            user = authenticate(request, username=username, password=password)
            print(user)

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
                                                          'followers_list': follow_list, 'request':request})
            else:
                return render(request, 'new_login.html', {'messege': 'Incorrect username or password. Please try again.'})
        else:
            return render(request, 'new_login.html', {'messege': 'User Does Not Exists. Please try again.'})



class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login/")

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
                return render(request, "user_add.html", {'message': 'User is Registered Successfully', 'request':request})
        else:
            messages.error(request, "confirmed password is not matched")
            return HttpResponseRedirect("/register/")
    else:
        pass


@csrf_exempt
@login_required(login_url='/admin/login/')
def blog_post(request):
    if request.method == 'GET':
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        return render(request, "blog_post.html", {'usr': request.user, 'img_path': blogger_obj.profile_photo})
    elif request.method == 'POST':
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        content = request.POST['content']
        title = request.POST['title']
        print(request.FILES)

        photo1 = request.FILES['file1'] if 'file1' in request.FILES else None
        photo2 = request.FILES['file2'] if 'file2' in request.FILES else None

        blg_create = Blog.objects.create(title=title, blogger=blogger_obj, content=content)
        blg_create.save()
        if photo1:
            image1 = BlogImage.objects.create(blog=blg_create, images=photo1)
            image1.save()
        if photo2:
            image2 = BlogImage.objects.create(blog=blg_create, images=photo2)
            image2.save()


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
        total_blogger = len(User.objects.all())
        value = 100//total_blogger
        print(value)

        follow_list = []
        for i in blogger_obj.following.all():
            follow_list.append(i.id)
        return render(request, 'dashboard.html',
                      {'all_blogger': all_blogger_data, 'img_path': blogger_obj.profile_photo,
                       'followers_list': follow_list, 'request':request, 'total': value})



@csrf_exempt
@login_required(login_url='/login/')
def blogger_details(request, id=None):
    if request.method == 'GET':
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        return render(request, "user_details.html", {'img_path': blogger_obj.profile_photo})


@csrf_exempt
@login_required(login_url='/login/')
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        print(blogs)
        usr_obj = User.objects.get(username=request.user)
        blogger_obj = Blogger.objects.get(blogger=usr_obj)
        share_obj = Share.objects.all()


        images = BlogImage.objects.all()
        comment_obj = Comments.objects.all()
        return render(request, "blog_list.html", {'blogs': blogs, 'img_path': blogger_obj.profile_photo,
                                                  'blog_images': images, "comments":comment_obj, "share_blogs":share_obj})
    else:
        pass


@csrf_exempt
@login_required(login_url='/login/')
def like_blog(request, blog_id):
    if request.method == "GET":
        print(blog_id)
        blog_obj = Blog.objects.get(id=blog_id)
        blogger_obj = Blogger.objects.get(blogger=request.user)
        try:
            blog_obj.like.add(blogger_obj)
            return HttpResponseRedirect('/blog/list/')
        except Exception as E:
            messages.error(request, "Sorry:you are Not able to like ")
            return HttpResponseRedirect('/blog/list/')
#
# @csrf_exempt
# @login_required
# def settings(request):
#     user = request.user
#
#     try:
#         github_login = user.social_auth.get(provider='github')
#     except UserSocialAuth.DoesNotExist:
#         github_login = None

@csrf_exempt
@login_required(login_url='login')
def comment_blog(request, blog_id):

    if request.method == "POST":
        try:
            blog_obj = Blog.objects.get(id=blog_id)
            blogger_obj = Blogger.objects.get(blogger=request.user)
            comment = request.POST['comment']
            comment_obj = Comments.objects.create(user=blogger_obj, blog=blog_obj, comment=comment)
            comment_obj.save()
            messages.success(request, "Commented Successfully")
            return HttpResponseRedirect('/blog/list/')
        except Exception as E:
            messages.error("Somthing went wrong %s" %E)
            return HttpResponseRedirect('/blog/list/')
    else:
        return HttpResponse("<h2>Method is not allowed</h2>")

@csrf_exempt
@login_required(login_url='login')
def share_blog(request, blog_id):
    if request.method == "GET":
        try:
            blog_obj = Blog.objects.get(id=blog_id)
            blogger_obj = Blogger.objects.get(blogger=request.user)
            share_obj = Share.objects.create(blogger=blogger_obj, blog=blog_obj)
            share_obj.save()
            blog_obj.shared.add(share_obj)
            messages.success(request, "Share the blog is done successfully")
            return HttpResponseRedirect('/blog/list/')

        except Exception as E:
            messages.error(request, "Somthing went wrong %s" %E)
            return HttpResponseRedirect('/blog/list/')

    else:
        return HttpResponse("<h2>Method is not allowed</h2>")


