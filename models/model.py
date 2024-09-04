try:
    import sqlite3
    from sqlite3 import Error
    from datetime import datetime 
    import os
    from .log_settings import chat_logger
except Exception as e:
    print('[ERROR IMPORTING PACKAGES]', e)
root_path = '/storage/emulated/0/'
# for first time create folder>logger>database
def first_time():
    try:
        main_folder = os.path.join(root_path, 'INCHAT')
        if not os.path.exists(main_folder):
            os.mkdir(main_folder)

        logger_folder = os.path.join(main_folder, 'logger')
        if not os.path.exists(logger_folder):
            os.mkdir(logger_folder)

        database_folder = os.path.join(main_folder, 'database')
        if not os.path.exists(database_folder):
            os.mkdir(database_folder)

        
    except Exception as e:
        return [0, e]
    else:
        return [1, None]

