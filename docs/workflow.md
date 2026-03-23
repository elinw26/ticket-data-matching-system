# Data Processing Workflow

This document describes how data flows through the Data Matching Automation System.

The workflow focuses on reusing historical data and processing only new or unmatched records.

---

## Workflow Overview

The data processing workflow can be summarized as:

```
Input Data (Google Sheets)
        ↓
Load Historical Data (JSON)
        ↓
Data Matching (Python)
        ↓
Manual Handling (Unmatched Records)
        ↓
Update Historical Dataset (JSON)
```


Each stage performs a specific role while keeping the system modular and efficient.

---

## Step 1 — Data Input

New data is entered through Google Sheets.

These records serve as the starting point of the processing workflow.

Typical characteristics:

- newly collected records  
- not yet processed  
- may overlap with existing data  

---

## Step 2 — Load Historical Data

The system loads previously processed data from JSON storage.

This dataset serves as a reusable reference for matching operations.

Key purpose:

- avoid reprocessing known records  
- provide consistent historical context  

---

## Step 3 — Data Matching

Incoming data is compared against the historical dataset.

During this step:

- known records are matched automatically  
- unmatched records are identified  

The system separates data into:

- **matched records** → already known  
- **unmatched records** → require further handling  

---

## Step 4 — Manual Handling (Unmatched Records)

Records that could not be matched are processed manually.

This step may include:

- assigning classification results  
- validating new data  
- completing missing information  

This ensures that new data becomes usable for future automation.

---

## Step 5 — Update Historical Dataset

Processed results are written back into the JSON dataset.

This step:

- adds newly processed records  
- updates existing entries if necessary  
- maintains a continuously growing dataset  

---

## Summary

The workflow follows a continuous loop:

1. input new data  
2. reuse historical data  
3. process only unmatched records  
4. update the dataset for future reuse  

This approach reduces repetitive work and enables scalable data processing.
