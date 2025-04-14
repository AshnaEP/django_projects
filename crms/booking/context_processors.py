def user_data(request):
    u=request.user
    name = ""
    email = ""
    if request.user.is_authenticated:
        name = u.username
        email = u.email
    return {'username':name,'user_email':email}