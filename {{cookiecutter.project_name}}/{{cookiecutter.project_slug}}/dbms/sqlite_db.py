"""SQL Lite Database Module

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import shutil
from pathlib import Path

import sqlalchemy
from sqlmodel import SQLModel, create_engine

from {{cookiecutter.project_slug}}.logging import psnap_get_logger

# Forward declaration


class SQLiteDBUtils:
    __instance: object | None = None
    __init_done: bool = False

    def __init__(self, db_name: str = "{{cookiecutter.project_slug}}.db", echo: bool = False):
        if SQLiteDBUtils.__init_done is True:
            return
        SQLiteDBUtils.__init_done = True
        self.logger = psnap_get_logger("dbms.SQLiteDBUtils")
        self.logger.debug(f"[{id(self)}] Creating db_name={db_name} echo={echo}")
        self.echo = echo
        self.db_dir = Path(__file__).parent.parent / ".tmp_sqlite_db"
        if not self.db_dir.exists():
            self.logger.debug(f"[{id(self)}] Creating dir {self.db_dir}")
            self.db_dir.mkdir()

        self.db_name = db_name
        self.db_file_path = self.db_dir / self.db_name
        self.db_backup_file_path = self.db_dir / f"{db_name}.backup"

    def __new__(cls, *args, **kwargs):  # type: ignore[no-untyped-def]
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def backup_db(self, move: bool = False) -> None:
        self.logger.debug(f"[[[ [{id(self)}] Backup DB START")

        if self.db_file_path.exists():
            if move:
                self.logger.info(f"[{id(self)}] MOVING {self.db_file_path} to {self.db_backup_file_path} ")
                shutil.move(self.db_file_path, self.db_backup_file_path)
            else:
                self.logger.info(f"[{id(self)}] COPYING {self.db_file_path} to {self.db_backup_file_path} ")
                shutil.copy(self.db_file_path, self.db_backup_file_path)
        else:
            self.logger.info(f"[{id(self)}] sqlite db {self.db_file_path} not found.")
        self.logger.debug(f"]]] [{id(self)}] Backup DB END")

    def restore_db(self) -> None:
        self.logger.debug(f"[[[ [{id(self)}] Restore DB START")

        if self.db_backup_file_path.exists():
            self.logger.info(f"[{id(self)}] restoring {self.db_backup_file_path} to {self.db_file_path} ")
            shutil.move(self.db_backup_file_path, self.db_file_path)
        else:
            self.logger.info(f"[{id(self)}] sqlite db backup {self.db_backup_file_path} not found.")
        self.logger.debug(f"]]] [{id(self)}] Restore DB END")

    def get_database_engine(self, new_db: bool = False) -> sqlalchemy.Engine:
        """Get SQLAlchemy Engine for database connection
        Parameters
        ----------
        db_name: The SQLite database name
        echo: If set to True, SQLite will echo statements
        new_db: If set to True, delete existing DB and create a new one.

        Returns
        -------
        engine: SQLAlchemy Engine for database connection

        """
        if not self.db_file_path.exists():
            self.logger.info(f"[{id(self)}] sqlite db {self.db_file_path} not found. Will create!")
            new_db = True
        if self.db_file_path.is_file() and new_db:
            self.logger.info(f"[{id(self)}] deleting existing database {self.db_file_path}")
            self.db_file_path.unlink()
        driver = f"sqlite:///{self.db_file_path!s}"
        self.logger.info(f"[{id(self)}] creating sqlite driver {driver}")
        engine = create_engine(driver, echo=self.echo)
        if new_db is True:
            self.logger.info(f"[{id(self)}] creating database {self.db_file_path}")
            SQLModel.metadata.create_all(engine)

        return engine
