from django.contrib import admin
from django.urls import path
import studenti.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('student/add', studenti.views.skats_forma),
    path('', studenti.views.skats_visi_studenti),
    path('student/<int:student_id>', studenti.views.skats_viens_students, name='viens_students'),

]
