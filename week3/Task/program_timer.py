# importing the timeit Module:
import timeit

# defining the program_time Decorator:
def program_time(number, repeat):
    # defining the wrapper function:
    def wrapper(func):
        # measuring execution time:
        runs = timeit.repeat(func, number=number, repeat=repeat)
        # calculating and printing the average time:
        print(f"Total time taken for execution: {sum(runs)/len(runs)}")
    return wrapper


