def filledOrders(order, k):
    # Write your code here
    c = []
    if sum(order) <= k:
        return len(order)
    else:
        for i in order:
            if i > k:
                c.append(i)
                return len(c) - 1
            else:
                c.append(i)
                if len(c) > 1:
                    if sum(c) > k:  # and order.index(i) == len(order):
                        return len(c.pop(order.index(i)))
                    else:
                        continue
                else:
                    continue


print(filledOrders([30, 44, 60, 40, 20, 45], 200))
