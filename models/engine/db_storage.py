#!/usr/bin/python3
""" DBstorage module """

from sqlalchemy import (create_engine)


class DBStorage:
    """New engine to store the data in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Environments variables defined"""
        mysql_user = getenv(HBNB_MYSQL_USER)
        mysql_pwd = getenv(HBNB_MYSQL_PWD)
        mysql_host = getenv(HBNB_MYSQL_HOST)
        mysql_db = getenv(HBNB_MYSQL_DB)
        hb_env = getenv(HBNB_ENV)
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(mysql_db, mysql_user, mysql_host, mysql_pwd), pool_pre_ping=True)

        if hb_env == "test":
            base.metadata.drop_all(self.__engine)
