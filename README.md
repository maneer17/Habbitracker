# Coding Tracker (Pixela)

A simple Python script that logs your daily coding hours to a [Pixela](https://pixe.la) 
graph, turning your coding habit into a GitHub-style contribution heatmap.

## What it does

- Prompts you each day for how many hours you coded
- Posts that value to a Pixela graph (`manar-draw`) as a float quantity in hours
- Automatically uses today's date, so you can run it once a day to build up a 
  visual streak of your coding consistency over time

## How it works

The script uses the [Pixela API](https://docs.pixe.la/) to:
1. Create a Pixela user account (one-time setup)
2. Create a graph to track coding hours (one-time setup)
3. Post a new data point for today's date every time you run it

Update and delete operations are also included (commented out) for correcting 
past entries if needed.

## Requirements

- Python 3
- `requests` library (`pip install requests`)
- A [Pixela](https://pixe.la) account/token

## Usage

```bash
python coding_tracker.py
```

You'll be prompted:
