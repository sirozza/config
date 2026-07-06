import configparser
from loguru import logger
from pathlib import Path

files_all = {
    'files_dir' : 'files',
    'log_dir' : 'log',
    'config_file' : 'config.ini',
    'config_set' : 'DEFAULT',
}

log_folder = Path(files_all.get('log_dir'))
file_config = Path(files_all.get('config_file'))

config = configparser.ConfigParser()




# if __name__ == "__main__":
#     main()