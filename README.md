# Simulation Log Agent

Day 1 of an engineering-agent learning project.

This small Python program reads a simulation log, finds `WARNING` and `ERROR`
messages, and prints a short diagnostic report.

## Run it

```bash
python3 analyze_log.py
```

## What this teaches

- Read a text file from an engineering workflow.
- Put reusable logic in a Python function.
- Let program output decide an overall status: `NORMAL`, `WARNING`, or `ERROR`.
- Track the work with Git from the first day.

## Planned next step

Read a CSV result file, calculate a temperature jump, and prepare a structured
result that an AI agent could later call as a tool.
