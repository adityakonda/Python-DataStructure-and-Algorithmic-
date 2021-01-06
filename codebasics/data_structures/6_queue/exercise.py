import threading
import time
from collections import deque


class Restaurant:

    def __init__(self):
        self.order_queue = deque()
        self.order_items = []

    def place_order(self):

        for item in self.order_items:
            time.sleep(0.5)
            self.order_queue.appendleft(item)
            print("placed order for : ", item)

    def serve_order(self):
        # taking order after 2 sec
        time.sleep(2)
        for item in self.order_items:
            print("serving order : " + self.order_queue.pop())
            time.sleep(1)


if __name__ == '__main__':

    restaurant = Restaurant()
    restaurant.order_items = ['pizza','samosa','pasta','biryani','burger']

    t1 = threading.Thread(target=restaurant.place_order)
    t2 = threading.Thread(target= restaurant.serve_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All orders are served..!!!")

