# System Architecture

## Overview

The system is designed as a multi-component architecture that separates
team evaluation, data storage, matching logic, and user interaction
into independent layers.

This structure supports a collaborative workflow involving 90+
contributors across multiple teams, where data volume and processing
complexity exceed the capabilities of single-layer spreadsheet solutions.

---

## Architecture Overview

```text
┌─────────────────────────────────────┐
│     Contributor Sheets              │
│     (Individual Evaluation Input)   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     GAS Component 1                 │
│     Team Evaluation & Collection    │
│     - color-coded classification    │
│     - daily backup consolidation    │
│     - batch processing              │
│     - timeout + trigger handling    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     JSON Files on Google Drive      │
│     (Historical Dataset)            │
│     - classified records            │
│     - incremental updates           │
│     - 10MB file size management     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     GAS Component 2 + PyQt5 App     │
│     Record Matching & Distribution  │
│     - loads classification files    │
│     - matches incoming records      │
│     - distributes unmatched records │
│     - desktop UI for contributors   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Python Matching Layer           │
│     (Core Logic)                    │
│     - incremental processing        │
│     - history reuse                 │
│     - independent of GAS limits     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Google Sheets Output            │
│     - classification sheets         │
│     - distribution sheets           │
│     - analysis output               │
└─────────────────────────────────────┘
```

---

## Layer Descriptions

### Contributor Sheets (Input Layer)

Individual spreadsheets maintained by each contributor.
Records are evaluated and color-coded according to
predefined classification rules.

Each contributor operates independently,
with results consolidated in the daily backup step.

---

### GAS Component 1 — Team Evaluation and Collection

Handles the collaborative data collection workflow.

Responsibilities:
- consolidates color-coded results from all contributor sheets
- runs automated daily backup combining all contributor data
- writes classified records to JSON files on Google Drive
- manages batch processing with timeout handling
  and trigger-based continuation for large datasets
- removes outdated records based on date thresholds

---

### JSON Files on Google Drive (Storage Layer)

Serves as the central historical dataset shared between components.

Responsibilities:
- stores classified records from team evaluation
- enables reuse of previously validated results
- supports incremental updates without full reprocessing
- manages file size through automatic file splitting at 10MB

This layer acts as the interface between the collection layer
and the matching layer, decoupling the two processes.

---

### GAS Component 2 + PyQt5 Desktop Application (Distribution Layer)

Handles matching of incoming records against the historical dataset
and distributes results to output sheets.

Responsibilities:
- loads multiple JSON classification files from Google Drive
- matches incoming records against predefined categories
- writes matched results to corresponding classification sheets
- distributes unmatched records in configurable batches
- provides a desktop application interface for contributors
  to reduce operational errors

The desktop application (PyQt5) was introduced to standardize
contributor operations and reduce errors caused by manual steps
in the online spreadsheet workflow.

---

### Python Matching Layer (Core Logic)

Handles the core incremental matching logic independently
of Google Apps Script execution constraints.

Responsibilities:
- reads new records and historical dataset
- compares records and classifies as matched or unmatched
- updates historical dataset with newly processed records
- operates independently of network conditions and GAS limits

This layer was introduced as data volume approached the limits
of reliable GAS-based processing.

---

### Google Sheets Output Layer

Displays processed results for team use.

Responsibilities:
- shows classification results per category
- displays unmatched records for manual review
- provides analysis output for cross-source comparison

---

## Design Rationale

| Layer | Technology | Reason |
|---|---|---|
| Data Collection | Google Apps Script | Integrates directly with contributor sheets |
| Historical Storage | JSON on Google Drive | Lightweight, no infrastructure required |
| Matching Logic | Python | Independent of GAS execution limits |
| Contributor UI | PyQt5 | Reduces operational errors, works offline |
| Output Display | Google Sheets | Accessible to all team members |

---

## Scalability Considerations

The current architecture is designed for small-to-medium team workflows.

Known limitations:
- JSON file size is capped at 10MB per file
- GAS triggers are unreliable for very large datasets
- network instability can interrupt online processing

Planned extensions:
- database layer to replace JSON storage
- Python desktop application to replace GAS matching components
- offline processing to eliminate network dependency
