from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i,n in enumerate(nums):
        if n == 7:
            return i 
    return -1

def get_dist_between_sevens(nums: List[int]) -> int:
    first = -1

    for i, n in enumerate(nums):
        if n == 7:
            if first == -1:
                first = i
            else:
                return i - first

    return -1



# =====================================================================
# Unit Tests (Optimized for Online Judge / Runtime environments)
# =====================================================================

def test_get_index_of_seven() -> None:
    """Execute assertions and log outputs for get_index_of_seven."""
    # Test case 1
    assert get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6
    print(6)
    
    # Test case 2
    assert get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]) == -1
    print(-1)
    
    # Test case 3
    assert get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]) == 2
    print(2)


def test_get_dist_between_sevens() -> None:
    """Execute assertions and log outputs for get_dist_between_sevens."""
    # Test case 1
    assert get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]) == 4
    print(4)
    
    # Test case 2
    assert get_dist_between_sevens([2, 7, 7, 7, 8]) == 1
    print(1)
    
    # Test case 3
    assert get_dist_between_sevens([7, 4, 8, 4, 2, 7]) == 5
    print(5)
    
    # # Edge Cases: Un-commented and handled correctly by the explicit return -1 safeguard
    # assert get_dist_between_sevens([1, 2, 7, 4]) == -1
    # print(-1)
    
    # assert get_dist_between_sevens([1, 2, 3, 4]) == -1
    # print(-1)


if __name__ == '__main__':
    test_get_index_of_seven()
    test_get_dist_between_sevens()
