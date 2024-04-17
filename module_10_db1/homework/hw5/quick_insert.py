from typing import Union, List

Number = Union[int, float, complex]


def find_insert_position(array: List[Number], number: Number) -> int:
    if len(array) == 0:
        return 0
    else:
        if array[0] > number:
            return 0
        elif array[-1] < number:
            return len(array)
        else:
            left = 0
            right = len(array) - 1
            mid = (left + right) // 2
            while left <= right:
                mid = (left + right) // 2
                if number == array[mid]:
                    return mid + 1
                elif number > array[mid]:
                    left = mid + 1
                elif number < array[mid]:
                    right = mid - 1
            return mid


if __name__ == '__main__':
    A: List[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    insert_position: int = find_insert_position(A, x)
    assert insert_position == 5

    A: List[Number] = [1, 2, 3, 3, 3, 5]
    x: Number = 4
    A.insert(insert_position, x)
    assert A == sorted(A)
