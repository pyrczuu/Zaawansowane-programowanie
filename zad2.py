def check_list_length(lst: list, n: int):
    if len(lst) != n:
        raise ValueError(f"Lista musi mieć {n} wejść.")


def zad_a(names: list):
    check_list_length(names, 5)
    for name in names:
        print(name)


def zad_b_i(nums: list):
    check_list_length(nums, 5)
    for i in range(5):
        nums[i] *= 2
    return nums


def zad_b_ii(nums: list):
    check_list_length(nums, 5)
    return [x * 2 for x in nums]


def zad_c(nums: list):
    check_list_length(nums, 10)
    for i in range(10):
        if nums[i] % 2 == 0:
            print(nums[i])


def zad_d(nums: list):
    check_list_length(nums, 10)
    for i in range(10):
        if i % 2 == 0:
            print(nums[i])
