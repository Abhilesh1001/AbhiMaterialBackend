from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cus/',include('cusauth.urls')),
    path('mat/',include('material.urls')),
    path('grn/',include('goodreceipt.urls')),
    path('shar/',include('shareholderfund.urls')),
    path('loan/',include('shlord.urls')),
    path('payment/',include('payment.urls'))
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
