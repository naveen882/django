from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import fields


#class UserProfile(models.Model):
#	user = models.ForeignKey(User)
#	created_date = models.DateTimeField(auto_now_add=True, db_index=True)
#	first_name = models.CharField(max_length=255)
#	last_name = models.CharField(max_length=255)
#	role = models.CharField(max_length=255)
#
#	class Meta:
#		db_table='up'
#		app_label = 'app1'



class Candidates(models.Model):
	version = models.IntegerField()
	current_employer_id = models.IntegerField(null=True)
	current_employer_text = models.CharField(max_length=100,null=True)
	current_location_id = models.IntegerField(null=True)
	date_of_birth = models.DateTimeField(null=True)
	final_degree_id = models.IntegerField(null=True)
	final_degree_text = models.CharField(max_length=100,null=True)
	final_department_id = models.IntegerField(null=True)
	final_department_text = models.CharField(max_length=70,null=True)
	gender = models.IntegerField(null=True)
	is_fresher = models.NullBooleanField() #models.SmallIntegerField(null=True) is small Int
	current_location_text = models.CharField(max_length=75,null=True)
	marital_status = models.IntegerField(null=True)
	opening_status_id = models.IntegerField(null=True)
	status_id = models.IntegerField(null=True)
	total_experience = models.IntegerField(null=True)
	notes = models.TextField()
	relevant_experience = models.IntegerField(null=True)
	expertise_id1 = models.IntegerField(null=True)
	expertise_text = models.CharField(max_length=50,null=True)
	expertise_id2 = models.IntegerField(null=True)
	hierarchy_id = models.IntegerField(null=True)
	hierarchy_text = models.CharField(max_length=50,null=True)
	university_id = models.IntegerField(null=True)
	university_text = models.CharField(max_length=100,null=True)
	email1 = models.CharField(max_length=100,null=True)
	email2 = models.CharField(max_length=100,null=True)
	first_name = models.CharField(max_length=75,null=True)
	importance = models.IntegerField()
	last_name = models.CharField(max_length=75,null=True)
	middle_name = models.CharField(max_length=75,null=True)
	mobile1 = models.CharField(max_length=75,null=True)
	phone_office = models.CharField(max_length=100,null=True)
	phone_residence = models.CharField(max_length=100,null=True)
	sensitivity = models.IntegerField(null=True)
	salutation = models.IntegerField(null=True)
	college_id = models.IntegerField(null=True)
	college_text = models.CharField(max_length=255,null=True)
	resume_grade_id = models.IntegerField(null=True)
	no_of_attachments = models.IntegerField()
	experience_updated_on = models.DateTimeField(null=True)
	technology_text = models.TextField()
	current_ctc = models.CharField(max_length=255,null=True)
	user_id = models.IntegerField(null=True)
	candidate_name = models.CharField(max_length=255,null=True)
	brownie_point_total = models.IntegerField(null=True)
	sourcer = models.IntegerField(null=True)
	sourcer_log = models.CharField(max_length=2000,null=True)
	crm_status_date = models.DateTimeField(null=True)
	address1 = models.CharField(max_length=255,null=True)
	address2 = models.CharField(max_length=255,null=True)
	address3 = models.CharField(max_length=255,null=True)
	notice_period = models.IntegerField(null=True)
	skill_id = models.IntegerField(null=True)
	current_source_id = models.IntegerField(null=True)
	sourcer_modified_date = models.DateTimeField(null=True)
	tenant_id = models.IntegerField(null=True)
	published_on = models.DateTimeField(null=True)
	published_by = models.IntegerField(null=True)
	is_active = models.NullBooleanField(default=1)
	is_draft = models.NullBooleanField()
	is_archived = models.NullBooleanField()
	true_false2 = models.NullBooleanField()
	true_false1 = models.NullBooleanField()
	integer2 = models.IntegerField(null=True)
	integer1 = models.IntegerField(null=True)
	text4 = models.CharField(max_length=1000,null=True)
	text3 = models.CharField(max_length=1000,null=True)
	text2 = models.CharField(max_length=1000,null=True)
	text1 = models.CharField(max_length=1000,null=True)
	is_alive = models.BooleanField(default=1)
	created_by = models.IntegerField()
	created_on = models.DateTimeField( auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField(default=0)
	guid = models.CharField(max_length=40)
	candidateoriginalsourceinfo_id = models.IntegerField(null=True)
	candidatepreference_id = models.IntegerField(null=True)
	candidatesourceinfo_id = models.IntegerField(null=True)
	percentage_or_cgp = models.FloatField(null=True) ##pending double DEFAULT NULL,
	is_percentage = models.NullBooleanField()
	original_candidate_id = models.IntegerField(null=True)
	pan_card = models.CharField(max_length=20,null=True)
	passport = models.CharField(max_length=10,null=True)
	percentage_of_duplication = models.IntegerField(null=True)
	candidateresumefulltext_id = models.IntegerField(null=True)
	candidatefulltext_id = models.IntegerField(null=True)
	country_code = models.CharField(max_length=10,null=True)
	bulk_custom_field_string = models.TextField()#longtext,
	is_black_listed = models.BooleanField(default=0)
	duplicate_or_blacklist_comment = models.CharField(max_length=5000,null=True)
	original_source_info_modified = models.DateTimeField(null=True)
	duplication_comment = models.CharField(max_length=5000,null=True)
	is_set_resume_status_to_crm = models.NullBooleanField()
	is_rejected = models.NullBooleanField()
	is_partial_duplicate = models.BooleanField(default=0)
	black_list_mode = models.IntegerField(default=0)
	soft_delete_type = models.IntegerField(default=0)
	candidate_photo_file_id = models.IntegerField(null=True)
	is_hirepro_vendor_candidate = models.NullBooleanField()
	is_utilized = models.BooleanField()
	audio_file_name = models.CharField(max_length=255,null=True)
	text5 = models.CharField(max_length=50,null=True)
	integer3 = models.IntegerField(null=True)
	integer4 = models.IntegerField(null=True)
	integer5 = models.IntegerField(null=True)
	password = models.CharField(max_length=255,null=True)
	owner_id = models.IntegerField(null=True)
	usn = models.CharField(max_length=45,null=True)
	country = models.IntegerField(null=True)
	nationality = models.IntegerField(null=True)
	familydetail_id = models.IntegerField(null=True)
	type_of_candidate = models.IntegerField(default=0)
	original_source_id = models.IntegerField(default=0)
	source_modified_by = models.IntegerField(null=True)
	source_modified_on = models.DateTimeField(null=True)
	originated_from = models.IntegerField(default=0)
	level_id = models.IntegerField(null=True)
	role_Id = models.IntegerField(null=True)
	mentor = models.IntegerField(null=True)
	buddies = models.CharField(max_length=100,null=True)
	bu_id = models.IntegerField(null=True)
	current_activity = models.IntegerField(null=True)
	activity_status = models.IntegerField(null=True)
	candidate_user_id = models.IntegerField(null=True)
	candidatestaffingprofile_id = models.IntegerField(null=True)
	current_experience = models.IntegerField(null=True)
	bpo_experience = models.IntegerField(null=True)
	date_custom_field1 = models.DateTimeField(null=True)
	date_custom_field2 = models.DateTimeField(null=True)
	text_area1 = models.CharField(max_length=3000,null=True)
	text_area2 = models.CharField(max_length=3000,null=True)
	text_area3 = models.CharField(max_length=3000,null=True)
	text_area4 = models.CharField(max_length=3000,null=True)
	candidate_photo_path = models.CharField(max_length=500,null=True)
	uuid = models.CharField(max_length=32,null=True)
  #PRIMARY KEY (`id`),
  #KEY `candidatefulltext_id` (`candidatefulltext_id`),
  #KEY `email1` (`email1`),
  #KEY `tenant_id` (`tenant_id`)
#) #ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 |

	class Meta:
		db_table='candidates'

class Candidate_education_profiles(models.Model):
	college_id = models.IntegerField(null=True)
	college_text = models.CharField(max_length=100,null=True)
	degree_id = models.IntegerField(null=True)
	degree_text = models.CharField(max_length=100,null=True)
	degree_type_id = models.IntegerField(null=True)
	degree_type_text = models.CharField(max_length=50,null=True)
	end_year = models.IntegerField(null=True)
	is_final = models.NullBooleanField(null=True)
	percentage = models.DecimalField(max_digits=3, decimal_places=2,null=True)
	start_year = models.IntegerField(null=True)
	university_id = models.IntegerField(null=True)
	university_text = models.CharField(max_length=100,null=True)
	start_month = models.IntegerField(null=True)
	end_month = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add = True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	#candidate_id = models.IntegerField(null=True)
	education_type = models.IntegerField(default=1)
	is_percentage = models.NullBooleanField()
	institute_type_id = models.IntegerField(null=True)
	candidate = models.ForeignKey(Candidates,null=True)
	#PRIMARY KEY (`id`),
	#KEY `candidate_id` (`candidate_id`)
	#) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1 |


	class Meta:
		db_table='candidate_education_profiles'


class Candidate_work_profiles(models.Model):
	deisignation_id = models.IntegerField(null=True)
	designation_text = models.CharField(max_length=75,null=True)
	employer_id = models.IntegerField(null=True)
	employer_text = models.CharField(max_length=100,null=True)
	location_id = models.IntegerField(null=True)
	location_text = models.CharField(max_length=75,null=True)
	reason_for_leaving = models.TextField(null=True)
	yearly_salary = models.IntegerField(null=True)
	from_month = models.IntegerField(null=True)
	to_month = models.IntegerField(null=True)
	from_year = models.IntegerField(null=True)
	to_year = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	#candidate_id = models.IntegerField(null=True)
	candidate = models.ForeignKey(Candidates,null=True) #db_index=True
	bulk_custom_field_string = models.TextField(null=False)# longtext,
	is_latest = models.NullBooleanField()
	industry = models.IntegerField(null=True)
	expertise = models.IntegerField(null=True)
	sub_expertise = models.IntegerField(null=True)
	sub_expertise2 = models.IntegerField(null=True)
	title = models.CharField(max_length=55,null=True)
	#PRIMARY KEY (`id`),
	#KEY `candidate_id` (`candidate_id`)
	#) ENGINE=InnoDB DEFAULT CHARSET=latin1 |

	class Meta:
		db_table = 'candidate_work_profiles'

class Candidate_location_preferences(models.Model):
	location_id = models.IntegerField()
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	candidatepreference_id = models.IntegerField(null=True)
	location_text = models.CharField(max_length=50,null=True)

	class Meta:
		db_table = 'candidate_location_preferences'


class Candidate_preferences(models.Model):
	#desired_salary_from = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	#desired_salary_to = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	desired_salary_from = models.FloatField(null=True)
	desired_salary_to = models.FloatField(null=True)
	desired_title_id = models.IntegerField(null=True)
	desired_title_text = models.CharField(max_length=50,null=True)
	job_category_id1 = models.IntegerField(null=True)
	job_category_text = models.CharField(max_length=50,null=True)
	notes = models.CharField(max_length=255,null=True)
	other_compensation = models.CharField(max_length=255,null=True)
	is_willing_to_relocate = models.NullBooleanField()
	job_category_id2 = models.IntegerField(null=True)
	job_category_id3 = models.IntegerField(null=True)
	job_category_id4 = models.IntegerField(null=True)
	company_type_id = models.IntegerField(null=True)
	company_type_text = models.CharField(max_length=50,null=True)
	company_sub_type_id = models.IntegerField(null=True)
	company_sub_type_text = models.CharField(max_length=50,null=True)
	notice_period = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)

	class Meta:
		db_table = 'candidate_preferences'

class Attachments(models.Model):
	version = models.IntegerField()
	attachment_type_id = models.IntegerField(null=True)
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)
	source_item_type = models.CharField(max_length=255,null=True)
	source_item_id = models.IntegerField(null=True)
	target_item_type = models.CharField(max_length=255,null=True)
	target_item_id = models.IntegerField(null=True)#file id

	class Meta:
		db_table = 'attachments'

class Files(models.Model):
	version = models.IntegerField()
	title = models.TextField()
	original_file_name = models.TextField()
	file_type_id = models.IntegerField(null=True)
	file_type_text = models.CharField(max_length=255,null=True)
	file_format_id = models.IntegerField(null=True)
	file_size = models.BigIntegerField()
	is_compressed = models.NullBooleanField()
	is_encrypted = models.NullBooleanField()
	target_path = models.TextField()
	file_created_on = models.DateTimeField(auto_now_add=True)
	file_modified_on = models.DateTimeField(auto_now_add=True)
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)
	filecontent_id = models.IntegerField(null=True)

	class Meta:
		db_table = 'files'

class Candidate_full_texts(models.Model):
	candidate_resume_full_text = models.TextField(null=True)
	candidate_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	tenant_id = models.IntegerField(null=True)
	rank = models.IntegerField(null=True)

	class Meta:
		db_table = 'candidate_full_texts'

	def clean(self):
		if (self.created_by is None):
			raise ValidationError('Validation Error')

class Candidate_salarys(models.Model):
	date_created = models.DateTimeField(null=True)
	company_name = models.CharField(max_length=100,null=True)
	basic = models.FloatField(null=True)
	flexible = models.FloatField(null=True)
	pf = models.FloatField(null=True)
	performance_bonus = models.FloatField(null=True)
	gratuity = models.FloatField(null=True)
	super_annuation = models.FloatField(null=True)
	insurance = models.FloatField(null=True)
	medical = models.FloatField(null=True)
	stocks = models.CharField(max_length=255,null=True)
	comments = models.CharField(max_length=255,null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	candidate_id = models.IntegerField(null=True)
	offer_id = models.IntegerField(null=True)
	currency = models.IntegerField(null=True)

	class Meta:
		db_table = 'candidate_salarys'

class Candidate_social_network_details(models.Model):
	version = models.IntegerField()
	face_book_link = models.CharField(max_length=255,null=True)
	face_book_details = models.CharField(max_length=255,null=True)
	twitter_link = models.CharField(max_length=255,null=True)
	twitter_details = models.CharField(max_length=255,null=True)
	linked_in_link = models.CharField(max_length=255,null=True)
	linked_in_details = models.CharField(max_length=255,null=True)
	candidate_id = models.IntegerField()
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)

	class Meta:
		db_table = 'candidate_social_network_details'
