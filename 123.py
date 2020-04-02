from random import randrange

nums = []

def same(abc, cde):

    result = False

    for x in abc:
        if x == cde:
            result = True
            break

    return result



while len(nums)<6:

    balls = randrange(1,46)
    print(balls)
    if same(nums, balls) == True:
        continue

    nums.append(balls)

print(nums)


