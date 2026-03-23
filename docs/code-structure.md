# Code Structure

This document describes how the Data Matching Automation System is organized at the code level.

The system follows a modular structure that separates user interaction, data preparation, and data processing into independent components.

---

## Overview

The system consists of three main modules:


```
src/
    component_A_data_preparation/
    component_B_data_preparation/
    component_C_data_matching/
```



Each module represents a distinct stage in the data processing workflow and has a clearly defined responsibility.

---

## Component A — Interaction Layer (Google Sheets / GAS)

This module handles user interaction and serves as the entry and exit point of the system.

Responsibilities:

- receive input data through Google Sheets  
- display processed results in spreadsheet format  
- support manual handling of unmatched records  
- trigger or coordinate processing steps when required  

Notes:

- implemented using Google Sheets and Google Apps Script (GAS)  
- focuses on usability and data visibility rather than core processing logic  

---

## Component B — Data Preparation

This module transforms raw input data into structured datasets for processing.

Responsibilities:

- read input data from spreadsheets  
- normalize and clean raw records  
- extract relevant identifiers and metadata  
- generate structured JSON datasets  
- update datasets when new data is added  

Output:

- structured JSON files used as the input for the matching module  

---

## Component C — Data Matching

This module performs the core matching and analysis logic.

Responsibilities:

- load historical JSON datasets  
- compare incoming records with existing data  
- identify matched and unmatched records  
- generate structured output for further use  

Output:

- processed results written to analysis sheets  
- updated records prepared for storage and reuse  

---

## Data Flow Between Modules

The system follows a one-directional data flow:

```
Interaction Layer (Sheets / GAS)
↓
Data Preparation (Python)
↓
JSON Dataset (Intermediate Storage)
↓
Data Matching (Python)
↓
Interaction Layer (Output Display)
```


This structure ensures a clear separation between interaction, data preparation, and processing.

---

## JSON Dataset Structure

The JSON dataset serves as the intermediate data layer shared between modules.

Each dataset contains:

- unique identifiers  
- associated metadata  
- grouped records organized by source  

This structure enables efficient lookup, matching, and incremental updates.

---

## Design Principles

The code structure is based on the following principles:

- **separation of concerns**  
  interaction, preparation, and processing are handled independently  

- **modularity**  
  components can be modified or extended without affecting the entire system  

- **reusability**  
  historical datasets are reused across multiple processing runs  

- **maintainability**  
  clear structure simplifies debugging and future development  

---

## Notes

The system combines spreadsheet-based interaction (Google Sheets / GAS) with Python-based processing.

JSON is used as a lightweight intermediate storage format.

For larger-scale systems, the storage layer can be replaced by a database without changing the overall architecture.
