import pandas as pd
import datetime as dt
import io
import numpy as np
import pandas as pd


df = pd.read_csv('Downloads/austin_address.csv')
df.columns = ['Conctact_ID', "First Name", 'Last Name', "Gender", 'DOB', 'Address', 'ZIP', 'Phone Number', 'Status', 'Created_User', 'Created_DT', 'Modified_User', 'Modified_DT']


df['DOB'] = pd.to_datetime(df['DOB'])
current_date = dt.datetime.now()
df['Age'] = (current_date - df['DOB']) // pd.Timedelta(days=365.25)
df.insert(5, 'Age', df.pop('Age'))

gender_frequencies = df['Gender'].value_counts(dropna=False)
zip_frequencies = df['ZIP'].value_counts(dropna=False)
created_user_frequencies = df['Created_User'].value_counts(dropna=False)

print("Gender Frequencies:")
print(gender_frequencies)

print("\nZIP Code Frequencies:")
print(zip_frequencies)

print("\nCreated User Frequencies:")
print(created_user_frequencies)

age_ranges = pd.cut(df['Age'], bins=[0, 60, 65, 75, 115, float('inf')], labels=['Under 60', '60-64', '65-74', '75-114', '115+'])

age_frequencies = age_ranges.value_counts(dropna=False)
age_frequencies_no_nan = age_ranges.value_counts()
total_count = len(df)

age_percentages = (age_frequencies / total_count) * 100

age_percentages_without_na = (age_frequencies_no_nan / age_frequencies_no_nan.sum()) * 100

print("\n Age Distribution:")
print(age_percentages)
print(age_frequencies)

print('Dataframe with NAN')
age_groups = pd.DataFrame({'Age Range': age_frequencies.index, 'Frequency': age_frequencies.values, 'Percentage': age_percentages.values})

age_groups['Value Percent'] = age_groups['Frequency'] / age_groups['Frequency'].sum() * 100
print(age_groups)

print('Dataframe without NAN')
new_df_without_na = pd.DataFrame({'Age Range': age_percentages_without_na.index, 'Frequency': age_percentages_without_na.values, 'Percentage': age_percentages_without_na.values})

print(new_df_without_na)

