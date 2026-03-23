# Data-matching-automation-system
> Automated data matching and processing system using Python, Google Sheets, and JSON for reusable data workflows.

---

## Project Overview

In collaborative data processing workflows, data from multiple sources often overlaps and is processed repeatedly.

Without a shared historical dataset:

- processed results are not reused  
- manual work increases across contributors  
- data consistency becomes difficult to maintain  

Additionally, spreadsheet-based solutions (e.g. Google Apps Script) do not scale well due to execution time limitations.

This project introduces a structured workflow that separates data input, data processing, and data storage.

It enables efficient reuse of historical data and supports scalable data processing beyond spreadsheet limitations.

## Workflow Overview

The system is built around a continuous data processing loop:

```text
Input Data
   │
   ▼
Historical Matching
   │
   ▼
Manual Processing
   │
   ▼
Data Update
   │
   ▼
Data Reuse
```

The workflow focuses on reusing existing results, processing only new data, and continuously building a reusable historical dataset.

---

## Example Workflow

The following example illustrates how data flows through the system and how historical data is reused to reduce manual work.

### Step 1 — Data Input 

New data is added to the input sheet as the starting point of the processing workflow.

<br>
<img src="docs/input_example.png" width="300">
<br>

---

### Step 2 — Historical Data Loading

Existing records are loaded from the JSON dataset to provide a reusable historical reference.

<br>
<img src="docs/history_before.png" width="350">
<br>

---

### Step 3 — Data Matching

Incoming data is matched against the historical dataset.  

Known records are processed automatically, while unmatched entries are identified for further handling.

<br>
<img src="docs/output_example.png" width="300">
<br>

---

### Step 4 — Data Update 

Processed results are written back to the JSON dataset, updating the historical data for future reuse.

<br>
<img src="docs/history_after.png" width="350">
<br>

---

## Project Structure

```text

src/
├─  frontend_data_matching/
└─  backend_data_update/

docs/
├─ architecture.md
├─ workflow.md
└─ code-structure.md

```

- **src** contains the implementation of the data processing system  
- **docs** contains detailed documentation describing system design and workflow logic


## Component Overview

### Data Matching (Frontend)

Responsible for handling incoming data and matching it against the historical dataset.

Typical operations include:

- importing new data  
- matching against existing records  
- identifying unmatched entries  

---

### Data Processing (Manual Step)

Responsible for handling data that cannot be matched automatically.

Typical operations include:

- analyzing new data  
- assigning classification results  

---

### Data Update (Backend)

Responsible for updating and maintaining the historical dataset.

Typical operations include:

- collecting processed results  
- updating JSON data  
- maintaining reusable storage  

---

### JSON Data Layer

JSON files stored in Google Drive serve as the shared data layer.

This layer enables:

- reuse of processed data  
- separation between processing and storage  
- reduced dependency on spreadsheets

---

## System Structure
The system is divided into three logical parts:

```text
Google Sheets (Interaction)
        ↓
Python Processing
        ↓
JSON Data Storage

```

---
## Documentation

Detailed documentation is available in the **docs** directory:

- System architecture → [docs/architecture.md](docs/architecture.md)
- Data workflow explanation → [docs/workflow.md](docs/workflow.md)
- Code structure explanation → [docs/code-structure.md](docs/code-structure.md)

These documents describe the system design and workflow logic in more detail.

## Technologies

- Python  
- JSON  
- Google Sheets  
- Google Drive  
- Google Apps Script (background)

---

## Status

This repository contains a simplified public version of the automation system.

Sensitive data and internal workflow details have been removed before publication.

---

## Notes

- translates real-world workflows into structured systems  
- applies automation under practical constraints  
- transitions from spreadsheet-based logic to Python  
- builds reusable data processing pipelines  
