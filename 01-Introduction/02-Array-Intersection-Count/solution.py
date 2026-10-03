def intersection_count(arr1, arr2):
    count = 0

    for element in arr1:
        if element in arr2:
            count += 1

    return count


n = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter first array: ").split()))

m = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter second array: ").split()))

result = intersection_count(arr1, arr2)

print("Intersection count:", result)