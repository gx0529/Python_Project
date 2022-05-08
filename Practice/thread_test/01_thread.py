
import threading
import time


g_num = 0

# 创建一个互斥锁，默认使没有上锁的
mutex = threading.Lock()


def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前 已经被上锁，那么此时会堵塞在这里，知道这个锁被解开为止
    # mutex.acquire()
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # 解锁
    # mutex.release()
    print("-----in test1 g_num=%d" % g_num)


def test2(num):
    global g_num
    # mutex.acquire()
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    # mutex.release()
    print("-----in test2 g_num=%d" % g_num)


def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据过去
    t1 = threading.Thread(target=test1, args=(10000000,))
    t2 = threading.Thread(target=test2, args=(10000000,))

    t1.start()
    # time.sleep(1)
    t2.start()

    time.sleep(10)

    print("-----=in main g_num=%d" % g_num)

if __name__ == '__main__':
    main()
