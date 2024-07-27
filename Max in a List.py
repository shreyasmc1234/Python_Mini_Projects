def find_largest(numbers):
    if not numbers:
        raise ValueError("The list is empty. Cannot find the largest number.")
    n=numbers[0]
    for j in numbers[1:]:
        if j>n:
            n=j
    return n

#numbers=[1,2,3]
numbers=[]
print(find_largest(numbers))