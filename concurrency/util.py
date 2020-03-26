def profiled(threads):
    before = datetime.now()
    for thread in threads:
        thread.start()
    while 1:
        if threads[0].is_alive() == False and threads[1].is_alive() == False and threads[2].is_alive() == False and \
                threads[3].is_alive() == False:
            print(datetime.now() - before)
            break


