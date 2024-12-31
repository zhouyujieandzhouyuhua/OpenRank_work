import os
import django

from datetime import datetime
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db import models

from user.models import Student

from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom


# from .models import Comment

# Create your models here.


# 题库表
class Question(models.Model):
    id = models.AutoField('序号',primary_key=True)
    course = models.IntegerField(verbose_name='科目',null=True)
    title = models.TextField('题目')
    question_type = models.CharField('试题类型',default='单选题',max_length=10)
    owner = models.CharField('创建人',default='admin',max_length=20)
    a = models.CharField('A选项',max_length=40,null=True)
    b = models.CharField('B选项',max_length=40,null=True)
    c = models.CharField('C选项',max_length=40,null=True)
    d = models.CharField('D选项',max_length=40,null=True)
    answer = models.CharField('答案',default='',max_length=1000)
    difficulty = models.CharField('难度',default="一般",max_length=10)
    score = models.IntegerField('分值')
    last_modify_time = models.DateTimeField('最后更新时间', auto_now_add=True)
    class Meta:
        db_table = 'question'


# 试卷表
class TestPaper(models.Model):
    id = models.AutoField('序号',primary_key=True)
    title = models.CharField('试卷名称',max_length=40,unique=True)
    pid = models.CharField('题目',max_length=500,default='')
    answer = models.CharField('答案',max_length=500,default='')
    owner = models.CharField(default='',max_length=100,verbose_name='出卷人')
    course = models.CharField(default='',max_length=100,verbose_name='科目')
    time = models.IntegerField('考试时长',help_text='单位是分钟')
    exam_time = models.DateTimeField('出卷时间', auto_now_add=True)
    class Meta:
        db_table = 'test_paper'


# # 学生成绩表
class Record(models.Model):
    id = models.AutoField('序号',primary_key=True)
    xuehao = models.IntegerField(verbose_name='学号')
    name = models.CharField(default='',max_length=50)
    grade = models.FloatField('成绩')
    test_paper_id = models.IntegerField('试卷ID')
    answer = models.CharField('考生答案',default='',max_length=500)
    exam_time = models.DateTimeField('考试时间', auto_now_add=True)
    class Meta:
        db_table = 'record'



class Score(models.Model):

    student_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    total_score = models.IntegerField()
    subject = models.CharField(max_length=20)
    time = models.DateTimeField()
    # question_1 = models.IntegerField()
    question_1 = models.IntegerField()
    question_2 = models.IntegerField()
    question_3 = models.IntegerField()
    question_4 = models.IntegerField()
    question_5 = models.IntegerField()
    question_6 = models.IntegerField()
    question_7 = models.IntegerField()
    question_8 = models.IntegerField()
    question_9 = models.IntegerField()
    question_10 = models.IntegerField()
    question_11 = models.IntegerField()



    # class Meta:
    #     db_table = 'cms_score'  # 自定义表名

    def __str__(self):
        return self.name







class Course(models.Model):   #课程，如”《微机原理》《大数据理论》《人工智能基础》《数据结构》“
    title = models.CharField(max_length=255) #课程的标题
    description = models.TextField() #课程的简介
    image_url = models.URLField() #课程的封面
    video_url = models.URLField() #课程的url，不用添加
    instructor = models.CharField(max_length=100) #课程的讲解教师
    detail_page_url = models.URLField() #课程的详情页面，即点击”“立即学习
    chapter = models.URLField() #可忽略
    gonggao_context = models.CharField(max_length=255) #课程的公告页面url
    video_1 = models.URLField(blank=True)  #课程的第一节课视频url
    video1_name = models.CharField(max_length=200, blank=True) #课程的第一节课的名称，比如”教学安排（1）“
    video1_date = models.DateTimeField(blank=True, null=True) #课程第一节课的更新时间
    video_1_students = JSONField(default=list, null=True, blank=True) #该课程第一节课的所观看过的学生信息，点赞收藏，评论，后续添加视频进度百分比数据
    video_2 = models.URLField(blank=True)
    video2_name = models.CharField(max_length=200, blank=True)
    video2_date = models.DateTimeField(blank=True, null=True)
    video_2_students = JSONField(default=list, null=True, blank=True)
    video_3 = models.URLField(blank=True)
    video3_name = models.CharField(max_length=200, blank=True)
    video3_date = models.DateTimeField(blank=True, null=True)
    video_3_students = JSONField(default=list, null=True, blank=True)
    video_4 = models.URLField(blank=True)
    video4_name = models.CharField(max_length=200, blank=True)
    video4_date = models.DateTimeField(blank=True, null=True)
    video_4_students = JSONField(default=list, null=True, blank=True)
    video_5 = models.URLField(blank=True)
    video5_name = models.CharField(max_length=200, blank=True)
    video5_date = models.DateTimeField(blank=True, null=True)
    video_5_students = JSONField(default=list, null=True, blank=True)
    video_6 = models.URLField(blank=True)
    video6_name = models.CharField(max_length=200, blank=True)
    video6_date = models.DateTimeField(blank=True, null=True)
    video_6_students = JSONField(default=list, null=True, blank=True)
    video_7 = models.URLField(blank=True)
    video7_name = models.CharField(max_length=200, blank=True)
    video7_date = models.DateTimeField(blank=True, null=True)
    video_7_students = JSONField(default=list, null=True, blank=True)
    video_8 = models.URLField(blank=True)
    video8_name = models.CharField(max_length=200, blank=True)
    video8_date = models.DateTimeField(blank=True, null=True)
    video_8_students = JSONField(default=list, null=True, blank=True)
    video_9 = models.URLField(blank=True)
    video9_name = models.CharField(max_length=200, blank=True)
    video9_date = models.DateTimeField(blank=True, null=True)
    video_9_students = JSONField(default=list, null=True, blank=True)
    video_10 = models.URLField(blank=True)
    video10_name = models.CharField(max_length=200, blank=True)
    video10_date = models.DateTimeField(blank=True, null=True)
    video_10_students = JSONField(default=list, null=True, blank=True)
    video_11 = models.URLField(blank=True)
    video11_name = models.CharField(max_length=200, blank=True)
    video11_date = models.DateTimeField(blank=True, null=True)
    video_11_students = JSONField(default=list, null=True, blank=True)
    video_12 = models.URLField(blank=True)
    video12_name = models.CharField(max_length=200, blank=True)
    video12_date = models.DateTimeField(blank=True, null=True)
    video_12_students = JSONField(default=list, null=True, blank=True)
    video_13 = models.URLField(blank=True)
    video13_name = models.CharField(max_length=200, blank=True)
    video13_date = models.DateTimeField(blank=True, null=True)
    video_13_students = JSONField(default=list, null=True, blank=True)
    video_14 = models.URLField(blank=True)
    video14_name = models.CharField(max_length=200, blank=True)
    video14_date = models.DateTimeField(blank=True, null=True)
    video_14_students = JSONField(default=list, null=True, blank=True)
    video_15 = models.URLField(blank=True)
    video15_name = models.CharField(max_length=200, blank=True)
    video15_date = models.DateTimeField(blank=True, null=True)
    video_15_students = JSONField(default=list, null=True, blank=True)
    video_16 = models.URLField(blank=True)
    video16_name = models.CharField(max_length=200, blank=True)
    video16_date = models.DateTimeField(blank=True, null=True)
    video_16_students = JSONField(default=list, null=True, blank=True)

    test_score = models.JSONField('测试成绩', default=list)  # JSON 字段，默认值为空列表
    knowledge = JSONField(default=list, null=True, blank=True)



    class Meta:
        db_table = 'course'












class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.CharField(max_length=20, choices=[('teacher_qa', '老师答疑模块'), ('general_discussion', '综合讨论区')])
    student_name = models.CharField(max_length=100)  # 新增的字段
    student_number = models.CharField(max_length=20)  # 新增的字段
    class Meta:
        db_table = 'topics'  # 自定义表名
    def __str__(self):

        return self.title
    @classmethod
    def count_by_student_and_course(cls, student_name):
        from django.db.models import Count
        return cls.objects.filter(student_name=student_name).values('course__title').annotate(topic_count=Count('id'))


class Comment(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)  # 新增的字段
    # parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'comments'  # 自定义表名
    def __str__(self):
        return f"Comment by {self.author.username} on '{self.topic.title}'"



# class Comment(models.Model):
#     id = models.AutoField(primary_key=True)
#     content = models.TextField()
#     student_name = models.CharField(max_length=100)  # 假设此处使用学生姓名作为唯一标识
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     topic = models.ForeignKey('Topic', related_name='comments', on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Comment by {self.student_name}'
#
#     class Meta:
#         ordering = ['-created_at']




class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    date = models.DateField()


    class Meta:
        db_table = 'news'  # 自定义表名

    def __str__(self):
        return self.title


class IndividualTimu(models.Model):
    DIFFICULTY_CHOICES = [
        ('A', '90-100'),
        ('B', '80-90'),
        ('C', '60-80'),
        ('D', 'below 60'),
    ]

    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    title = models.CharField(max_length=255)  # 新增字段
    choice_question1 = models.JSONField()
    choice_question2 = models.JSONField()
    choice_question3 = models.JSONField()
    choice_question4 = models.JSONField()
    choice_question5 = models.JSONField()
    choice_question6 = models.JSONField()
    choice_question7 = models.JSONField()
    choice_question8 = models.JSONField()
    choice_question9 = models.JSONField()
    choice_question10 = models.JSONField()
    tiankong1 = models.JSONField()
    tiankong2 = models.JSONField()
    tiankong3 = models.JSONField()
    tiankong4 = models.JSONField()
    tiankong5 = models.JSONField()
    tiankong6 = models.JSONField()
    tiankong7 = models.JSONField()
    tiankong8 = models.JSONField()
    tiankong9 = models.JSONField()
    tiankong10 = models.JSONField()
    jisuanti1 = models.JSONField()
    jisuanti2 = models.JSONField()
    jisuanti3 = models.JSONField()
    jisuanti4 = models.JSONField()
    jisuanti5 = models.JSONField()

    class Meta:
        db_table = 'individual_timu'  # 自定义表名

    # def __str__(self):
    #     return self.difficulty







class IndividualVideo(models.Model):
    # 自动递增的主键ID
    id = models.AutoField(primary_key=True)

    # 知识点名称，最大长度为255个字符
    knowledge = models.CharField(max_length=255)

    # 视频标题，最大长度为255个字符
    title = models.CharField(max_length=255)

    # 分类，使用CharField并限制为预定义的选项
    CLASSIFICATIONS = [
        ('举例', '举例'),
        ('节奏慢', '节奏慢'),
        ('幽默', '幽默'),
        ('严肃', '严肃'),
    ]
    classification = models.CharField(max_length=10, choices=CLASSIFICATIONS)

    # 视频URL，最大长度为512个字符
    url = models.URLField(max_length=512)

    class Meta:
        db_table = 'individual_video'

    def __str__(self):
        return self.title






class StudentPaper(models.Model):
    student_name = models.CharField(max_length=100)
    paper_title = models.CharField(max_length=200)
    file_url = models.URLField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'student_papers'

    def __str__(self):
        return self.paper_title







class Curriculum(StructuredNode):
    name = StringProperty(required=True)
    description = StringProperty()

class KnowledgePoint(StructuredNode):
    name = StringProperty(required=True)
    description = StringProperty()
    grade_level = IntegerProperty()
    parent = RelationshipTo('KnowledgePoint', 'CONTAINS')
    curriculum = RelationshipFrom(Curriculum, 'BELONGS_TO')

class Relationship(StructuredNode):
    knowledge_point_1 = RelationshipTo(KnowledgePoint, 'RELATES_TO')
    knowledge_point_2 = RelationshipTo(KnowledgePoint, 'RELATES_TO')
    relationship_type = StringProperty(choices=[
        ('CONTAINS', '包含'),
        ('BELONGS_TO', '属于'),
        ('EQUIVALENT', '同一'),
        ('PARALLEL', '平行'),
        ('REFERENCE', '参考'),
        ('RELATED', '相关'),
        ('SEQUENTIAL', '顺序'),
    ])



class KnowledgeNode(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'knowledge_node'

    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    question_text = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_answer = models.CharField(max_length=1)
    knowledge_point = models.ForeignKey(KnowledgeNode, on_delete=models.CASCADE)



    class Meta:
        db_table = 'quiz_question'

    def __str__(self):
        return self.question_text