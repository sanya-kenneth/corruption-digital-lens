"""corruption_lens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import url
from django.conf.urls.static import static

from app.views import employee_survey, home, act_detail, public_survey, register_like, report_incident, feedback, interplay_like, system_survey, thank_you, thanks
from corruption_lens import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', home, name='home'),
    path('corruption-form/acts/<int:corruption_id>',
         act_detail, name='act_detail'),
    path('act/like/<int:act_id>/<int:corruption_id>',
         register_like, name='register-like'),
    path('interplay/like/<int:interplay_id>/<int:corruption_id>',
         interplay_like, name='interplay-like'),
    path('incident/report', report_incident, name='report-incident'),
    path('feedback', feedback, name='feedback'),
    # path('questionnaire/survey/initial/', SurveyView.as_view(), name='initial_survey'),
    # path('questionnaire/survey/post/', SurveyView.as_view(), {'is_post': True}, name='post_survey'),
    path('questionnaire/thank_you/', thank_you, name='thank_you'),

    path('questionnaire/system/', system_survey, name='system_survey'),
    path('questionnaire/public/', public_survey, name='public_survey'),
    path('questionnaire/employee/', employee_survey, name='employee_survey'),
    path('questionnaire/thanks/', thanks, name='thanks'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Corruption Digital Lens"
