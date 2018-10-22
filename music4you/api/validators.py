from django.core.exceptions import ValidationError
"""validation the size of the upload file"""

def validate_file_size(value):
    filesize= value.size
    """"upload size max 20971520 bites --> 20 MB"""
    if filesize > 20971520:
        raise ValidationError("The maximum file size that can be uploaded is 20MB")
    else:
        return value
