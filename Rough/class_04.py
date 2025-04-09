from timeit import default_timer as tm


my_list = ["a"] * 100000

start = tm()
my_str = ""
for i in my_list:
    my_str += i
stop = tm()
print(f"FOR LOOP {start}, {stop:.2f}")
print(stop-start)


start1 = tm()
my_str2 = "".join(my_list)
stop2 = tm()
print(f"JOIN {start1}, {stop2}")
print(stop2-start1)
