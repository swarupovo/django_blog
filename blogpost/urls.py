from django.contrib import admin
from django.urls import path
from blogpost.views import user_login, user_register, blogger_list, follow_blogger, unfollow_blogger, blogger_details, \
    blog_list, blog_post

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', user_login, name="admin_login"),
    path('register/', user_register, name="register_user"),
    path('blogger/follow/<int:id>/', follow_blogger, name="follow"),
    path('blogger/unfollow/<int:id>/', unfollow_blogger, name="unfollow"),
    path('blogger/list/', blogger_list, name="blogger_list"),
    path('blogger/<int:id>/', blogger_details, name="blogger_details"),
    path('blog/list/', blog_list, name="blog_list"),
    path('post/blog/', blog_post, name="post_blog")
]
