import pandas as pd 
import matplotlib.pyplot as plt 
# Membaca file Excel 
file_path = r"C:\Users\najlah rupaidah\OneDrive\Dokumen\buku buku semester 5\tugas semester 5\Prak Fiskom\visualisasi data (23 plot)\23. data excel.xlsx" 
data = pd.read_excel(file_path) 
# Asumsi bahwa kolom pertama adalah X dan kolom kedua adalah Y 
X = data.iloc[:, 0]  # Kolom pertama (nilai sumbu x) 
Y = data.iloc[:, 1]  # Kolom kedua (nilai sumbu y) 
# Plotting data 
plt.plot(X, Y) 
plt.title('Data dari "data1.xlsx"') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show()
