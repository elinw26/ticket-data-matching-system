# Data Processing Workflow

## Overview

The system operates through two parallel workflow paths
that share a common JSON storage layer:

- **Path 1** — Team evaluation and data collection
- **Path 2** — Record matching and distribution

Both paths are designed to handle large datasets from 90+
contributors, with timeout handling and trigger-based
continuation where needed.

---

## Path 1 — Team Evaluation and Data Collection

This path handles the daily collection and consolidation
of contributor evaluation results.

```text
Contributors evaluate records in individual sheets
        ↓
Color-coded classification applied to records
        ↓
Daily backup triggered via custom menu
        ↓
Results consolidated from all contributor sheets
        ↓
Classified records written to JSON files on Google Drive
        ↓
Outdated records removed based on date threshold
```

### Step 1 — Individual Evaluation

Each contributor evaluates records in their own sheet,
applying color-coded classifications based on
predefined evaluation criteria.

Contributors operate independently,
with no direct dependency on other contributors' sheets.

### Step 2 — Daily Backup and Consolidation

A daily backup process consolidates results from
all contributor sheets into summary sheets.

Key characteristics:
- processes multiple contributor sheets in a single run
- handles large datasets through batch processing
- uses timeout detection and trigger-based continuation
  to complete processing across multiple runs if needed
- manages JSON file size through automatic file splitting at 10MB

### Step 3 — JSON Dataset Update

Consolidated and classified records are written to
structured JSON files stored on Google Drive.

This step:
- appends newly classified records to existing JSON files
- creates new files when existing files approach 10MB
- maintains a continuously growing historical dataset
- provides the data foundation for Path 2

### Step 4 — Data Cleanup

Outdated records are removed based on configurable date thresholds,
keeping the dataset current and manageable.

---

## Path 2 — Record Matching and Distribution

This path handles matching of incoming records against
the historical JSON dataset and distributes results
to classification sheets.

```text
New records prepared in input sheet
        ↓
Desktop application or GAS triggered
        ↓
JSON classification files loaded from Google Drive
        ↓
Records matched against classification categories
        ↓
Matched records written to classification sheets
        ↓
Unmatched records distributed in configurable batches
        ↓
Historical dataset updated with new records
```

### Step 1 — Input Preparation

New records are prepared in the input sheet,
either manually or through automated collection.

Duplicate records are automatically removed
before processing begins.

### Step 2 — Classification File Loading

Multiple JSON classification files are loaded
from the Google Drive folder.

Each file represents a different classification category,
loaded and parsed into memory for matching.

### Step 3 — Record Matching

Incoming records are matched against the loaded
classification datasets.

Matching logic:
- checks each incoming record against all classification categories
- assigns matched records to their corresponding category
- identifies unmatched records for separate handling
- ensures no record is processed in multiple categories

### Step 4 — Results Distribution

Matched records are written to their corresponding
classification sheets for team use.

Unmatched records are distributed in configurable batches
for manual review and follow-up.

### Step 5 — Dataset Update

The historical dataset is updated with newly processed records,
ensuring future runs can reuse validated results
without reprocessing.

---

## Python Core Logic Workflow

The Python matching layer implements the core incremental
processing logic independently of GAS constraints.

```text
Load new records from JSON file
        ↓
Load historical dataset from JSON file
        ↓
Compare records against historical dataset
        ↓
Classify as matched or unmatched
        ↓
Write results to output
        ↓
Update historical dataset with new records
```

This layer was introduced when data volume made
GAS-based processing unreliable due to:
- execution time limits
- network instability during online processing
- difficulty recovering from mid-run failures

---

## Workflow Coordination

The two paths share the JSON storage layer on Google Drive,
which acts as the interface between collection and matching.

```text
Path 1 (Collection)          Path 2 (Matching)
        │                           │
        ▼                           ▼
    Writes to                  Reads from
        │                           │
        └──────► JSON Storage ◄─────┘
```

This separation means:
- collection and matching can run independently
- the historical dataset grows continuously across both paths
- either path can be updated without affecting the other

---

## Error Handling and Recovery

**Timeout handling**
Both GAS components detect approaching execution limits
and save progress before stopping,
with triggers scheduled to continue processing.

**Duplicate detection**
Incoming records are deduplicated before matching
to prevent redundant processing.

**File size management**
JSON files are automatically split at 10MB
to prevent individual files from becoming too large
for reliable GAS processing.

**Planned improvements**
A Python desktop application is planned to replace
the online GAS processing layer,
eliminating network dependency and providing
more reliable error recovery for large datasets.
