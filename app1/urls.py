from django.conf.urls import include, url
from django.contrib import admin
from  . import views

urlpatterns = [
	 url(r'^login/$',views.login ),
	 url(r'^files/$',views.get_files),
	 url(r'^listusers/$',views.list_users),
	 url(r'^db1save/$',views.db1save),
	 url(r'^db2save/$',views.db2save),
	 url(r'^app/$',views.app ),

	 url(r'^candidatesave/$',views.candidate_create),
	 url(r'^getbycandidateid/(?P<m_id>[0-9]+)$',views.candidate_create),
	 url(r'^getallcandidates/$',views.candidate_create),

	 url(r'^candidateeducationsave/$',views.candidate_educationprofiles_create),
	 url(r'^getbycandidateeducationid/(?P<m_id>[0-9]+)$',views.candidate_create),
	 url(r'^getallcandidateseducationdetails/$',views.candidate_educationprofiles_create),

	 url(r'^candidateworkprofilesave/$',views.candidate_work_profiles),
	 url(r'^getbycandidateworkprofileid/(?P<m_id>[0-9]+)$',views.candidate_work_profiles),
	 url(r'^getallcandidatesworkprofiles/$',views.candidate_work_profiles),

	 url(r'^candidatelocationsave/$',views.candidate_location_preferences),
	 url(r'^getbycandidatelocationid/(?P<m_id>[0-9]+)$',views.candidate_location_preferences),
	 url(r'^getallcandidateslocations/$',views.candidate_location_preferences),

	 url(r'^attachmentssave/$',views.attachments),
	 url(r'^getbycandidateattachmentsid/(?P<m_id>[0-9]+)$',views.attachments),
	 url(r'^getallcandidatesattachments/$',views.attachments),

	 url(r'^candidatesocialnetworkdetailssave/$',views.candidate_social_network_details),
	 url(r'^candidatesocialnetworkdetailsid/(?P<m_id>[0-9]+)$',views.candidate_social_network_details),
	 url(r'^getallcandidatesocialnetworkdetails/$',views.attachments),


	 url(r'^candidatefilessave/$',views.files),
	 url(r'^getbycandidatefilesid/(?P<m_id>[0-9]+)$',views.files),
	 url(r'^getallcandidatesfiles/$',views.files),

	 url(r'^candidatefulltextssave/$',views.candidate_full_texts),
	 url(r'^getbycandidatefulltextsid/(?P<m_id>[0-9]+)$',views.candidate_full_texts),
	 url(r'^getallcandidatefulltexts/$',views.candidate_full_texts),

	 url(r'^candidatesalaryssave/$',views.candidate_salarys),
	 url(r'^getbycandidatesalarysid/(?P<m_id>[0-9]+)$',views.candidate_salarys),
	 url(r'^getallcandidatesalarys/$',views.candidate_salarys),

	 url(r'^candidatesocialnetworkdetailssave/$',views.candidate_salarys),
	 url(r'^candidatesocialnetworkdetailsid/(?P<m_id>[0-9]+)$',views.candidate_salarys),
	 url(r'^getallcandidatesocialnetworkdetails/$',views.candidate_salarys),
]
