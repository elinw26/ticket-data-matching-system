# Code Structure

## Overview

The system combines Google Apps Script (JavaScript) for spreadsheet-based
workflows with Python for core matching logic and a PyQt5 desktop
application for contributor interaction.

The codebase is organized into three main components,
each with a clearly defined responsibility.

---

## Component Overview

```text
system/
├── GAS Component 1 (Google Apps Script)
│   Team Evaluation and Data Collection
│
├── GAS Component 2 (Google Apps Script)
│   Record Matching and Distribution
│
└── Python Layer
    ├── Core Matching Logic
    └── Desktop Application (PyQt5)
```

---

## GAS Component 1 — Team Evaluation and Data Collection

**Language:** Google Apps Script (JavaScript)
**Environment:** Google Sheets (bound script)

This component manages the collaborative evaluation workflow
across all contributor sheets.

### Modules

**UI and Menu**
- custom menu interface triggered on spreadsheet open
- menu actions mapped to all major workflow functions

**Configuration Loading**
- reads processing parameters from a configuration sheet
- loads keywords, source URL, and output settings dynamically
- makes the pipeline reusable without modifying script code

**Source Data Reading**
- opens and reads from external source spreadsheets
- retrieves values, backgrounds, rich text, and notes
  for full formatting preservation

**Record Filtering**
- filters records based on keyword configuration
- maps source columns to output columns
- preserves all cell formatting during filtering

**Backup and Consolidation**
- consolidates color-coded results from all contributor sheets
- runs daily backup combining results across multiple contributors
- handles batch processing with timeout detection
- uses trigger-based continuation for large datasets
- manages JSON file size with automatic file splitting at 10MB

**Data Cleanup**
- removes outdated records based on configurable date thresholds
- deletes columns that fall below the threshold date

---

## GAS Component 2 — Record Matching and Distribution

**Language:** Google Apps Script (JavaScript)
**Environment:** Google Sheets (bound script)

This component handles matching of incoming records against
the historical JSON dataset and manages result distribution.

### Modules

**Classification File Loading**
- reads multiple JSON files from a Google Drive folder
- parses each file into an in-memory dataset for matching
- identifies files by name pattern

**Record Matching**
- matches incoming records against loaded classification datasets
- assigns matched records to corresponding classification categories
- identifies and separates unmatched records
- removes duplicates before processing

**Result Distribution**
- writes matched results to classification sheets
- distributes unmatched records in configurable batches
- creates distribution sheets dynamically based on record count
- applies formatting and column width to output sheets

**Sample Data Generation**
- generates sample datasets by combining records
  from multiple source sheets
- used as reference input for the matching process

**Progression Tracking**
- tracks participant progression across multiple engagement steps
- each step has independent processing logic and output sheet
- uses temporary JSON files as intermediate storage
  between processing stages

**Real-time Matching**
- matches current records against source data in real time
- writes matched source attributes back to the input sheet

**Analysis Mapping**
- maps processed data from analysis sheets to a mapping table
- preserves formatting during mapping for consistent output

**Time Tracking**
- parses and aggregates time entries in multiple formats
- writes totals to a designated output cell

**Cross-spreadsheet Backup**
- backs up processed data to external spreadsheets
- preserves cell formatting, hyperlinks, and notes during backup
- inserts columns dynamically to accommodate new backup entries

---

## Python Layer — Core Matching Logic

**Language:** Python
**Environment:** Local execution (independent of GAS)

This layer implements the core incremental matching logic
independently of Google Apps Script execution constraints.

### Modules

**Data Loading**
- reads new records from JSON input file
- reads historical dataset from JSON storage file
- extracts ID lists for matching

**Matching Logic**
- compares incoming IDs against historical dataset
- classifies records as matched or unmatched
- handles incremental processing across multiple runs

**Dataset Update**
- extends historical dataset with newly processed records
- writes updated dataset back to JSON storage file

**Demo Implementation**
- a simplified version of the matching logic is available
  in `src/data_matching/`
- uses local JSON sample files to demonstrate core logic
  without requiring external API connections

---

## Desktop Application — PyQt5

**Language:** Python
**Framework:** PyQt5
**Environment:** Local desktop application (Windows/macOS)

The desktop application provides a graphical interface
for contributors to run matching and distribution workflows
without direct access to the underlying scripts.

### Key Features

**Configuration Management**
- saves and loads spreadsheet links across sessions
- validates contributor identity through sheet name verification

**Workflow Triggers**
- provides buttons to trigger each processing stage independently
- displays real-time progress in a log area

**Batch Size Configuration**
- allows configurable batch sizes for record distribution
- saves configuration between sessions

**Language Support**
- supports multiple interface languages for multilingual teams

---

## JSON Dataset Structure

JSON files serve as the shared data layer between components.

### Historical Dataset Format

```json
{
  "ids": [
    "id_1",
    "id_2",
    "id_3"
  ]
}
```

### Multi-field Source Dataset Format

```json
{
  "source_column": {
    "A_data": ["id_1", "id_2"],
    "B_to_H_data": ["metadata_1", "metadata_2", "..."]
  }
}
```

The `ids` field in the Historical Dataset corresponds directly
to the `A_data` field in the Multi-field Source Dataset.
This shared ID format allows data to flow between the two systems
without conversion.

---

## Design Principles

**Separation of concerns**
Each component handles a distinct stage of the workflow.
GAS components manage spreadsheet interaction,
Python handles core processing logic,
and the desktop application manages contributor interaction.

**Modular structure**
Components can be modified or extended independently
without affecting other parts of the system.

**Reusability**
Historical datasets are reused across processing runs,
reducing redundant work as data volume grows.

**Scalability path**
The architecture is designed with a clear migration path:
JSON storage can be replaced by a database,
and GAS processing can be replaced by Python
without restructuring the overall system design.
