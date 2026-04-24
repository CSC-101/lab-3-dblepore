# task 1
more = [x + 1 for x in [1,2,3,4]]     # x takes on 1, then 2, then 3, then 4
print()                               # more = [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # n:1 ->1, n:2 ->4, n:3 -> 9, n:4 -> 16


squares = [square(x) for x in [1,2,3,4]]   # square = [1,4,9,16], these are all the values that n
print()                                    # becomes after the function call

def check(n:int) -> bool:
    return n > 2                             # n:0 ->false, n:1 ->false, n:2 ->false,n:3 ->true
                                             # n:4 -> true


answer = [x for x in range(5) if check(x)]   # answers = [false, false, false, true, true]
print()

def inc(m:int) -> int:
    return m + 1                             # m:0->1, m:1->2, m:2->3, m:3->4, m:4->5
                                             #


def check(n:int) -> bool:
    return n > 2                             # n:1 ->false, n:2 ->false, n:3 ->true ,n:4 ->true
                                             # n:5 -> true


answer = [inc(x) for x in range(5) if check(x)]   # answer = [false,false, true, true,true]
print()

# task 2
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # num: 4 total: 4, num: 9 total 13, num: 2 total: 15,
    return total                      # num: 1 total: 16

result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # idx: 0 new_list: [4], idx: 1 new_list: [4,9], idx: 2 new_list: [4,9,2]
    return new_list                    # idx: 4 new_list: [4,9,2,1].
                                       # this differs from the above loop because it is using indexes to access
                                       # the values in nums, as opposed to accessing them directly.


result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # new_list: [5], new_list: [5,10],
    return new_list                    #new_list: [5, 10, 3], new_list: [5,10,3,2]

result = increment_all([4, 9, 2, 1])