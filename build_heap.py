# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    def heapify(i):
        left = 2*i + 1
        right = left + 1
        min_idx=i
        if data[left]<data[min_idx]:
            min_idx=left
        if right<n and data[right]<data[min_idx]:
            min_idx=right
        if min_idx==i:
            return
        else:
            data[i], data[min_idx]=data[min_idx], data[i]
            swaps.append((i, min_idx))
            if min_idx<=start:
                heapify(min_idx)

    start=(n-2)//2
    for i in range(start, -1, -1):
        heapify(i)
    return swaps


def main():
    #print("input n:")
    n = int(input())
    #print("input data:")
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
