from django.contrib.auth.backends import RemoteUserBackend


class DBSRemoteUserBackend(RemoteUserBackend):
    def configure_user(self, request, user):
        user.password = user.username
        user.save()
        return user


backend = DBSRemoteUserBackend()
