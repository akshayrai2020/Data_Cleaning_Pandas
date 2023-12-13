import pandas as pd

# Reading the dataset
file_path = 'path_to_your_file/employees_data.csv'
employees_data = pd.read_csv(file_path)

# Handling missing values
employees_data['Age'].fillna(employees_data['Age'].mean(), inplace=True)
employees_data['Height'].fillna(employees_data['Height'].median(), inplace=True)
employees_data['Weight'].fillna(employees_data['Weight'].median(), inplace=True)
employees_data['DateOfBirth'] = pd.to_datetime(employees_data['DateOfBirth'], errors='coerce')

# Handling boolean values
employees_data['IsActive'].fillna(True, inplace=True)
employees_data['IsActive'] = employees_data['IsActive'].astype(bool)

# Drop rows with missing email or invalid date of birth
employees_data = employees_data.dropna(subset=['Email', 'DateOfBirth'])

# Save as new CSV file
cleaned_file_path = 'path_to_your_file/cleaned_employees_data.csv'
employees_data.to_csv(cleaned_file_path, index=False)

# Display cleaned dataset
print("Cleaned Employees Data:")
print(employees_data)
