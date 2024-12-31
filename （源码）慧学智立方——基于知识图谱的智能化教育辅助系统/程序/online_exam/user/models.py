from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.
# 用户基本信息
class UserTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', default='', max_length=50)
    password = models.CharField('密码', default='123', max_length=50)
    phone = models.CharField('手机号', default='', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    role = models.IntegerField('角色', default=3)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'

class Student(models.Model):
    # user = models.OneToOneField(UserTable, on_delete=models.CASCADE)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100, default='', verbose_name='学号')
    name = models.CharField(max_length=100, default='', verbose_name='姓名')
    password = models.CharField(max_length=100, default='', verbose_name='密码')
    gender = models.CharField(max_length=100, default='', verbose_name='性别')
    phone = models.CharField(max_length=11, default='', null=True, blank=True, verbose_name='电话号码')
    age = models.IntegerField(default=18, verbose_name='年龄')
    image = models.CharField( default='/static/image/default.png', max_length=200, verbose_name='头像')
    role = models.IntegerField('角色', default=1)
    # base_data = models.JSONField(default=dict, blank=True)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'


# 科目信息
class Subject(models.Model):
    subject_name = models.CharField(max_length=20, default='', verbose_name='科目名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '科目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject_name

    class Meta:
        db_table = 'subject'

# 老师信息
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='', verbose_name='老师姓名')
    number = models.CharField(max_length=100, default='', verbose_name='工号')
    password = models.CharField(max_length=100, default='', verbose_name='密码')
    phone = models.CharField(max_length=11, default='', null=True, blank=True, verbose_name='电话号码')
    age = models.IntegerField(default=18, verbose_name='年龄')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='所属科目')
    teacher_school = models.CharField(max_length=100, default='', verbose_name='老师所在学校')
    role = models.IntegerField('角色', default=2)
    class Meta:
        verbose_name = '老师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'










# class Course(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image_url = models.URLField()
#     video_url = models.URLField()
#     instructor = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'course'





