"""online_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from cms import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('',views.login),
    path('index',views.index),
    path('login_out',views.login_out),
    path('chengji',views.chengji),
    path('get_chengji',views.get_chengji),
    path('shijuan', views.shijuan),
    path('get_shijuan', views.get_shijuan),
    path('shiti',views.shiti),
    path('get_questions',views.get_questions),
    path('add_question',views.add_question),
    path('edit_question',views.edit_question),
    path('del_question',views.del_question),
    path('add_shijuan',views.add_shijuan),
    path('test_paper',views.test_paper),
    path('to_test_paper/<pid>',views.to_test_paper),
    path('inference',views.inference),
    path('see_shijuan/<pid>',views.see_shijuan),
    path('edit_shijuan',views.edit_shijuan),
    path('get_scores/', views.get_scores, name='get_scores'),
    path('to_test_paper/uphomework/',views.uphomework),
    path('upload_zuowen_photo/', views.upload_zuowen_photo, name='upload_zuowen_photo'),
    path('ai_answer/', views.ai_answer, name='ai_answer'),
    # path('get_words/', views.get_words, name='get_words'),
    path('gendu/', views.gendu, name='gendu'),
    path('your_endpoint/', views.ChangeLanguageView.as_view(), name='change_language'),
    path('dialogue/', views.dialogue, name='dialogue'),
    path('setUserLanguage/', views.setUserLanguage, name='setUserLanguage'),
    path('setAiLanguage/', views.setAiLanguage, name='setAiLanguage'),
    # path('AIcourse/', views.AIcourseView.as_view(), name='AIcourse'),
    path('set_chat_mode/', views.set_chat_mode, name='set_chat_mode'),

    # path('courses/', views.course_list, name='course_list'),
    path('AIcourse/', views.course_list,name='course_list'),
    path('AIcourse/<int:course_id>/', views.course_detail, name='course_detail'),
    # path('AIcourse/<int:course_id>/', views.course_detail, name='course-detail'),
    path('AIcourse/<int:course_id>/<int:chapter>', views.shangke_list, name='shangke_list'),
    path('AIcourse/<int:course_id>/<int:chapter>/gonggao_<int:announcement_id>/', views.gonggao, name='gonggao'),
    path('AIcourse/<int:course_id>/<int:chapter>/kejian_<int:announcement_id>/', views.kejian, name='kejian'),
    path('AIcourse/<int:course_id>/<int:chapter>/test_<int:announcement_id>/<pid>', views.test, name='test'),
    path('AIcourse/<int:course_id>/<int:chapter>/exam_<int:announcement_id>/', views.exam, name='exam'),
    path('AIcourse/<int:course_id>/<int:chapter>/discuss_<int:announcement_id>/', views.discuss, name='discuss'),
    path('japanese_museum/', views.japanese_museum, name='japanese_museum'),
    path('nanking_massacre_museum/', views.nanking_massacre_museum, name='nanking_massacre_museum'),
    path('physics_lab/', views.physics_lab, name='physics_lab'),
    path('update_student_data/', views.update_student_data, name='update_student_data'),
    path('submit_paper/', views.submit_paper, name='submit_paper'),
    path('success/', views.success_page, name='success_page'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('individual_chengji/', views.student_data_view, name='student_data_view'),
path('get_courses_by_module/<int:module_id>/', views.get_courses_by_module, name='get_courses_by_module'),


path('api/topics/', views.api_topics, name='api_topics'),
path('api/topics_list/', views.api_topics_list, name='api_topics_list'),

# path('api/comments/topic/<int:topic_id>/', views.get_topic_comments, name='get_topic_comments'),

    path('api/comments/', views.api_comments, name='api_comments'),
    # path('api/comments/topic/<int:topic_id>/', views.api_comments_list, name='api_comments_list'),
    path('api/comments_list/<int:topic_id>/', views.api_comments_list, name='api_comments_list'),
    path('api/topic_detail/<int:topic_id>/', views.topic_detail, name='topic_detail'),
path('courses/', views.api_courses, name='courses-list'),
path('fetch_comments/', views.fetch_comments, name='fetch_comments'),
    path('api/get_detailed_data/', views.get_detailed_datas, name='get_detailed_datas'),
    path('analyzeScores/', views.analyzeScores, name='analyzeScores'),
    path('get_course_id_to_analyse/',views.get_course_id_to_analyse, name='get_course_id_to_analyse'),
    path('generate_exam/', views.generate_exam, name='generate_exam'),
path('get_exam_info/', views.get_exam_info, name='get_exam_info'),
path('upexam/', views.upexam, name='upexam'),
path('download_and_grade/<int:paper_id>/', views.download_and_grade, name='download_and_grade'),


path('admin_2/', views.admin_2,name='admin_2'),
path('admin_2/index.html', views.index_html, name='index_html'),
path('admin_2/flex-layout.html', views.flex_layout_html, name='flex_layout_html'),
path('admin_2/flow-layout.html', views.flow_layout_html, name='flow_layout_html'),
path('admin_2/button.html', views.button_view, name='button_view'),
path('admin_2/table.html', views.table_html, name='table_html'),
path('admin_2/form.html', views.form_html, name='form_html'),
path('admin_2/popups.html', views.popups_html, name='popups_html'),

path('admin_2/echarts.html', views.echarts_html, name='echarts_html'),

path('admin_2/ueditor.html', views.ueditor_html, name='ueditor_html'),


path('admin_2/progress.html', views.progress_html, name='progress_html'),
path('admin_2/tab.html', views.tab_html, name='tab_html'),

path('admin_2/button-dropdown.html', views.button_dropdown_html, name='button_dropdown_html'),
path('admin_2/title.html', views.title_html, name='title_html'),
path('admin_2/paging.html', views.paging_html, name='paging_html'),
path('admin_2/animation.html', views.animation_html, name='animation_html'),
path('admin_2/breadcrumb.html', views.breadcrumb_html, name='breadcrumb_html'),
path('admin_2/layer.html', views.layer_html, name='layer_html'),
path('admin_2/paging.html/', views.paging_html, name='paging_html'),

path('get_violence_data/',  views.get_violence_data, name='get_violence_data'),

    path('send_alert/', views.send_alert, name='send_alert'),

# path('loudongjiance/', views.loudongjiance, name='loudongjiance'),
path('neo4j/', views.neo4j_visualization, name='neo4j_visualization'),
    path('api/get-graph-data/', views.get_graph_data, name='get_graph_data'),
# path('visualization/', views.graph_visualization, name='graph_visualization'),
path('loudongjiance/', views.graph_visualization, name='graph_visualization'),

    path('check-answers/', views.check_answers, name='check_answers'),
    path('save_elements/', views.save_elements, name='save_elements'),
    path('submit_student_answer/', views.submit_student_answer, name='submit_student_answer'),

path('ai_reply_student_question/', views.AI_reply_student_question, name='ai_reply_student_question'),




]
