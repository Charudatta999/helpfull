# thread_test.py

import random
import threading
def randomnum():
    print('hello')

if __name__ == "__main__":
    size = 10000000   # Number of random numbers to add
    threads = 15   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=randomnum)
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    print ("List processing complete.")