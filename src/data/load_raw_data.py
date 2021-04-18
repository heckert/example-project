# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd

import src.globals
from src.globals import raw_data_dir


data_source = {'name': 'example.csv',
            'url': '',
            'meta_data_url': ''}


def main(input_url, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    #df = pd.read_csv(input_url)
    #df.to_csv(output_filepath, index=False, encoding='utf8')
    pass
    

if __name__ == '__main__':
    logging.info('loading raw data from {}'.format(data_source['url']))
    main(data_source['url'], raw_data_dir/data_source['name'])
    logging.info('data stored at {}'.format(raw_data_dir/data_source['name']))
    
