import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import os

# 加载数据
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'student_data.xlsx')
student_data = pd.read_excel(file_path)

# 特征和目标变量
features = student_data.drop(columns=['Username', 'Average Exam Score'])
target = student_data['Average Exam Score']

# 数据预处理
# 处理缺失值（如果有）
features.fillna(features.mean(), inplace=True)

# 标准化特征
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测和评估
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 输出结果
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# 查看各特征的系数
coefficients = pd.DataFrame(model.coef_, index=features.columns, columns=['Coefficient'])
print(coefficients)

# 输出最有影响力的特征
most_influential = coefficients.abs().sort_values(by='Coefficient', ascending=False).head(10)
print("Most Influential Features:")
print(most_influential)
