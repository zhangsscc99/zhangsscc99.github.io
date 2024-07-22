import pandas as pd

# Data extracted from the image
data = {
    'First Name': ['Yuting'],
    'Last Name': ['Wang'],
    'Email': ['yutingw3@illinois.edu'],
    'Phone': ['+19179699903'],
    'Location (City)': ['Chicago, Illinois, United States']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel file
file_path = "C:\\Users\\zhang\\Desktop"
df.to_excel(file_path, index=False)

file_path
