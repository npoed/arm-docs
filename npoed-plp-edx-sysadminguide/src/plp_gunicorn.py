"""
gunicorn configuration file: http://docs.gunicorn.org/en/develop/configure.html

This file is created and updated by ansible, edit at your peril
"""
import multiprocessing

preload_app = True
timeout = 300
# Адрес, по которому развёрнут gunicorn
bind = "127.0.0.1:18890"
# Путь до PLP
pythonpath = "/edx/app/plp/npoed-plp-edx/npoed_plp"
# Ограничение по числу одновременных запросов
max_requests = 1000
#workers = 4
# Число потоков
threads = 4

