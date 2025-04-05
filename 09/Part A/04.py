def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = [90, 80, 70, 60, 50]
total, average = sum_avg(marks)
print(f"Total: {total}, Average: {average}")
