import re
def group_by_commas(n):
    return '{:,}'.format(n)

print(group_by_commas(19234))
print(group_by_commas(19255366477))