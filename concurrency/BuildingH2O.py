import threading
import random

import threading


class H2O:
    def __init__(self):
        self.condition = threading.Condition()
        self.hcount = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.condition:
            while self.hcount == 2:
                self.condition.wait()
            releaseHydrogen()
            self.hcount = self.hcount + 1
            self.condition.notify_all()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.condition:
            while self.hcount != 2:
                self.condition.wait()
            releaseOxygen()
            self.hcount = 0
            self.condition.notify_all()


def threadGen(H2O: H2O):
    count = 10
    threads = []

    releaseHydrogen = lambda: print('H', sep='')
    releaseOxygen = lambda: print('O', sep='')



    for i in range(1, count + 1):
        choice = random.randint(0, 1)

        if choice == 1:
            threads.append(threading.Thread(target=H2O.hydrogen, args=releaseHydrogen))
            releaseHydrogen()
        else:
            threads.append(threading.Thread(target=H2O.oxygen, args=releaseOxygen))
            releaseOxygen()

    # print('')


if __name__ == '__main__':
    h2o = H2O()
    threadGen(h2o)