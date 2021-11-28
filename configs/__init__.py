# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
from dataclasses import dataclass
from dynaconf import Dynaconf
from os.path import dirname, abspath, join

from rich.console import Console

CONFIG_PATH = dirname(abspath(__file__))
settings_toml = join(CONFIG_PATH, 'settings.toml')
config_json = join(CONFIG_PATH, '.config.json')

_settings = Dynaconf(
    settings_files=[settings_toml, config_json],
    # path/glob
    environments=True,  # activate layered environments
    env_switcher="MODE",  # `export MODE=production`
    load_dotenv=True,  # read a .env file
    dotenv_path="configs/.env"  # custom path for .env file to be loaded
)
Console().print(f"Using env is [bold cyan]{_settings.current_env}[/bold cyan]")

## dynamic add environment
## in python script
# os.environ["DYNACONF_PORT"] = "@int 5000"
# os.environ["DYNACONF_DB"] = "@int workspace"
# os.environ["DYNACONF_LOG_LEVEL"] = "DEBUG"
# settings.reload()

## in terminal or shell
# export DYNACONF_PORT="@int 5000"
# export DYNACONF_LOG_LEVEL="DEBUG"


@dataclass
class Settings:
    LOG_LEVEL = _settings.LOG_LEVEL
    CREATE_TABLE = _settings.CREATE_TABLE

    # mail config
    MAIL_HOST = _settings.mail.host
    MAIL_PORT = _settings.mail.port
    MAIL_USER = _settings.mail.user
    MAIL_PASSWD = _settings.mail.passwd
    MAIL_RECEIVERS = _settings.mail.receivers

    # def total_cost(self) -> float:
    #     return self.unit_price * self.quantity_on_hand


settings = Settings()
