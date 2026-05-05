## Data Matching — Core Logic Demo

This folder contains a simplified demo of the core matching logic.
The demo uses local JSON files to make the logic independently
runnable without external API dependencies.

### What this demo shows

- Loading historical data from a JSON file
- Comparing new records against historical data
- Classifying records as matched or unmatched
- Updating the historical dataset with new records

### Files

- [`demo.py`](demo.py) — core matching logic (3-stage workflow)
- [`sample_history.json`](sample_history.json) — simulated historical dataset
- [`sample_new_ids.json`](sample_new_ids.json) — simulated new input data

### Project Context

This demo is part of a three-project data management system
built to support workflows involving 90+ contributors:

- [Project 1 — Basic Data Processing Automation](https://github.com/elinw26/basic-data-processing-automation)
  Automates participant engagement record processing through
  a multi-stage pipeline including metric parsing, sorting,
  cross-spreadsheet matching, and archiving —
  implemented in Google Apps Script

- [Project 2 — Multi-Source Data Processing](https://github.com/elinw26/multi-source-data-processing)
  Manages participant source data through structured JSON datasets
  with a two-part data model (IDs + metadata),
  tracks progression across multiple engagement steps,
  and supports cross-source quality analysis —
  implemented in Google Apps Script

- Project 3 (this project) —
  Extends the workflow with Python-based incremental matching,
  a team collaboration evaluation system,
  and a desktop application interface for contributors

The transition from Google Apps Script to Python reflects the need
for more reliable processing beyond spreadsheet execution limits.
With 90+ contributors generating data across multiple sheets,
JSON files approached the 10MB threshold, making GAS triggers
unreliable for full dataset scans within the 6-minute execution limit.

### Note

This demo isolates the core matching logic for clarity.
The full Project 3 workflow includes:

- a team evaluation system across multiple contributor sheets
- automated daily backup with batch processing
  and timeout handling
- a desktop application (PyQt5) for contributor interaction
- Google Sheets and Google Drive API integration
  for data input, matching, and output

### Possible Extensions

The current system focuses on data matching and reuse
of historical records.

Related implementations across the project series include:

- multi-stage data pipelines with automated archiving
  → implemented in Project 1
- structured multi-field JSON datasets with full CRUD operations
  → implemented in Project 2
- Google Sheets and Google Drive API integration
  → implemented in the full Project 3 workflow
- desktop application interface for contributors
  → implemented in Project 3 (PyQt5)

Further extensions not yet implemented:

- database integration to replace JSON storage
  for larger-scale applications
- full Python desktop application to replace
  GAS-based processing components
