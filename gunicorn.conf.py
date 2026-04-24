import multiprocessing

bind = "0.0.0.0:8000"
worker_class = "uvicorn.workers.UvicornWorker"
# raw_env = ["ENVIRONMENT=staging"] # local、staging、production
workers = multiprocessing.cpu_count() * 2 + 1
