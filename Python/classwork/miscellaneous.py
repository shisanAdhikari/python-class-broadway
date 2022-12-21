"""
def sum(list, target):
    array = []
    for i in range(list):

        for j in range(i, len(list)):
            a = list[i] + list[j]

            if list[i] == list[j]:
                continue


            elif list[i] + list[j] == target:
            return (list[i], list[j])

    return []


result = sum(list=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
print(result)

"""

print("hello beautiful peoples")


