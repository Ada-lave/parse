from threading import Timer

# выполнять функцию hello() каждые 10 секунд
def hello():
    print("Привет, мир")
    Timer(10, hello).start()

hello()