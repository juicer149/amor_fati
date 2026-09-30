# Amor Fati

A personal activity-tracking experiment from 2025 and the second project in my
Amor Fati project line.

This project was a restart of an earlier terminal-based routine tracker. The
main architectural experiment was moving activity definitions out of hardcoded
Python logic and into YAML configuration files.

It also introduced a `src/` package layout and separate domain objects for
activities and logged activity occurrences.

## What was implemented

The functional core consists of:

- `Activity` — loads activity definitions from YAML
- `ActivityBit` — represents one occurrence of an activity
- `ActivityCatalog` — discovers and loads activities from the config directory
- YAML-based activity definitions
- weighted scoring for unit-based activities
- simple scoring for boolean activities
- a YAML helper and activity-template utility

Some planned modules, including the CLI, repository and separate score
calculator, were created as placeholders but were never implemented.

## Project structure

```text
amor_fati/
├── config/
│   └── activities/
├── src/
│   └── amorfati/
│       ├── cli/
│       ├── core/
│       │   ├── activity.py
│       │   ├── activity_bit.py
│       │   └── catalog.py
│       ├── features/
│       ├── storage/
│       └── utils/
├── templates/
├── tests/
├── Makefile
└── README.md
```

## Verification

Run:

```bash
make check
```

This compiles the source and runs the restored test suite.

The tests cover:

- loading unit-based activities from YAML
- weighted activity scoring
- boolean activity scoring
- incomplete boolean activities
- invalid or empty YAML
- catalog loading while skipping invalid activity files

## Historical restoration

This repository has been kept close to its original 2025 state.

The restoration made only small changes needed to make the implemented core
usable and verifiable:

- removed the accidentally committed virtual environment
- added `.gitignore`
- added tests for the implemented domain model
- fixed the missing catalog logger
- made empty YAML files fail cleanly instead of crashing catalog loading
- preserved support for the older `value`-based boolean activity definitions
- updated the Makefile for the `src/` package layout
- documented which parts of the project were implemented and which remained
  placeholders

The unfinished CLI, repository, loader and separate score-calculator modules
were intentionally not completed.

## Project lineage

1. `RUTINHANTERARE` — first routine tracker and scoring CLI, 2024
2. `amor_fati` — YAML-driven activity and domain-model experiment, 2025
3. `AmorFatiMVP` — later simplified event and logging model, 2025

A later Django training-log experiment continued exploring the same general
ideas.

## Status

Historical project preserved as the second stage of the Amor Fati project
line.
