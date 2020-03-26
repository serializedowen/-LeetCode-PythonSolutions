import threading

# Problem 1114
class Foo:
    def __init__(self):
        self.lockTwo = threading.Lock()
        self.lockThree = threading.Lock()

        self.lockTwo.acquire()
        self.lockThree.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lockTwo.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.

        self.lockTwo.acquire()
        printSecond()
        self.lockTwo.release()
        self.lockThree.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.lockThree.acquire()
        printThird()
        self.lockThree.release()


def threadGen(inst: Foo):

    first = [lambda: print('first', end='')]
    second = [lambda: print('second', end='')]
    third = [lambda: print('third', end='')]


    threads = [threading.Thread(args=first, target=inst.first),
               threading.Thread(args=third, target=inst.third),
               threading.Thread(args=second, target=inst.second)
               ]
    return threads


if __name__ == '__main__':

    # for i in range(0, 10000):
    #     print(i)
    inst = Foo()
    threads = threadGen(inst)
    for i in range(0, 3):
        threads[i].start()
