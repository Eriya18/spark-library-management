> Library Management Real-Time ETL Pipeline Architecture
>
> ETL Pipeline Overview
>
> This document provides the complete architecture and flow of the
> Library Management Real-Time ETL Pipeline, covering batch and
>
> streaming sources, transformation logic, and storage design.
>
> Pipeline Architecture
>
> Pipeline Stages

┌──────────────────┐ ┌──────────────────┐ ┌────────────────────┐
┌─────────────────┐

│ EXTRACTION │ --\> │ VALIDATION & │ --\> │ TRANSFORMATION & │ --\> │
LOADING │

│ │ │ CLEANING │ │ ANALYTICS │ │ │

└──────────────────┘

> │

└──────────────────┘

> │

└────────────────────┘

> │

└─────────────────┘

> │
>
> Batch Sources:
>
> \- users.csv
>
> \- books.json
>
> \- loans.txt
>
> \- returns.parquet
>
> \- categories.csv

Missing / Null Check

Timestamp standardization

Schema validation

Duplicates removal

> Join books + categories
>
> Clean timestamps
>
> Calculate overdue days
>
> Compute fines

Borrowing frequency

Category popularity

Delta Lake Storage

Partitioned by date

> ACID transactions

Time-travel enabled

> Real-time Stream:
>
> \- Kafka: library-loans

Streaming Analytics:

\- 5-min top books window

\- Rolling borrowing trends

\- Real-time overdue alerts

> Sources
>
> **users.csv** -- 1M user records\\
>
> **books.json** -- 1M book metadata\\
>
> **loans.txt** -- historical borrow logs (pipe-delimited)\\
>
> **returns.parquet** -- latest return events\\
>
> **categories.csv** -- book category mapping\\
>
> **Kafka** **Topic:** library-loans -- real-time borrowing events
>
> Transformations
>
> Standardize and clean timestamps\\

Parse, validate, and sanitize raw logs\\

Join books + categories\\

Compute:

> Overdue days\\
>
> Fine amounts\\
>
> Borrowing frequency per user\\
>
> Category popularity\\

Windowed analytics (5-minute top borrowed books)

> Storage

**Delta** **Lake** (no Hadoop, no winutils)

Partitioned by date\\

Supports ACID, schema evolution, and time travel

> Dashboard (Plotly Dash)

Live Top Borrowed Books\\

Real-Time Overdue Loans\\

Borrowing Trend (Rolling Window)

> Tech Stack

**PySpark** **+** **Delta** **Lake**\\

**Kafka** (Docker on Windows / Local on Linux)\\

**Plotly** **Dash** for visualization
