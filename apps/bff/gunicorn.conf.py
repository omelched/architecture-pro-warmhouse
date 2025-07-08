import multiprocessing

bind = "0.0.0.0:8000"
capture_output = True

workers = 2 * multiprocessing.cpu_count() + 1
worker_connections = 1000

errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" %(a)s'