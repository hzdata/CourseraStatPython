import pandas as pd
boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
boston_df=pd.read_csv(boston_url)
import matplotlib.pyplot as plt
plt.boxplot([boston_df[boston_df['CHAS'] == g]['MEDV'] for g in boston_df['CHAS'].unique()],
            labels=boston_df['CHAS'].unique())

boston_df['Agegrp'] = pd.cut(boston_df['AGE'], bins=[0, 35, 70, float('inf')], labels=['35 years and younger', '35-70 years', '70 years and older'])
import seaborn as sns 

order = ['35 years and younger', '35-70 years', '70 years and older']

sns.boxplot(
    x = "Agegrp",
    y = "MEDV",
    showmeans=True,
    data=boston_df,
    order=order
)
sns.histplot(boston_df["PTRATIO"], kde=True)
t_result = stats.ttest_ind(boston_df[boston_df['CHAS']== 0]['MEDV'], boston_df[boston_df['CHAS'] == 1]['MEDV'])