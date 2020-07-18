import django
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path
from appdata.views import (
indexView, appendData, saveData
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", indexView, name = "indexView"),
    # path('get/ajax/validate/formid', checkFormId, name = "validate_formid"),
    path('appendData', appendData, name='appendData'),
    path('saveData', saveData, name='saveData'),
]

# if django.conf.settings.DEBUG:
#     urlpatterns += static (django.conf.settings.STATIC_URL,
#                            document_root=django.conf.settings.STATIC_ROOT)
#     urlpatterns += static (django.conf.settings.MEDIA_URL,
#                            document_root=django.conf.settings.MEDIA_ROOT)