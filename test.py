def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):

    if start < end:
        pi = partition(elements, start, end)
        partition(elements, start, pi - 1)  # left partition
        partition(elements, pi + 1, end)  # right partition


if __name__ == '__main__':
    #elements = [11, 9, 29, 7, 2, 15, 18]
    #quick_sort(elements, 0, len(elements) - 1)

    # for y in range(0,3):
    #     for x in range(0,3):
    #         print(3 + y,3 + x)

    grid = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    def check_grid_is_suduko(grid):

        list_number = []

        # check if grid is a sequence
        for x in range(0,3):
            for y in range(0,3):
                list_number.append(grid[x][y])

        if sorted(list_number) != [*range(1,10)]:
            return False
        list_number.clear()

        # check row has duplicated
        for x in range(0,3):
            for y in range(0,3):
                list_number.append(grid[x][y])

            if len(list_number) != len(set(list_number)):
                return False
            list_number.clear()

        # check if coln has duplicates
        for y in range(0,3):
            for x in range(0,3):
                list_number.append(grid[x][y])

            if len(list_number) != len(set(list_number)):
                return False
            list_number.clear()

        return True




    #print(check(grid))

    #check if its a sequence for 1 to 9

    # check if row and columns are not repeated

    # check if columns are not repeated




    #print(elements)
