from Progress_bar import *


if __name__ == "__main__":
    n_loop = 10000
    test_list = [i for i in range(n_loop)]
    progress_instance = Progress_Bar(n_loop)

    for i in range(n_loop):
        progress_instance.set_progress_info(i, time.time())
        for j in range(n_loop):
            pass
        progress_instance.report_progress()

