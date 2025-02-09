user_input = input("Enter numbers separated by space: ")s
numbers = [int(num) for num in user_input.split()]
average = sum(numbers) / len(numbers)
print("Average:", average)

