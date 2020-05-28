from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate the user using email"""

    def authenticate(self, username=None, password=None):
        """Get instance of the USer based on the Email"""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Used by Django auth system to retrieve user"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None