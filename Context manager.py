from datetime import datetime
import time  # проверять действие измерителя будем с помощью библиотеки time


# вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием
# и закрытием контекстного менеджера
class Timer:
    def __init__(self):
        pass

    def __enter__(self):  # этот метод вызывается при запуске с помощью with.
        # Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере,
        # как в примере с файлом, то просто верните этот объект через return
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
        print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")


with Timer():
    path = "C:/Users/Rossvik/Desktop/journal.txt"
    with open(path, 'r', encoding='utf8') as file_:
        str_ = file_.readlines()
        str_.reverse()
        with open(path, 'w', encoding='utf8') as file_2:
            file_2.writelines(str_)
