import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

# 加载数据
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'student_data.xlsx')
data = pd.read_excel(file_path)

# 数据预处理
data = data.drop(columns=['Username'])
X = data.drop(columns=['Average Exam Score'])
y = data['Average Exam Score']

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 标准化数据
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 训练模型
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')

# 预测新数据函数
def predict_new_data(new_data):
    new_data_scaled = scaler.transform(new_data)
    predictions = model.predict(new_data_scaled)
    return predictions

# 示例：预测新的学生数据
last_student_data = pd.DataFrame([X.iloc[250]])  # 使用现有数据的最后一条样本作为示例
last_student_predictions = predict_new_data(last_student_data)
print(f'Predicted Average Exam Score (Last Student): {last_student_predictions[0]}')
