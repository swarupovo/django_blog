from django.core.exceptions import ValidationError

# from blogpost.models import BlogImage
# from .models import BlogImage


def max_image_cheque(value):
    # pass
    from blogpost.models import BlogImage
    img_number = BlogImage.objects.filter(blog=value)
    if len(img_number) > 1:
        return ValidationError("Value must be grater than 4")
    else:
        return value