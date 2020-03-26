import threading

# Problem 1226
class DiningPhilosophers:
    def __init__(self):
        self.sem = threading.Semaphore()




    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        with self.sem:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()

