## Data Matching — Core Logic Demo

This folder contains a simplified demo of the core matching logic.

### What this demo shows

- Loading historical data from a JSON file
- Comparing new records against historical data
- Classifying records as matched or unmatched
- Updating the historical dataset with new records

### Files

- `demo.py` — core matching logic (3-stage workflow)
- `sample_history.json` — simulated historical dataset
- `sample_new_ids.json` — simulated new input data

### Note

This is a simplified example focused on the matching logic.
In the full workflow:
- new data is loaded from Google Sheets via API
- historical data is stored on Google Drive
- results are written back to Google Sheets

### Possible extensions

- Integration with Google Sheets API
- Matching based on multiple fields
- Database integration for larger scale
