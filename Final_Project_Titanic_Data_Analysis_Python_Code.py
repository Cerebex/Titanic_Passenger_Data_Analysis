import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Open and read csv file into pandas
filename = '/Users/samuelmiller/Documents/Udacity/Data Analyst Nanodegree/Titanic Data/SM Submission 2/titanic_data.csv'
titanic_data_df = pd.read_csv(filename)

# Find Amount of Missing Data in each columns (Site: http://stackoverflow.com/questions/29530232/python-pandas-check-if-any-value-is-nan-in-dataframe)
missing_data = titanic_data_df.isnull().sum()
print missing_data

#Histogram of titanic age distribution
titanic_data_df.Age.hist(bins = 70)
plt.title('Distribution of Age')
plt.xlabel('Ages')
plt.ylabel('Passenger Counts')
plt.show()

#Age Distribution for Survival
p = sns.boxplot(data = titanic_data_df, x = 'Survived', y = 'Age')
p.set(title = 'Age Distribution by Survival', 
        xlabel = 'Survival', 
        ylabel = 'Age Distribution', 
        xticklabels = ['Died', 'Survived'])
plt.show()

#Creates column in data set that shows if someone died. This allows sumation of total dead and alive at a certain age. 
#Plots average survival rate at each specific age. 
titanic_data_df['Dead'] = (titanic_data_df['Survived'] == 0).astype(int)
age_grouped_data = titanic_data_df.groupby('Age')
age_df = age_grouped_data['Survived'].mean()
total_age_survival = age_df.plot(kind='bar', fontsize = 6, title="Survival Rate vs. Age")
total_age_survival.set(xlabel="Age", ylabel="Survival Rate")
plt.show()

#Plots average survival rate of children(<14) and adults.
grouped_data_total_age_survival = age_grouped_data['Survived', 'Dead'].sum()
Total_passengers_age = grouped_data_total_age_survival['Survived'] + grouped_data_total_age_survival['Dead']
average_survived_age_greater_14 = (grouped_data_total_age_survival.loc[grouped_data_total_age_survival.index[:] >14, \
	'Survived'].sum() *1.)/(Total_passengers_age.loc[Total_passengers_age.index[:]>14].sum())
average_survived_age_less_14 = (grouped_data_total_age_survival.loc[grouped_data_total_age_survival.index[:] <=14, \
	'Survived'].sum()*1.)/(Total_passengers_age.loc[Total_passengers_age.index[:] <=14].sum())
age_df_split = pd.DataFrame(
	data= [average_survived_age_less_14, average_survived_age_greater_14],
	index = ['Age<=14', 'Age>14'],
	columns = ['Survival Rate'])
print age_df_split
Child_and_Adult_Survival = age_df_split.plot(kind='bar', title="Survival Rate vs. Age Set", legend = False)
Child_and_Adult_Survival.set(xlabel="Age Set", ylabel="Survival Rate")
plt.show()

#Class survival amount in barplot
df = titanic_data_df.groupby(['Pclass', 'Survived']).apply(len).reset_index()
print df
p = sns.barplot(data = df, x = 'Pclass', y = 0, hue = 'Survived')
p.set_xticklabels(['First Class', 'Second Class', 'Third Class'])
p.set(xlabel = 'P Class', ylabel = 'Passenger Counts', title = 'Class Survival Counts')
plt.show()

#Show's that on average the higher P Class you had, the more likely you were to survive. 
pclass_df = titanic_data_df.groupby('Pclass')['Survived'].mean().reset_index()
print pclass_df
pclass_survival = sns.barplot(data = pclass_df, x='Pclass', y='Survived')
pclass_survival.set(title="P Class by Survival Rate",
						xlabel = "P Class", 
						ylabel="Survival Rate",
						xticklabels = ['First Class', 'Second Class', 'Third Class'])
plt.show()


#Show's on average that females are more likely than males to survive. 
sex_df = titanic_data_df.groupby('Sex')['Survived'].mean().reset_index()
print sex_df
sex_survival = sns.barplot(data = sex_df, x = 'Sex', y = 'Survived')
sex_survival.set(title="Average Survival Rate of Each Sex on Titanic",
					xlabel="Sex", 
					ylabel="Survival Rate")
plt.show()

#Show average survival rate vs. Gender and Class:
pclass_gender_df = titanic_data_df.groupby(['Pclass', 'Sex'])['Survived'].mean().reset_index()
print pclass_gender_df
pclass_gender_survival_plt = sns.barplot(data = pclass_gender_df, x = 'Pclass', y='Survived', hue = 'Sex')
pclass_gender_survival_plt.set(title = "Survival Rate vs. P Class & Sex",
									xlabel = "P Class", 
									ylabel="Survival Rate",
									xticklabels = ['First Class', 'Second Class', 'Third Class'])
plt.show()

#Show total numbers of each class gender that survived and died
plcass_gender_survival_totals = titanic_data_df.groupby(['Pclass', 'Sex', 'Survived']).apply(len).reset_index()
print plcass_gender_survival_totals










