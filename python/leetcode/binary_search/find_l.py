"""
find id, s.t. arr[id] < num
"""


def find_smaller(arr, num):
    # arr.append(float('inf'))
    st_id = 0
    end_id = len(arr) - 1

    if num <= arr[0]:
        return -1

    while st_id < end_id:
        mid_id = (st_id + end_id) // 2
        if num <= arr[mid_id]:
            end_id = mid_id - 1
        else:
            st_id = mid_id + 1
            """
      if st_id != mid_id: # not stuck in infinite loop
      else:
        break
      """
    return st_id - 1


if __name__ == "__main__":
    # test normal
    ori_array = [1, 3, 5, 7, 9]
    array = []
    for i in ori_array:
        array = array + [i] * 5

    lookups = [item for item in range(min(array) - 1, max(array) + 2)]
    print(array)
    for item in lookups:
        id_ = find_smaller(array, item)
        if id_ < 0 or id_ >= len(array):
            print(item, id_)
        else:
            print(item, id_, array[id_])
