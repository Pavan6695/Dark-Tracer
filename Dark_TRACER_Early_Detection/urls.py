"""Dark_TRACER_Early_Detection URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider
from Dark_TRACER_Early_Detection import settings


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', remoteuser.login, name="login"),

    url(r'^Register1/$', remoteuser.Register1, name="Register1"),

    url(r'^Predict_Detection_Type/$', remoteuser.Predict_Detection_Type,
        name="Predict_Detection_Type"),

    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile,
        name="ViewYourProfile"),

    url(r'^serviceproviderlogin/$',
        serviceprovider.serviceproviderlogin,
        name="serviceproviderlogin"),

    url(r'^View_Remote_Users/$',
        serviceprovider.View_Remote_Users,
        name="View_Remote_Users"),

    url(r'^charts/(?P<chart_type>\w+)$',
        serviceprovider.charts,
        name="charts"),

    url(r'^charts1/(?P<chart_type>\w+)$',
        serviceprovider.charts1,
        name="charts1"),

    url(r'^likeschart/(?P<like_chart>\w+)$',
        serviceprovider.likeschart,
        name="likeschart"),

    url(r'^Find_Malware_Detection_Type_Ratio/$',
        serviceprovider.Find_Malware_Detection_Type_Ratio,
        name="Find_Malware_Detection_Type_Ratio"),

    url(r'^train_model/$',
        serviceprovider.train_model,
        name="train_model"),

    url(r'^Predict_Malware_Detection_Type_Details/$',
        serviceprovider.Predict_Malware_Detection_Type_Details,
        name="Predict_Malware_Detection_Type_Details"),

    url(r'^Download_Predicted_DataSets/$',
        serviceprovider.Download_Predicted_DataSets,
        name="Download_Predicted_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)