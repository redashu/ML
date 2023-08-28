import pandas as pd
import matplotlib.pyplot as plt 
# storing url in a variable
data_url='https://raw.githubusercontent.com/redashu/Datasets/master/advertising.csv'
# creating data from using URL data
df=pd.read_csv(data_url)
# printing it
print(df.head())
# TV vs sales
print(df['TV'])
# ploting 
plt.xlabel('TV')
plt.ylabel('sales')
# creating first subplot row , column , plot1 
plt.subplot(3,1,1)
plt.title('Advertinsing data')
plt.scatter(df.TV,df.Sales)
plt.subplot(3,1,2)
plt.scatter(df.Radio,df.Sales)
plt.subplot(3,1,3)
plt.scatter(df.Newspaper,df.Sales)
plt.show()

