def enough(cap, on, wait):
    if cap - on >= wait:
        return 0
    else:
        return wait - (cap - on)

print (enough(10, 5, 5))
print (enough(100, 60, 50))





# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus.
# wait is the number of people waiting to get on to the bus.


# enough(10, 5, 5)
# 0 # He can fit all 5 passengers
# enough(100, 60, 50)
# 10 # He can't fit 10 out of 50 waiting


# test.describe('Example Tests')
# test.assert_equals(enough(10, 5, 5), 0)
# test.assert_equals(enough(100, 60, 50), 10)
# test.assert_equals(enough(20, 5, 5), 0)