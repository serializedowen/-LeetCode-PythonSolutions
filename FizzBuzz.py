import threading

# Problem 1195
class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.done = False
        self.fz = threading.Lock()
        self.bz = threading.Lock()
        self.fzbz = threading.Lock()
        self.num = threading.Lock()
        self.fz.acquire()
        self.bz.acquire()
        self.fzbz.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        while True:
            self.fz.acquire()
            if self.done: break
            printFizz()
            self.num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        while True:
            self.bz.acquire()
            if self.done: break
            printBuzz()
            self.num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        while True:
            self.fzbz.acquire()
            if self.done: break
            printFizzBuzz()
            self.num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for x in range(1, self.n + 1):
            self.num.acquire()
            if x % 15 == 0:
                self.fzbz.release()
            elif x % 3 == 0:
                self.fz.release()
            elif x % 5 == 0:
                self.bz.release()
            else:
                printNumber(x)
                self.num.release()
        self.num.acquire()
        self.done = True
        self.fz.release()
        self.bz.release()
        self.fzbz.release()


class FizzBuzz2(object):
    def __init__(self, n):
        self.n = n
        self.event = threading.Event()
        self.lock = threading.Lock()
        self.count = 0

    def synchronize(self):
        self.lock.acquire()
        self.event.clear()

        # print(self.count)
        if self.count == 4:
            self.count = 0
            self.event.set()

        self.lock.release()
        return

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):

            if i % 3 == 0 and i % 5 != 0:
                printFizz()

            self.count = self.count + 1
            self.synchronize()
            self.event.wait()
        return

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                printBuzz()

            self.count = self.count + 1
            self.synchronize()
            self.event.wait()

        return

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()
            self.count = self.count + 1
            self.synchronize()
            self.event.wait()
        return

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                printNumber(i)
            self.count = self.count + 1
            self.synchronize()
            self.event.wait()
        return



def profiled(threads):
    before = datetime.now()
    for thread in threads:
        thread.start()
    while 1:
        if threads[0].is_alive() == False and threads[1].is_alive() == False and threads[2].is_alive() == False and \
                threads[3].is_alive() == False:
            print(datetime.now() - before)
            break


def threadGen(fizzbuzz):
    threads = [threading.Thread(name='buzz', target=fizzbuzz.buzz, args=[lambda: print('buzz')]),
               threading.Thread(name='fizz', target=fizzbuzz.fizz, args=[lambda: print('fizz')]),
               threading.Thread(name='fizzbuzz', target=fizzbuzz.fizzbuzz, args=[lambda: print('fizzbuzz')]),
               threading.Thread(name='number', target=fizzbuzz.number, args=[lambda x: print(x)])]
    return threads





if __name__ == '__main__':
    from datetime import datetime

    threads = threadGen(FizzBuzz(15))
    profiled(threads)

    threads2 = threadGen(FizzBuzz2(15))
    profiled(threads2)

