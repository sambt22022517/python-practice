def number_of_ways(start_pos: int, end_pos: int, k: int) -> int:
    if k == 0:
        if end_pos == start_pos:
            return 1
        else:
            return 0
    return (number_of_ways(start_pos, end_pos+1, k-1) % (10**9+7) + 
            number_of_ways(start_pos, end_pos-1, k-1) % (10**9+7)) % (10**9+7)


if __name__ == "__main__":
    print(number_of_ways(1, 2, 3))
