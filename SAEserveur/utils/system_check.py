import psutil 
def check_resources(min_memory_mb, min_cpus):
    min_memory_mb = 2048
    min_cpus = 2



    available_memory_mb = psutil.virtual_memory().available / (1024 ** 2)
    if available_memory_mb < min_memory_mb:
        return False


    cpu_count = psutil.cpu_count()
    if cpu_count < min_cpus:
        return False

    return True