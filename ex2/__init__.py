from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        import time
        def inner_wrapper(*args, **kwargs):
            start_time = time.monotonic()
            time_stamps = []
            for i in range(num):
                func(*args, **kwargs)
                time_stamps.append(time.monotonic() - start_time)
                start_time = time.monotonic()
                print("{:f}".format(time_stamps[-1]))   
            print(sum(time_stamps)/ len(time_stamps))
        return inner_wrapper
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
