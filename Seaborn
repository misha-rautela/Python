import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
%matplotlib inline
tips=sns.load_dataset('tips')
sns.scatterplot(x='total_bill',y='tip',data=tips)

plt.show()
#lineplot function to view the line plot using seaborn package
sns.lineplot(x='size',y='total_bill',data=tips)

#barplot function to view the barplot using seaborn package
sns.barplot(x='day',y='total_bill',data=tips)

#boxplot function to view the boxplot using seaborn package
sns.boxplot(x="day",y='total_bill',data=tips)

#violinplot function to view the violinplot using seaborn package
sns.violinplot(x="day",y='total_bill',data=tips)

#histplot function to view the histplot using seaborn package
sns.histplot(tips['total_bill'],bins=10,kde=True)

#kdeplot function to view the kdeplot using seaborn package
sns.kdeplot(tips['total_bill'],fill=True)

#pairplot function to view the pairplot using seaborn package
sns.pairplot(tips)
