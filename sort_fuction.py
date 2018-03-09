'''
冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

步骤：

比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
'''
插入排序 InsertionSort
介绍：

插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤：

从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果被扫描的元素（已排序）大于新元素，将该元素后移一位
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
'''
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
'''
快速排序

描述

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比
另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
'''/
选择排序 SelectionSort
介绍：

选择排序无疑是最简单直观的排序。它的工作原理如下。

步骤：

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
'''
def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

lists = [12,56,78,3,10,45,67]
bubble_list = bubble_sort(lists)
print(bubble_list)

insert_list = insert_sort(lists)
print(insert_list)

quick_list = quick_sort(lists,12,0)
print(quick_list)

select_list = select_sort(lists)
print(select_list)
