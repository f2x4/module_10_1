from time import sleep
import time
import threading

def counter(func):
    """ Считает время выполнения функции func """
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        exec_time = round(end - start, 2)
        print(f'    Время выполнения функции {func.__name__} {exec_time} сек.')
    return wrapper


@counter
def write_words(word_count, file_name):
    """ Функция должна вести запись слов """
    # Открыть файл file_name на добавление
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(0, word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    print(threading.current_thread())
    return

@counter
def exec_function():
    """ Вызов функций write_words """
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

@counter
def exec_threads():
    """ Вызов функций write_words в потоках """
    thread_1 = threading.Thread(
        target = write_words, args = (10, 'example5.txt')
    )
    thread_2 = threading.Thread(
        target = write_words, args = (30, 'example6.txt')
    )
    thread_3 = threading.Thread(
        target = write_words, args = (200, 'example7.txt')
    )
    thread_4 = threading.Thread(
        target = write_words, args = (100, 'example8.txt')
    )
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()


exec_function()
print('@'*60)
exec_threads()





