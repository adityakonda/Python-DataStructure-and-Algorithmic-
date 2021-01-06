import time, threading

def cal_square(list_num):
    print("Calculating squares of numbers:")

    for i in list_num:
        time.sleep(0.2)
        print('\n')
        print(" square is: " + str(i*i))


def cal_cube(list_num):
    print("Calculating cube of numbers:")

    for i in list_num:
        time.sleep(0.2)
        print('\n')
        print(" cube is: " + str(i * i * i))


if __name__ == '__main__':

    list_of_num = [1,2,3,4,5]

    t = time.time()
    t1 = threading.Thread(target=cal_square, args=(list_of_num,))
    t2 = threading.Thread(target=cal_cube, args=(list_of_num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    # cal_square(list_of_num)
    # cal_cube(list_of_num)

    print("total time executed is : " + str(float(time.time() - t)))
