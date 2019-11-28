import pandas as pd
import os
import tempfile
import zipfile
import glob
import quandl


def download_quandl_dataset(database, dataset, save_path, columns, tickers, start_date, end_date):
    """
    Download a dataset from Quandl and save it to `save_path`.
    Filter by columns, tickers, and date
    :param database: The Quandl database to download from
    :param dataset: The dataset to download
    :param save_path: The path to save the dataset
    :param columns: The columns to save
    :param tickers: The tickers to save
    :param start_date: The rows to save that are older than this date
    :param end_date: The rows to save that are younger than this date
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_wiki_file = tmp_dir + 'tmp.zip'
        quandl.bulkdownload(database, dataset_code=dataset, filename=tmp_wiki_file)

        # Unzip downloaded data
        zip_ref = zipfile.ZipFile(tmp_wiki_file, 'r')
        zip_ref.extractall(tmp_dir)
        zip_ref.close()

        # Check if the zip file only contains one csv file
        #   We're assuming that Quandl will always give us the data in a single csv file.
        #   If it's different, we want to throw an error.
        csv_files = glob.glob(os.path.join(tmp_dir, '*.csv'))
        assert len(csv_files) == 1,\
            'Bulk download of Quandl Wiki data failed. Wrong number of csv files found. Found {} file(s).'\
                .format(len(csv_files))
        tmp_csv_file = csv_files[0]

        names = quandl.get_table('{}/{}'.format(database, dataset), ticker='EMPTY_RESULTS_TICKER').columns.values
        tmp_df = pd.read_csv(tmp_csv_file, names=names)
        tmp_df['date'] = pd.to_datetime(tmp_df['date'])

        # Remove unused data and save
        tmp_df = tmp_df[tmp_df['date'].isin(pd.date_range(start_date, end_date))]  # Filter unused dates
        tmp_df = tmp_df[tmp_df['ticker'].isin(tickers)]  # Filter unused tickers
        tmp_df.to_csv(save_path, columns=columns, index=False)  # Filter unused columns and save