# TAAC_PROJ_1

## TASK 1: Split dataset into smaller sets

See `data/gen_dataset.py`

- Reads folder in `DATA_LOC`
- For each file:
    - Select `FIRST_N` entries
    - Parse file name as category and add as a column of DataFrame
- Save data to `FINAL_PATH`