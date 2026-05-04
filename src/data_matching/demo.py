import json

# Stage 1: Load data
# In the actual workflow, new_ids come from Google Sheets
# and history_ids come from a JSON file on Google Drive

with open("sample_history.json", "r") as f:
    data_history = json.load(f)
    history_ids = data_history["ids"]

with open("sample_new_ids.json", "r") as f:
    data_new = json.load(f)
    new_ids = data_new["ids"]

# Stage 2: Compare and classify
matched = []
unmatched = []

for new_id in new_ids:
    if any(new_id == history_id for history_id in history_ids):
        matched.append(new_id)
    else:
        unmatched.append(new_id)

print("Matched:", matched, "| Count:", len(matched))
print("Unmatched:", unmatched, "| Count:", len(unmatched))

# Stage 3: Update history file
history_ids.extend(unmatched)
with open("sample_history.json", "w") as f:
    json.dump({"ids": history_ids}, f)

print("Updated history IDs:", history_ids)
