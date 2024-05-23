import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

def detect(df):
    outliers = []
    tr = 3
    mean = np.mean(df)
    std = np.std(df)

    for i in df:
        z = (i - mean)/std
        if np.abs(z)>tr:
            outliers.append(i)
    return outliers

##---------------------------------------------A---------------------------------------------------------------------------------

data = pd.read_csv("DATA.csv")
data = pd.DataFrame(data)


temp_col = data['Temperature']
temp_col_mean = temp_col.mean()
temp_col = temp_col.fillna(temp_col_mean)
data['Temperature'] = temp_col

MV_mean = data['Monthly_variation'].mean()
MV = data['Monthly_variation']
MV = MV.fillna(MV_mean)
data['Monthly_variation'] = MV

A_Mean = data['Anomaly'].mean()
A = data['Anomaly']
A = A.fillna(A_Mean)
data['Anomaly'] = A

print("A) Filled missing values with their respective means. ")
print(data[305791: 305799])
##-----------------------------------------B----------------------------------------------------------------------------------

print("\n\nB) Checking for datatype consistency")
print(data.dtypes)

##-----------------------------------------C----------------------------------------------------------------------------------

print("\n\nC) Added Date column and removed Years and Month columns")
data['Date'] = data['Years'].astype(str) + "-" + data['Month'].astype(str).str.zfill(2)
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].dt.strftime('%m-%y')
data2 = data.drop(columns=['Years', 'Month'])
print(data2.tail(10))

##-----------------------------------------D----------------------------------------------------------------------------------

print("\n\nD) Outliers for temperature: ")
y = data['Temperature'].to_list()
print(detect(y))

##-----------------------------------------E----------------------------------------------------------------------------------

print("\n\nE) Summary statistics for temperature, monthly variation, ananomaly values, including mean, median, standard deviation, and range. ")
print(data.describe())    

##-----------------------------------------F----------------------------------------------------------------------------------


avg = data.groupby('Country')['Temperature'].mean()
print("\n\nF) Countries and their average temperatures: ")
print(avg)

##-----------------------------------------G----------------------------------------------------------------------------------

print("\n\n")
Countries = data.iloc[0:534573][['Years', 'Country', 'Temperature']]
Countries_m = data.groupby(['Years'])['Temperature'].mean().reset_index()
plt.plot(Countries_m['Years'], Countries_m['Temperature'])
plt.xlabel('Years')
plt.ylabel('Temperatures')
plt.title('G) Trend Over The Years')
print("G) Plot made")
plt.show()

##-----------------------------------------H----------------------------------------------------------------------------------

print("\n\n")
H = data.iloc[0:534573][['Month', 'Temperature']]
# print(H['Temperature'].min())
lt = H['Temperature'].idxmin()
ht = H['Temperature'].idxmax()
print("H) Lowest temperature is in February: ")

print(H.loc[lt, 'Month'])
print("Highest temperature is in June: ")
print(H.loc[ht, 'Month'])
H_2 = data.groupby(['Month'])['Temperature'].mean().reset_index()
plt.plot(H_2['Month'], H_2['Temperature'])
plt.xlabel('Month')
plt.ylabel('Temperatures')
plt.title('H) Trend Over The Months')
print("Plot made")
plt.show()

##-----------------------------------------I----------------------------------------------------------------------------------

print("\n\n")
H_3 = data.iloc[0:534573][['Years', 'Month', 'Anomaly']]
# print(H_3)
H_3 = data.groupby('Month')['Anomaly'].mean().reset_index()
plt.scatter(H_3['Month'], H_3['Anomaly'])
plt.xlabel('Month')
plt.ylabel('Anomalies')
plt.title('I) Scatter Plot')
plt.show()
print("I) The plot shows us that the most anomalies occur early in the year. The least occur around August-October.")

##-----------------------------------------J----------------------------------------------------------------------------------
##------------------------------------Afghanistan----------------------------------------------------------------------------------

print("\n\n")
Afghanistan = data[data['Country'] == 'Afghanistan']
Pakistan = data[data['Country'] == 'Pakistan']
Aruba = data[data['Country'] == 'Aruba']
Zimbabwe = data[data['Country'] == 'Zimbabwe']
Argentina = data[data['Country'] == 'Argentina']

Afgh = Afghanistan[['Temperature', 'Years']]
Pak = Pakistan[['Temperature', 'Years']]
Arub = Aruba[['Temperature', 'Years']]
Zimb = Zimbabwe[['Temperature', 'Years']]
Arg = Argentina[['Temperature', 'Years']]

Afgh = Afgh.groupby('Years')['Temperature'].mean().reset_index()

plt.plot(Afgh['Years'], Afgh['Temperature'], marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('J) Afghanistan')

plt.grid(True)
plt.show()

##--------------------------------------Pakistan----------------------------------------------------------------------------------

Pak = Pak.groupby('Years')['Temperature'].mean().reset_index()

plt.plot(Pak['Years'], Pak['Temperature'], marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('J) Pakistan')

plt.grid(True)
plt.show()

##-----------------------------------------Aruba----------------------------------------------------------------------------------

Arub = Arub.groupby('Years')['Temperature'].mean().reset_index()

plt.plot(Arub['Years'], Arub['Temperature'], marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('J) Aruba')

plt.grid(True)
plt.show()

##-----------------------------------------Zimbabwe----------------------------------------------------------------------------------

Zimb = Zimb.groupby('Years')['Temperature'].mean().reset_index()

plt.plot(Zimb['Years'], Zimb['Temperature'], marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('J) Zimbabwe')

plt.grid(True)
plt.show()

##-----------------------------------Argentina----------------------------------------------------------------------------------

Arg = Arg.groupby('Years')['Temperature'].mean().reset_index()

plt.plot(Arg['Years'], Arg['Temperature'], marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('J) Argentina')

plt.grid(True)
plt.show()

print("J) Conclusion:\nArgentina, Pakistan and Aruba share the most similar trend in the change of temperature")

##-----------------------------------------K--------------------------------------------------------------------------------------

print("\n\n")
corr_coeff = data['Temperature'].corr(data['Anomaly'])

plt.scatter(data['Temperature'], data['Anomaly'])
plt.xlabel('Temperatures')
plt.ylabel('Anomalies')
plt.title(f'Scatter-plot\nCorrelation Coefficient: {corr_coeff:.2f}')
plt.grid(True)
print("K) Plot made")
plt.show()