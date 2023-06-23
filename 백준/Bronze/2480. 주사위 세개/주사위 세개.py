from collections import Counter
nums = list(map(int, input().split()))
counter = dict(Counter(nums).most_common(3))
if len(counter) == 1:
    print(10000+nums[0]*1000)
elif len(counter) == 2:
    print(1000+list(counter)[0]*100)
else:
    print(max(nums)*100)