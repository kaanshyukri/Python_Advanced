def check_nums(nums):
    positives = 0
    negatives = 0
    for num in nums:
        if num > 0:
            positives += num
        else:
            negatives += num
    if positives > abs(negatives):
        result = "The positives are stronger than the negatives"
    else:
        result = "The negatives are stronger than the positives"
    return f"{negatives}\n{positives}\n{result}"


numbers = [int(x) for x in input().split()]
print(check_nums(numbers))
