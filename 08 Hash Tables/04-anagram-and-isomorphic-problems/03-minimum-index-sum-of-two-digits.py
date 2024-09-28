def findRestaurant(list1, list2):
    index_map = {v: i for i, v in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for i, restaurant in enumerate(list2):
        if restaurant in index_map:
            index_sum = i + index_map[restaurant]
            if index_sum < min_sum:
                min_sum = index_sum
                result = [restaurant]
            elif index_sum == min_sum:
                result.append(restaurant)

    return result


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))  # ['Shogun']

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(findRestaurant(list1, list2))  # ['Shogun']