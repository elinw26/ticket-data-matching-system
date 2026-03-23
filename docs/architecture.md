# System Architecture

## Overview

This document describes the architecture of the Data Matching Automation System.

The system is designed to separate user interaction, processing logic, and historical data storage into independent layers.

This structure improves maintainability and supports scalable data processing beyond spreadsheet limitations.

---

## Architecture Overview

The system consists of three main layers:

```text
Google Sheets (Input / Output)
        │
        ▼
Python Processing Layer
        │
        ▼
JSON Data Storage (Historical Dataset)
```

The workflow moves from data input to processing and finally to historical data storage.

---

## Data Input & Interaction Layer (Google Sheets)

This layer is responsible for user interaction and data visualization.

Main responsibilities:

- input of new data  
- display of matching results  
- manual handling of unmatched records  

---

## Data Processing Layer (Python)

This layer handles the core processing logic.

Main responsibilities:

- reading input data  
- loading historical JSON dataset  
- performing data matching  
- identifying unmatched records  
- preparing structured output  

---

## JSON Data Storage (Historical Dataset)

JSON files act as a reusable data layer for storing processed results.

This layer:

- stores historical processed data  
- enables reuse across workflows  
- reduces repeated processing  
- supports incremental data updates  

---

## Design Rationale

The architecture separates responsibilities into independent layers:

| Layer | Responsibility |
|------|--------------|
| Input Layer | Data entry and visualization |
| Processing Layer | Matching and data transformation |
| JSON Storage | Reusable historical dataset |

This modular structure improves maintainability and allows the system to be extended without changing the entire workflow.

---

## Notes

The system uses JSON as a lightweight storage solution suitable for the current project scope.

For larger-scale systems, this layer can be replaced with a database without affecting the overall architecture.
