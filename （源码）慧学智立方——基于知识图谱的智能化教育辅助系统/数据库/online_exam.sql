/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80024
 Source Host           : 192.168.60.6:3306
 Source Schema         : online_exam

 Target Server Type    : MySQL
 Target Server Version : 80024
 File Encoding         : 65001

 Date: 09/11/2021 12:37:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `group_id` int(0) NOT NULL,
  `permission_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(0) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add student', 7, 'add_student');
INSERT INTO `auth_permission` VALUES (26, 'Can change student', 7, 'change_student');
INSERT INTO `auth_permission` VALUES (27, 'Can delete student', 7, 'delete_student');
INSERT INTO `auth_permission` VALUES (28, 'Can view student', 7, 'view_student');
INSERT INTO `auth_permission` VALUES (29, 'Can add subject', 8, 'add_subject');
INSERT INTO `auth_permission` VALUES (30, 'Can change subject', 8, 'change_subject');
INSERT INTO `auth_permission` VALUES (31, 'Can delete subject', 8, 'delete_subject');
INSERT INTO `auth_permission` VALUES (32, 'Can view subject', 8, 'view_subject');
INSERT INTO `auth_permission` VALUES (33, 'Can add user table', 9, 'add_usertable');
INSERT INTO `auth_permission` VALUES (34, 'Can change user table', 9, 'change_usertable');
INSERT INTO `auth_permission` VALUES (35, 'Can delete user table', 9, 'delete_usertable');
INSERT INTO `auth_permission` VALUES (36, 'Can view user table', 9, 'view_usertable');
INSERT INTO `auth_permission` VALUES (37, 'Can add teacher', 10, 'add_teacher');
INSERT INTO `auth_permission` VALUES (38, 'Can change teacher', 10, 'change_teacher');
INSERT INTO `auth_permission` VALUES (39, 'Can delete teacher', 10, 'delete_teacher');
INSERT INTO `auth_permission` VALUES (40, 'Can view teacher', 10, 'view_teacher');
INSERT INTO `auth_permission` VALUES (41, 'Can add question', 11, 'add_question');
INSERT INTO `auth_permission` VALUES (42, 'Can change question', 11, 'change_question');
INSERT INTO `auth_permission` VALUES (43, 'Can delete question', 11, 'delete_question');
INSERT INTO `auth_permission` VALUES (44, 'Can view question', 11, 'view_question');
INSERT INTO `auth_permission` VALUES (45, 'Can add record', 12, 'add_record');
INSERT INTO `auth_permission` VALUES (46, 'Can change record', 12, 'change_record');
INSERT INTO `auth_permission` VALUES (47, 'Can delete record', 12, 'delete_record');
INSERT INTO `auth_permission` VALUES (48, 'Can view record', 12, 'view_record');
INSERT INTO `auth_permission` VALUES (49, 'Can add test paper', 13, 'add_testpaper');
INSERT INTO `auth_permission` VALUES (50, 'Can change test paper', 13, 'change_testpaper');
INSERT INTO `auth_permission` VALUES (51, 'Can delete test paper', 13, 'delete_testpaper');
INSERT INTO `auth_permission` VALUES (52, 'Can view test paper', 13, 'view_testpaper');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$q0YUrV5Xca6zmh0Ai0grZG$WXEQmr+710NMfGqu47YrZ7hXGatyWUSw+I2AomuiEd8=', '2021-11-08 14:05:50.239605', 1, 'admin', '', '', '1427@qq.com', 1, 1, '2021-11-08 14:05:40.487735');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `group_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `permission_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL DEFAULT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(0) NULL DEFAULT NULL,
  `user_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (11, 'cms', 'question');
INSERT INTO `django_content_type` VALUES (12, 'cms', 'record');
INSERT INTO `django_content_type` VALUES (13, 'cms', 'testpaper');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'user', 'student');
INSERT INTO `django_content_type` VALUES (8, 'user', 'subject');
INSERT INTO `django_content_type` VALUES (10, 'user', 'teacher');
INSERT INTO `django_content_type` VALUES (9, 'user', 'usertable');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-10-24 01:53:56.401991');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-10-24 01:53:57.052782');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-10-24 01:53:57.218728');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-10-24 01:53:57.240716');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-24 01:53:57.255708');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-10-24 01:53:57.363682');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2021-10-24 01:53:57.430654');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2021-10-24 01:53:57.506635');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2021-10-24 01:53:57.526636');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2021-10-24 01:53:57.589603');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2021-10-24 01:53:57.594602');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2021-10-24 01:53:57.610602');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2021-10-24 01:53:57.689576');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2021-10-24 01:53:57.778548');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2021-10-24 01:53:57.870518');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2021-10-24 01:53:57.896505');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2021-10-24 01:53:57.963483');
INSERT INTO `django_migrations` VALUES (18, 'cms', '0001_initial', '2021-10-24 01:53:58.262385');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2021-10-24 01:53:58.320366');
INSERT INTO `django_migrations` VALUES (20, 'user', '0001_initial', '2021-10-24 01:53:58.533298');
INSERT INTO `django_migrations` VALUES (21, 'cms', '0002_record_name', '2021-10-24 15:18:28.681192');
INSERT INTO `django_migrations` VALUES (22, 'cms', '0003_auto_20211024_2333', '2021-10-24 15:33:53.359965');
INSERT INTO `django_migrations` VALUES (23, 'cms', '0004_auto_20211030_0919', '2021-10-30 01:19:59.652061');
INSERT INTO `django_migrations` VALUES (24, 'cms', '0005_auto_20211030_1941', '2021-10-30 11:41:19.767000');
INSERT INTO `django_migrations` VALUES (25, 'cms', '0006_auto_20211030_1951', '2021-10-30 11:51:08.407786');
INSERT INTO `django_migrations` VALUES (26, 'cms', '0007_testpaper_answer', '2021-10-31 05:52:20.451698');
INSERT INTO `django_migrations` VALUES (27, 'cms', '0008_record_answer', '2021-10-31 05:59:52.819287');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2r1avn3mkrc25u2iylv07idl7wdljb9q', 'eyJyb2xlIjoyLCJ1c2VyX2lkIjoxLCJ4dWVoYW8iOiIyMTAwMDA3IiwidXNlcm5hbWUiOiJcdTczOGJcdTY3OTcifQ:1mh5Kv:xPPwpCyT25M2ptFYBCUkUjCH62nawgM6Zsc21O-1c50', '2021-11-14 07:33:01.314962');
INSERT INTO `django_session` VALUES ('te1v7zm2t447u05q85qbxfgw8ik2rd11', 'eyJ4dWVoYW8iOiIyMTAwMDA2Iiwicm9sZSI6MiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJcdTczOGJcdTY3OTcifQ:1mkIn4:8KZISj-KClsNzWugPZY30Wd-TJVtL-v4UlIn5DUgLgw', '2021-11-23 04:31:22.545810');
INSERT INTO `django_session` VALUES ('wfseqqxnxfq6p59qszc5hrpwajxtg8jx', '.eJxVj88KgzAMh98lZynpP2s97r43EKS17ermLKiFwdi7rzIZmEMO3-9LSN7wyj6aBC0wiqUUVLCkyUNLK8irX_rRQcsr6E3eYv8nQOHErBkeft4DdzfzLZEhzdsyWrIr5EhXck3OT5fDPS2IZo1lmvNGUisHrR1lDAVSUVuL3BtldOBa-qDUYGVhIlBnkdVFQMEVqsYFC7-rZ_MsL0CXZWDYZeFR750jfL4Y0kxC:1mk5LM:Guful8lXfLeGbahb37s7AmN3J1F_U8VtGlizYL7iA5A', '2021-11-22 14:09:52.940561');

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `course` int(0) NULL DEFAULT NULL,
  `title` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `a` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `b` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `c` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `d` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `answer` varchar(1000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `difficulty` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `score` int(0) NOT NULL,
  `last_modify_time` datetime(6) NULL DEFAULT NULL,
  `owner` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `question_type` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of question
-- ----------------------------
INSERT INTO `question` VALUES (1, 2, '中国的面积是多少', '960万平方公里', '850万平方公里', '800万平方公里 ', '700万平方公里', 'A', '简单', 10, '2021-10-30 09:21:30.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (2, 1, '江苏的省会是哪个', '南京', '苏州', '徐州', '合肥', 'A', '一般', 10, '2021-10-30 06:10:13.746688', 'admin', '单选题');
INSERT INTO `question` VALUES (3, 2, '国庆节是哪一天', '10月1日', '8月1日', '7月1日', '1月1日', 'A', '简单', 10, '2021-10-30 19:43:58.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (4, 2, '腾讯的总部在哪里', '杭州', '宁波', '南京', '深圳', 'D', '简单', 10, '2021-10-30 19:45:19.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (5, 2, '杭州马指的是谁', '马化腾', '马云波', '马云飞', '马云', 'D', '简单', 10, '2021-10-30 19:46:15.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (6, 1, '历史上秦国第一任皇帝是谁', '嬴政', '嬴驷', '嬴稷', '赢楚', 'A', '简单', 10, '2021-10-30 19:47:35.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (7, 1, '屈原所在国家是哪个国', '楚国', '庆国', '赵国', '燕国', 'A', '简单', 10, '2021-10-30 19:48:23.000000', 'admin', '单选题');
INSERT INTO `question` VALUES (8, 1, '中国是世界经济第一大国', '0', '0', '0', '0', '错', '简单', 5, '2021-10-30 19:49:55.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (9, 1, '离骚是屈原编写的', NULL, NULL, NULL, NULL, '对', '简单', 5, '2021-10-30 19:51:42.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (10, 1, '床前明月光，疑是地上霜这首诗是杜甫所著', NULL, NULL, NULL, NULL, '错', '简单', 5, '2021-10-30 19:53:14.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (11, 1, '三国鼎立，三国指的是魏蜀吴', NULL, NULL, NULL, NULL, '对', '简单', 5, '2021-10-30 19:53:50.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (12, 1, '二马指的是马云和马化腾', NULL, NULL, NULL, NULL, '对', '简单', 5, '2021-10-30 19:54:18.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (13, 1, '赤壁之战是曹操和刘备对战', NULL, NULL, NULL, NULL, '错', '简单', 5, '2021-10-30 19:55:02.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (14, 1, '乌江自刎的历史人物是张辽', NULL, NULL, NULL, NULL, '错', '简单', 5, '2021-10-30 19:55:43.000000', 'admin', '判断题');
INSERT INTO `question` VALUES (15, 1, '请简要回答培养初中生形象思维能力的必要性', NULL, NULL, NULL, NULL, '思维是人脑对客观事物的一般特性和规律的一种间接的、概括的反映过程。进行思维训练，培养学生的思维能力', '一般', 25, '2021-10-30 19:57:03.000000', 'admin', '简答题');
INSERT INTO `question` VALUES (16, 1, '辛亥革命最主要的历史功绩是什么？', NULL, NULL, NULL, NULL, '开疆拓土', '一般', 25, '2021-10-30 19:57:57.000000', 'admin', '简答题');
INSERT INTO `question` VALUES (17, 1, '洋务运动有什么历史作用？', NULL, NULL, NULL, NULL, '创新', '一般', 25, '2021-10-30 19:58:38.000000', 'admin', '简答题');
INSERT INTO `question` VALUES (18, 1, '北京奥运会是哪一年', '2018', '2019', '2020', '2021', 'A', '简单', 10, '2021-10-31 07:28:43.877714', 'admin', '单选题');

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `xuehao` int(0) NOT NULL,
  `grade` double NOT NULL,
  `test_paper_id` int(0) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `exam_time` datetime(6) NULL DEFAULT NULL,
  `answer` varchar(500) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES (1, 210801520, 98, 3, '张三', '2021-10-24 15:33:53.063055', '');
INSERT INTO `record` VALUES (2, 1, 55, 3, '王林', '2021-10-31 06:03:14.390488', '');
INSERT INTO `record` VALUES (3, 1, 45, 4, '王林', '2021-10-31 06:08:56.355565', '[\'A\', \'A\', \'A\', \'D\', \'D\', \'对\', \'错\', \'对\', \'错\', \'错\', \'创新\']');
INSERT INTO `record` VALUES (4, 1, 80, 5, '王林', '2021-10-31 06:11:11.355168', '[\'A\', \'A\', \'D\', \'D\', \'A\', \'错\', \'对\', \'对\', \'错\', \'错\', \'我都奥我到我都爱我的哦啊哦我到哦我都爱我到位到我的哦哦啊我到位打完大无打完大打完大无打完大哇无大无大\']');
INSERT INTO `record` VALUES (5, 1, 80, 5, '王林', '2021-10-31 06:13:43.419290', '[\'A\', \'A\', \'D\', \'D\', \'A\', \'错\', \'对\', \'对\', \'错\', \'错\', \'哈哈哈哈哈哈哈哈哈\']');
INSERT INTO `record` VALUES (6, 1, 80, 5, '张三丰', '2021-10-31 07:25:30.674781', '[\'A\', \'A\', \'D\', \'D\', \'A\', \'错\', \'对\', \'对\', \'错\', \'错\', \'哈哈哈哈哈哈哈\']');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `number` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `gender` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `age` int(0) NOT NULL,
  `image` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `role` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '2108015', '张三2', '123', '男', '12345678991', 24, '/static/images/default.png', 1);
INSERT INTO `student` VALUES (2, '2100006', '王二小', '123', '', '12345678998', 18, '/static/image/default.png', 1);
INSERT INTO `student` VALUES (3, '2100007', '张三丰', '123', '', '15925898745', 18, '/static/image/default.png', 1);

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of subject
-- ----------------------------
INSERT INTO `subject` VALUES (1, '数学', '2021-10-30 09:22:00.000000');
INSERT INTO `subject` VALUES (2, '地理', '2021-10-30 09:22:08.000000');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `number` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `age` int(0) NOT NULL,
  `work_years` int(0) NOT NULL,
  `teacher_school` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `role` int(0) NOT NULL,
  `subject_id` bigint(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `teacher_subject_id_72aadb2d_fk_subject_id`(`subject_id`) USING BTREE,
  CONSTRAINT `teacher_subject_id_72aadb2d_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (1, '王林', '2100005', '123', '12345678998', 65, 35, '南京理工大学', 2, 1);

-- ----------------------------
-- Table structure for test_paper
-- ----------------------------
DROP TABLE IF EXISTS `test_paper`;
CREATE TABLE `test_paper`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `owner` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `course` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `time` int(0) NOT NULL,
  `exam_time` datetime(6) NULL DEFAULT NULL,
  `pid` varchar(500) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `answer` varchar(500) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test_paper
-- ----------------------------
INSERT INTO `test_paper` VALUES (3, '数学', '王林', '综合', 70, '2021-10-31 06:01:42.968875', '[7, 5, 1, 3, 4, 14, 11, 10, 12, 9, 16]', '[\'A\', \'A\', \'A\', \'D\', \'D\', \'A\', \'A\', \'错\', \'对\', \'错\', \'对\', \'对\', \'错\', \'错\', \'思维是人脑对客观事物的一般特性和规律的一种间接的、概括的反映过程。进行思维训练，培养学生的思维能力\', \'开疆拓土\', \'创新\']');
INSERT INTO `test_paper` VALUES (3, '语文', '王林', '综合', 70, '2021-10-31 06:08:18.149846', '[7, 3, 1, 5, 4, 12, 13, 11, 8, 14, 17]', '[ \'A\', \'A\', \'A\', \'D\', \'D\', \'对\', \'错\', \'对\', \'错\', \'错\',\'创新\']');
INSERT INTO `test_paper` VALUES (3, '地理', '王林', '综合', 60, '2021-10-31 06:10:37.292120', '[3, 7, 4, 5, 1, 8, 12, 11, 14, 10, 17]', '[\'A\', \'A\', \'D\', \'D\', \'A\', \'错\', \'对\', \'对\', \'错\', \'错\', \'创新\']');
INSERT INTO `test_paper` VALUES (3, '政治', '王林', '综合', 60, '2021-10-31 07:28:58.030162', '[4, 3, 1, 5, 6, 8, 9, 14, 11, 10, 16]', '[\'D\', \'A\', \'A\', \'D\', \'A\', \'错\', \'对\', \'错\', \'对\', \'错\', \'开疆拓土\']');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `role` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '123', '123456', '2021-10-24 22:10:39.000000', 3);

SET FOREIGN_KEY_CHECKS = 1;
