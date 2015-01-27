import os
import multiprocessing

cart_dir = os.environ["OPENSHIFT_ADVANCED_PYTHON_DIR"]
tmp_dir = os.environ["OPENSHIFT_TMP_DIR"]

workers = os.environ.get("OPENSHIFT_PYTHON_WORKERS",
                         multiprocessing.cpu_count() * 2 + 1)
worker_class = os.environ.get("OPENSHIFT_PYTHON_WORKER_CLASS", "gevent")
daemon = True
bind = "unix:{0}run/appserver.sock".format(cart_dir)
pidfile = "{0}run/appserver.pid".format(cart_dir)

accesslog = "{0}logs/appserver.access.log".format(cart_dir)
errorlog = "{0}logs/appserver.error.log".format(cart_dir)

worker_tmp_dir = "{0}".format(tmp_dir)
tmp_upload_dir = "{0}".format(tmp_dir)
