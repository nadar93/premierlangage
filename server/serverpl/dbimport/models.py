# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthorizedDomainNames(models.Model):
    domain = models.TextField()

    class Meta:
        managed = False
        db_table = 'authorized_domain_names'

    def __str__(self):
        return self.domain


class Category(models.Model):
    exercises_can_be_attached = models.NullBooleanField()
    wims_en_name = models.CharField(max_length=255)
    parentcategory = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.wims_en_name


class CategoryTranslation(models.Model):
    xwims_language = models.CharField(max_length=5)
    xwims_translation = models.CharField(max_length=255)
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = False
        db_table = 'category_translation'

    def __str__(self):
        return self.xwims_translation


class ClassmanagementCourse(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'classmanagement_course'


class ClassmanagementCourseActivity(models.Model):
    course = models.ForeignKey(ClassmanagementCourse, models.DO_NOTHING)
    activity = models.ForeignKey('PlayexoActivity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'classmanagement_course_activity'
        unique_together = (('course', 'activity'),)


class ClassmanagementCourseStudent(models.Model):
    course = models.ForeignKey(ClassmanagementCourse, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'classmanagement_course_student'
        unique_together = (('course', 'user'),)


class ClassmanagementCourseTeacher(models.Model):
    course = models.ForeignKey(ClassmanagementCourse, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'classmanagement_course_teacher'
        unique_together = (('course', 'user'),)


class Configuration(models.Model):
    serverurl = models.CharField(max_length=255)
    wimsurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'configuration'

    def __str__(self):
        return self.serverurl + ', ' + self.wimsurl


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Exercise(models.Model):
    popularity = models.IntegerField()
    wims_author_email = models.CharField(max_length=255, blank=True, null=True)
    wims_exercise_file_name = models.CharField(max_length=255)
    wims_identifier = models.CharField(max_length=255)
    wims_language = models.CharField(max_length=255, blank=True, null=True)
    wims_title = models.CharField(max_length=255)
    wims_version = models.CharField(max_length=255, blank=True, null=True)
    wims_wording = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise'

    def __str__(self):
        return 'File Name: ' + self.wims_exercise_file_name + ',,,, File Directory: ' + self.wims_identifier


class ExerciseAuthor(models.Model):
    author_name = models.CharField(max_length=255)
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')

    class Meta:
        managed = False
        db_table = 'exercise_author'

    def __str__(self):
        return self.author_name


class ExerciseComment(models.Model):
    complete_date = models.DateField()
    content = models.TextField()
    is_public = models.BooleanField()
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercise_comment'

    def __str__(self):
        return self.complete_date


class ExerciseIsWrong(models.Model):
    error_description = models.TextField()
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercise_is_wrong'

    def __str__(self):
        return self.error_description


class ExercisesCategoryVote(models.Model):
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercises_category_vote'

    def __str__(self):
        return self.id_category


class ExercisesKeywordsVote(models.Model):
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_keyword = models.ForeignKey('Keyword', models.DO_NOTHING, db_column='id_keyword')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercises_keywords_vote'

    def __str__(self):
        return self.id_keyword


class ExercisesLevelsVote(models.Model):
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_level = models.ForeignKey('Levels', models.DO_NOTHING, db_column='id_level')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercises_levels_vote'

    def __str__(self):
        return self.id_level


class ExercisesScoreVote(models.Model):
    score = models.FloatField()
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'exercises_score_vote'

    def __str__(self):
        return self.id_exercise + ', ' + self.score


class FilebrowserDirectory(models.Model):
    name = models.CharField(unique=True, max_length=1024)
    remote = models.CharField(max_length=1024)
    root = models.CharField(max_length=1024)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filebrowser_directory'


class FilebrowserDirectoryReadAuth(models.Model):
    directory = models.ForeignKey(FilebrowserDirectory, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filebrowser_directory_read_auth'
        unique_together = (('directory', 'user'),)


class FilebrowserDirectoryWriteAuth(models.Model):
    directory = models.ForeignKey(FilebrowserDirectory, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filebrowser_directory_write_auth'
        unique_together = (('directory', 'user'),)


class Keyword(models.Model):
    wims_en_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'keyword'

    def __str__(self):
        return self.wims_en_name

class KeywordTranslation(models.Model):
    xwims_language = models.CharField(max_length=5)
    xwims_translation = models.CharField(max_length=255)
    id_keyword = models.ForeignKey(Keyword, models.DO_NOTHING, db_column='id_keyword')

    class Meta:
        managed = False
        db_table = 'keyword_translation'

    def __str__(self):
        return self.xwims_translation


class Levels(models.Model):
    wims_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'levels'

    def __str__(self):
        return self. wims_name


class LoaderPl(models.Model):
    json = models.TextField()
    name = models.CharField(max_length=100)
    rel_path = models.CharField(max_length=360)
    directory = models.ForeignKey(FilebrowserDirectory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_pl'


class LoaderPltp(models.Model):
    sha1 = models.CharField(primary_key=True, max_length=160)
    json = models.TextField()
    name = models.CharField(max_length=50)
    rel_path = models.CharField(max_length=360)
    directory = models.ForeignKey(FilebrowserDirectory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_pltp'


class LoaderPltpPl(models.Model):
    pltp = models.ForeignKey(LoaderPltp, models.DO_NOTHING)
    pl = models.ForeignKey(LoaderPl, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'loader_pltp_pl'
        unique_together = (('pltp', 'pl'),)


class NextCategoryForExercise(models.Model):
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'next_category_for_exercise'

    def __str__(self):
        return 'Exercise id: ' + self.id_exercise + ', categor id: ' + self.id_category


class PlayexoActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    open = models.BooleanField()
    pltp = models.ForeignKey(LoaderPltp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'playexo_activity'


class PlayexoActivitytest(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    pltp = models.ForeignKey(LoaderPltp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'playexo_activitytest'


class PlayexoAnswer(models.Model):
    value = models.TextField()
    seed = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField()
    grade = models.IntegerField()
    pl = models.ForeignKey(LoaderPl, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'playexo_answer'


class PreviousCategoryForExercise(models.Model):
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'previous_category_for_exercise'

    def __str__(self):
        return 'Exercise id: ' + self.id_exercise + ', categor id: ' + self.id_category


class SandboxSandbox(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(primary_key=True, max_length=860)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sandbox_sandbox'


class UserProfileProfile(models.Model):
    student_id = models.IntegerField(unique=True, blank=True, null=True)
    consumer_id = models.IntegerField(unique=True, blank=True, null=True)
    editor_theme = models.IntegerField()
    role = models.IntegerField()
    color_blindness = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'user_profile_profile'


class UserProfileProfileActivity(models.Model):
    profile = models.ForeignKey(UserProfileProfile, models.DO_NOTHING)
    activity = models.ForeignKey(PlayexoActivity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_profile_activity'
        unique_together = (('profile', 'activity'),)


class UserSelectedCategory(models.Model):
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'user_selected_category'


class Users(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    is_banned = models.BooleanField()
    is_certified = models.BooleanField()
    is_registered = models.BooleanField()
    is_root = models.BooleanField()
    language = models.CharField(max_length=5)
    last_name = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    password_salt = models.CharField(max_length=255)
    random_identifier = models.IntegerField()
    registration_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.email


class Worksheet(models.Model):
    creation_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    id_owner = models.ForeignKey(Users, models.DO_NOTHING, db_column='id_owner')

    class Meta:
        managed = False
        db_table = 'worksheet'

    def __str__(self):
        return self.name


class WorksheetExercises(models.Model):
    parameters = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise')
    id_worksheet = models.ForeignKey(Worksheet, models.DO_NOTHING, db_column='id_worksheet')

    class Meta:
        managed = False
        db_table = 'worksheet_exercises'

    def __str__(self):
        return 'Exercise: ' + self.id_exercise + ', Worksheet: ' + self.id_worksheet
