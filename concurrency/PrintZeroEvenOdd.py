import threading

def lenInt(n):
    return len(str(n))


#Problem 1116
class ZeroEvenOdd:

    def digitAtIndex(self):
        return int(str(self.current)[self.index])
        # return self.current // 10 ** self.index % 10

    def __init__(self, n: int):
        self.n = n

        self.lockOdd = threading.Lock()
        self.lockEven = threading.Lock()
        self.lockZero = threading.Lock()
        self.current = 0


        self.index = 0

        self.lockOdd.acquire()
        self.lockEven.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1):
            self.lockZero.acquire()
            print(' ', sep='')
            printNumber(0)
            self.current = i
            self.index = 0
            if (self.digitAtIndex() % 2 == 0):
                self.lockEven.release()
            else:
                self.lockOdd.release()

        return

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while 1:
            self.lockEven.acquire()
            if self.lockZero.locked() == False:
                self.lockZero.acquire()
            if self.current > self.n:
                print('')
                break
            printNumber(self.digitAtIndex())

            self.index = self.index + 1
            if lenInt(self.current) == self.index:
                self.lockZero.release()
            elif self.digitAtIndex() % 2 == 0:
                self.lockEven.release()
            else:
                self.lockOdd.release()

        return

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while 1:
            self.lockOdd.acquire()

            if self.lockZero.locked() == False:
                self.lockZero.acquire()

            if self.current > self.n:
                print('')
                break
            printNumber(self.digitAtIndex())

            self.index = self.index + 1
            if lenInt(self.current) == self.index:
                self.lockZero.release()
            elif self.digitAtIndex() % 2 == 0:
                self.lockEven.release()
            else:
                self.lockOdd.release()

        return


def threadGen(inst):
    args = [lambda x: print(x, end='')]

    threads = [threading.Thread(args=args, target=inst.zero),
               threading.Thread(args=args, target=inst.even),
               threading.Thread(args=args, target=inst.odd)]
    return threads


if __name__ == '__main__':

    # for i in range(0, 10000):
    #     print(i)
    inst = ZeroEvenOdd(9999)
    threads = threadGen(inst)
    for i in range(0, 3):
        threads[i].start()
