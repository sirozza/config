from files.all_var import files_all, file_config, log_folder, logger, config
from flet import (
    Page,
    Text,
    TextField,
    AppView,
    Container,
    Column,
    FilledButton,
    ScrollMode,
    run
)


@logger.catch
def init_log():
    logger.add(
        r'.//log//log.log',
        backtrace=True,
        diagnose=True,
        format='{time:HH:mm:ss DD.MM.YY} {level} {message}',
        level='INFO',
        rotation='100 MB',
        compression='zip',
        )


def create_config_default():
    config[files_all.get('config_set')] = {'test_config': '1'}


@logger.catch
def checking_folders_and_files():
    log_folder.mkdir(parents=True, exist_ok=True)
    file_config.touch()


@logger.catch
def config_read():
    config.read(file_config, encoding='utf-8')


if __name__ == "__main__":
    checking_folders_and_files()
    init_log()
    config_read()