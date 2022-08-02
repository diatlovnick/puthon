# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.



lst = [1,2,3,4,5,6]
def mult_list(nums):
    return [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]

res = mult_list(lst)
#mult_list = lambda nums: [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]
print(lst)