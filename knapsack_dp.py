# Summary : We're trying including the current item in the bag by "if" black. 
# Take user input for weights and profits. Then sort the weights and based on sorted weight, the profits would sort too.

def knapsack(capacity, profits_of, weights_of):
    total_items = len(weights_of)
    dp = [[0] * (capacity + 1) for _ in range(total_items + 1)]

    for cur_item_in_dp in range(1, total_items + 1):
        for cur_capacity in range(1, capacity + 1):
            # both "cur_item_in_bag" and "cur_item_in_dp" refers to the same item but in bag and dp respectively.
            cur_item_in_bag, prev_item_in_dp = cur_item_in_dp - 1, cur_item_in_dp - 1
            remaining_space_after_taking_current_item = cur_capacity - weights_of[cur_item_in_bag]

            if weights_of[cur_item_in_bag] <= cur_capacity:
                dp[cur_item_in_dp][cur_capacity] = max(dp[prev_item_in_dp][cur_capacity], 
                                                       profits_of[cur_item_in_bag] + dp[prev_item_in_dp][remaining_space_after_taking_current_item])
            else : # if current capacity itself is less than the weight of the current item, then we can't include that item.
                dp[cur_item_in_dp][cur_capacity] = dp[prev_item_in_dp][cur_capacity]

    return dp[total_items][capacity]

if __name__ == "__main__":
    profits = [1, 2, 3]
    weights = [4, 5, 1]
    capacity = 4
    
    print(knapsack(capacity, profits, weights))

"""
if we can include the current item in the bag:
    max profit for current item in current capacity = max(previous max profit exluding the current item in case including the current item doesn't yield max profit,
                                                          max profit can be yielded including the current item)
                                                          
else : # if we can't include the current item in bag, then the profit is simply it;s previous item's profit.
    max profit for current item in current capacity = the previous item's max profit for the current capacity since we can't include the current item in the bag at all.

max(option1, option2)

    Option 1 : Choose the previous result if including the current item in the bag doesn't yield maximum profit.
    Option 2 : Include the current item by its profit + what the remaining space excluding the current item can yield MAX PROFIT in previous item where
           the current item is excluded.

"""

