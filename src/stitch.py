import pandas as pd
import os

from translate import lang_dir_walk, lang_dirs

dct_collages = {}

def proc_collage_file(file_path, langs):
    file_name = file_path.split(os.sep)[-1]
    directory = os.sep.join(file_path.split(os.sep)[:-1]) + os.sep
    df = pd.read_csv(file_path).loc[:, ['Key', 'en']]

    for lang in langs:
        lang_fname = file_name[:-4] + f'_{lang}.csv'
        lang_dir = directory.replace(f'{os.sep}_collage{os.sep}', f'{os.sep}{lang}{os.sep}')
        df_lang = pd.read_csv(f'{lang_dir}{os.sep}{lang_fname}').loc[:, ['Key', lang]]
        df = pd.merge(df, df_lang, on='Key', how='outer')

    df.to_csv(file_path, index=False)

def proc(root):
    langs = lang_dirs(root)
    lang_dir_walk(root + '_collage', __file__, lambda x: proc_collage_file(x, langs))

if __name__ == "__main__":
    proc(f'..{os.sep}')

# summary
# above threshold pct, add column - no manual so nothing gets removed
# collage folder next to languages - has same format as final - need zh-Hans as a language folder
