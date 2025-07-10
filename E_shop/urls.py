
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
admin.site.site_header="Speak and Shop Admin Pannel"
admin.site.site_title="SAS Dashboard"
admin.site.index_title="Welcome to Admin Pannel"
urlpatterns = [
    
    path('jet/',include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    #path('accounts/',include('django.contrib.auth.urls'),name='login'),
    #path('accounts/password_change',include('django.contrib.auth.urls'),name='password_change'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
