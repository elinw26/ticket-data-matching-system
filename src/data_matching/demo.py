# Ticket Data Matching System — Core Logic Demo
# 
# This demo shows the core matching logic of the system.
# In the actual workflow:
# - new_ids are loaded from Google Sheets
# - history_ids are loaded from a JSON file

# Simulated input data (from Google Sheets)
new_ids = ["1203917524", "567206389", "9999999999", "1203917524"]

# Simulated historical dataset (from JSON file)
history_ids = [
    "1203917524", "1203917524", "1203917524",
    "1203917524", "1203917524", "567206389"
]

# Result containers
high_frequency = []  # IDs appearing 5 or more times
to_check = []        # IDs appearing 1 to 4 times
new_id_list = []     # IDs not found in historical dataset

# Core matching logic
for ids in new_ids:
    count = history_ids.count(ids)
    if count >= 5:
        high_frequency.append(ids)
    elif 1 <= count <= 4:
        to_check.append(ids)
    else:
        new_id_list.append(ids)

# Output results
print("High frequency (5+):", high_frequency, "| Count:", len(high_frequency))
print("To check (1-4):", to_check, "| Count:", len(to_check))
print("New IDs:", new_id_list, "| Count:", len(new_id_list))
