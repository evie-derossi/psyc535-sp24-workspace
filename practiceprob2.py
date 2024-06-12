"""Create a function called rever that takes a list and returns it in revers"""

original : list[int] = [1,2,3,4,5,6,7,8,9,10]


def reverse(og_list : list[int]) -> list[int]:
    """Takes list input and puts it in reverse."""
    new : list[int] = []
    idx: int = 1
    while idx <= len(og_list):
        new.append(og_list[-idx])
        idx +=1
    print(new)
    return

reverse(original)