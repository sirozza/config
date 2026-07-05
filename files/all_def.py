from pathlib import Path
from files.init_dirs import files_all


log_folder = Path(files_all.get('log_dir'))


def checking_folders():
    log_folder.mkdir(parents=True, exist_ok=True)
    

if __name__ == "__main__":
    checking_folders()