#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n)
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items):
        if (items[i] > items[i+1]) and (items[i] != items[len(items)]):
            return False
        return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?"""
    sorted = False
    while sorted is not True:
        sorted_temp = True
        for i in range(0, len(items)-1):
            if items[i] != items[len(items)-1]:
                if items[i] > items[i+1]:
                    sorted_temp = False
                    temp_value = items[i]
                    items[i] = items[i+1]
                    items[i+1] = temp_value
        if sorted_temp is True:
            sorted = True
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items)-1):
        smallest = i
        for z in range(i, len(items)-1):
            if items[z] < items[smallest]:
                smallest = z
        if smallest != i:
            items[i], items[smallest] = items[smallest], items[i]
    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items)-1):
        for z in range(i, 0, -1):
            if (items[z] > items[i]) or (z == 0):
                temp_element = items.remove(items[z])
                items.insert(i, temp_element])
                break
    return items
