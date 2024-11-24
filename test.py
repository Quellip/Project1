# List of dictionaries
list_of_dicts = [{'subject': 'Art', 'marks': 25}, {'subject': 'biology'}, {'marks': 30}]

# Specify the key for filtering (ensure case sensitivity)
target_key = 'subject'

# Initialize an empty list to store filtered dictionaries
filtered_list = []

# Filter using a for loop
for d in list_of_dicts:
    if target_key in d:
        filtered_list.append(d)

# Print the result
print(filtered_list)