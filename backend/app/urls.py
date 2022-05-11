from garpixcms.urls import *  # noqa

urlpatterns = [] + urlpatterns  # noqa

urlpatterns = [
    path('api/v1/', include('api.urls'))
              ] + urlpatterns
