import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Doc du lieu tu file csv
try:
    df = pd.read_csv('nangsuat_thoitiet.csv')
    print("Doc file thanh cong. Tong so dong:", len(df))
except FileNotFoundError:
    print("Loi: Khong tim thay file nangsuat_thoitiet.csv")
    exit()

# 2. Lam sach du lieu
# Cac cot can phan tich
columns_check = ['NangSuat(Tan/ha)', 'LuongMua(mm)', 'NhietDo(C)', 'DoAm(%)']

# Chuyen doi du lieu sang dang so, loi se thanh NaN
for col in columns_check:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Xoa cac dong co gia tri NaN
df_clean = df.dropna()

print("So dong bi loai bo:", len(df) - len(df_clean))
print("So dong du lieu sach:", len(df_clean))

# 3. Tinh he so tuong quan
correlation = df_clean[columns_check].corr()
print("\nMa tran tuong quan:")
print(correlation)

# 4. Ve bieu do
plt.figure(figsize=(12, 8))

# Bieu do Heatmap
plt.subplot(2, 2, 1)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('He so tuong quan')

# Bieu do Nang suat vs Luong mua
plt.subplot(2, 2, 2)
sns.scatterplot(data=df_clean, x='LuongMua(mm)', y='NangSuat(Tan/ha)')
sns.regplot(data=df_clean, x='LuongMua(mm)', y='NangSuat(Tan/ha)', scatter=False, color='red')
plt.title('Nang suat theo Luong mua')

# Bieu do Nang suat vs Nhiet do
plt.subplot(2, 2, 3)
sns.scatterplot(data=df_clean, x='NhietDo(C)', y='NangSuat(Tan/ha)')
sns.regplot(data=df_clean, x='NhietDo(C)', y='NangSuat(Tan/ha)', scatter=False, color='red')
plt.title('Nang suat theo Nhiet do')

# Bieu do Nang suat vs Do am
plt.subplot(2, 2, 4)
sns.scatterplot(data=df_clean, x='DoAm(%)', y='NangSuat(Tan/ha)')
sns.regplot(data=df_clean, x='DoAm(%)', y='NangSuat(Tan/ha)', scatter=False, color='red')
plt.title('Nang suat theo Do am')

plt.tight_layout()
plt.show()