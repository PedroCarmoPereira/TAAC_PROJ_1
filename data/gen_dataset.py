import os
import re
import pandas as pd


DATA_LOC = './raw_data'
FINAL_PATH = './dataset.json'

FIRST_N = 10000

CATEGORY_RE = r"goodreads_reviews_([A-z_]*)"

main_df = pd.DataFrame()
for file in os.listdir(DATA_LOC):
    category = re.search(CATEGORY_RE, file).group(1)
    chunks = []
    path = DATA_LOC + "/" + file
    chunk_iterator = pd.read_json(path, lines=True, chunksize=FIRST_N, compression='gzip')
    
    first_n_points = next(chunk_iterator)

    t_df = pd.DataFrame(data=first_n_points)
    t_df['category'] = category

    main_df = pd.concat([main_df, t_df])

main_df.reset_index(inplace=True)
main_df.to_json('./dataset.json', orient='records')