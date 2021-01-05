from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
import datetime

def get_html(url):
    print(url)
    return datetime.datetime.now()


executor = ThreadPoolExecutor(max_workers=3)
all_tasks = [executor.submit(get_html, (url,)) for url in range(100)]
wait(all_tasks, return_when=ALL_COMPLETED)
print('done')