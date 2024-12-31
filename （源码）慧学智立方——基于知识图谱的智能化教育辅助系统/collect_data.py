import pandas as pd
import random
import os

# 生成随机学生姓名
def generate_student_names(num_students):
    first_names = ['张', '王', '李', '赵', '刘']
    last_names = ['伟', '芳', '秀英', '敏', '静', '丽', '强', '磊', '洋', '艳']
    return [random.choice(first_names) + random.choice(last_names) for _ in range(num_students)]

# 生成合理数据
def generate_student_data(num_students):
    data = []
    for _ in range(num_students):
        total_likes = random.randint(0, 16)
        like_percentage = total_likes / 16
        total_favorites = random.randint(0, 16)
        favorite_percentage = total_favorites / 16
        useful_progress_number = random.randint(0, 16)
        unuseful_progress_number = 16 - useful_progress_number
        progress = [random.randint(30, 100) if i < useful_progress_number else random.randint(0, 29) for i in range(16)]
        emo = [random.randint(0, 100) for _ in range(16)]
        participation_rate = useful_progress_number / 16

        # 根据学生的表现来生成测试成绩
        base_score = (sum(progress) / len(progress) + sum(emo) / len(emo)) / 2
        tests = [min(100, max(0, int(random.gauss(base_score, 10)))) for _ in range(5)]
        average_exam_score = sum(tests) / 5

        row = [
            total_likes, like_percentage, total_favorites, favorite_percentage,
            useful_progress_number, unuseful_progress_number, average_exam_score, participation_rate
        ] + tests + [average_exam_score] + progress + emo

        data.append(row)

    columns = [
        'Total Likes', 'Like Percentage', 'Total Favorites', 'Favorite Percentage', 'Useful Progress Number',
        'Unuseful Progress Number', 'Average Score', 'Participation Rate', 'Test 1', 'Test 2', 'Test 3', 'Test 4',
        'Test 5', 'Average Exam Score', 'Progress 1', 'Progress 2', 'Progress 3', 'Progress 4', 'Progress 5',
        'Progress 6', 'Progress 7', 'Progress 8', 'Progress 9', 'Progress 10', 'Progress 11', 'Progress 12',
        'Progress 13', 'Progress 14', 'Progress 15', 'Progress 16', 'Emo 1', 'Emo 2', 'Emo 3', 'Emo 4', 'Emo 5',
        'Emo 6', 'Emo 7', 'Emo 8', 'Emo 9', 'Emo 10', 'Emo 11', 'Emo 12', 'Emo 13', 'Emo 14', 'Emo 15', 'Emo 16'
    ]

    return pd.DataFrame(data, columns=columns)

# 生成数据并导出到Excel
num_students = 1000  # 生成1000个学生数据，以增加数据样本的数量
student_names = generate_student_names(num_students)
student_data = generate_student_data(num_students)
student_data['Username'] = student_names

# 调整列顺序
student_data = student_data[['Username'] + [col for col in student_data.columns if col != 'Username']]

# 获取桌面路径
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'student_data.xlsx')

# 保存到Excel
student_data.to_excel(file_path, index=False)
print(f'文件已保存到: {file_path}')
