from django.contrib.auth.decorators import login_required


def login_required_view(view):
    return login_required(view, login_url="admin:login")
