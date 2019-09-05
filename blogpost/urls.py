from django.contrib import admin
from django.urls import path, include
from blogpost.views import user_login, user_register, blogger_list, follow_blogger, unfollow_blogger, blogger_details, \
    blog_list, blog_post, Logout, like_blog, comment_blog

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', user_login, name="admin_login"),
    path('logout/', Logout.as_view(), name="admin_logout"),

    path('register/', user_register, name="register_user"),
    path('blogger/follow/<int:id>/', follow_blogger, name="follow"),
    path('blogger/unfollow/<int:id>/', unfollow_blogger, name="unfollow"),
    path('blogger/list/', blogger_list, name="blogger_list"),
    path('blogger/<int:id>/', blogger_details, name="blogger_details"),
    path('blog/list/', blog_list, name="blog_list"),
    path('post/blog/', blog_post, name="post_blog"),
    path('blog/list/like/<int:blog_id>/', like_blog, name="like_blog"),
    path('comment/<blog_id>/', comment_blog, name="post_comment")
]
