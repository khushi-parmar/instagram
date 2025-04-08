import jwt
from django.conf import settings
from django.http import JsonResponse
from functools import wraps
from authentication.models import User  # Adjust this based on your User model

def jwt_required(view_func):
    """
    Decorator to validate JWT token, check user existence, and attach user to request.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization")
        
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return JsonResponse({"message": "You are not logged in! Please log in to get access."}, status=401)

        try:
            decoded_token = jwt.decode(token, settings.SIMPLE_JWT["SIGNING_KEY"], algorithms=["HS256"])
            
            user_id = decoded_token.get("user_id")
            # breakpoint()
            user = User.objects.filter(_id=user_id).first()

            if not user:
                return JsonResponse({"message": "The user belonging to this token does no longer exist."}, status=401)
            # if decoded_token.get("exp")<datetime.utcnow():
            #     return JsonResponse({"message" : "token "})

            # if user.is_deleted:
            #     return JsonResponse({"message": "Your account is deleted. So you cannot log in."}, status=401)

            request.user = user  # Attach user to request
        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "Token has expired. Please log in again."}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"message": "Invalid token. Please log in again."}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
