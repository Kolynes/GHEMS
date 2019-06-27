from .shortcuts import json_response

def ensure_signed_in(func):
    def wrapper(request):
        if request.session.get("username"):
            return func(request)
        else:
            return json_response(False, error="You are not signed in!")
    return wrapper