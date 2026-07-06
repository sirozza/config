
from files.all_def import (
    config,
    files_all,
    checking_folders_and_files, 
    init_log, 
    logger, 
    config_read,
    Page,
    run,
    Container,
    AppView,
    Text,
    Column,
    FilledButton,
    ScrollMode,
    create_config_default
)


@logger.catch
def get_settings():
    config_table.controls.extend(
        [
            TextField(label=f"{data}", text_size=20, value=config[files_all.get('config_set')][data]) 
            for data in config[files_all.get('config_set')]
        ]
    )


@logger.catch
def save_settings(e):
    config[files_all.get('config_set')] = {data.label: data.value for data in config_table.controls}
    write_config(files_all.get('config_file'))
    e.page.update()



@logger.catch
def main(page: Page):
    page.scroll = "auto"
    page.title = "Program settings."
    page.add(title, Container(config_table), button_save)


title = Text(value="Program settings.", size=20)
config_table = Column(
    width=200, scroll=ScrollMode.ALWAYS, auto_scroll=True, adaptive=True
)


button_save = FilledButton(
    "Save settings", icon="add", on_click=save_settings, adaptive=True
)


if __name__ == "__main__":
    checking_folders_and_files()
    init_log()
    config_read()
    create_config_default()
    get_settings()
    run(main, view=AppView.FLET_APP)