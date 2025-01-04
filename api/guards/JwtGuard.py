from rest_framework.authentication import BaseAuthentication
from decouple import config
from django.contrib.auth.models import User
import jwt


class CustomUser:
    pass

class JwtGuard(BaseAuthentication):
    def getToken(self,authorizationHeader):
        try:
            return authorizationHeader.split(" ")[1]
        except:
            return False
            
    def authenticate(self,request):
        token = self.getToken(request.headers.get("authorization"))
      
        if token:
            decoded_value = jwt.decode(token,config("JWT_SECRET"),config("JWT_ALGO"))
            user = self.verifyUser(decoded_value['user_id'])
            if user:
                return user,None
        else:
            return None,None

    def verifyUser(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return False


