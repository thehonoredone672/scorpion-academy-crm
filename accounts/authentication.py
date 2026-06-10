import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions


class StatelessMongoUser:
    """
    Memory-resident authenticated user object.
    """

    def __init__(self, user_id, role, branch_id=None):
        self.id = user_id
        self.role = role
        self.branch_id = branch_id
        self.is_authenticated = True


class MongoJWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        # Allow public endpoints like login/register
        if not auth_header:
            return None

        try:
            header_parts = auth_header.split()

            if len(header_parts) != 2:
                raise exceptions.AuthenticationFailed(
                    "Invalid Authorization header format."
                )

            if header_parts[0].lower() != "bearer":
                raise exceptions.AuthenticationFailed(
                    "Authorization header must start with Bearer."
                )

            token = header_parts[1]

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                "Access token has expired."
            )

        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(
                "Invalid token."
            )

        user_id = payload.get("user_id")
        role = payload.get("role")
        branch_id = payload.get("branch_id")

        if not user_id:
            raise exceptions.AuthenticationFailed(
                "Token missing user_id."
            )

        if not role:
            raise exceptions.AuthenticationFailed(
                "Token missing role."
            )

        user = StatelessMongoUser(
            user_id=user_id,
            role=role,
            branch_id=branch_id
        )

        return (user, token)
