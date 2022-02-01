from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        start_time = time.clock()
        time_stamps = []
        for i in range(num):
            func(*args, **kwargs)
            time_stamps.append(time.clock() - start_time)
            start_time = time.clock()
            print(time_stamps[-1])   
        print(sum(time_stamps)/ len(time_stamps))
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
