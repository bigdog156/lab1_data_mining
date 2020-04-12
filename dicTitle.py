import enum
list = ['id','stg','name']
class EnumTitle(enum.Enum):
    dog = 1
    cat = 2
    # index = 0
    # for i in list:
    #     i = index
    #     index = index + 1

print(EnumTitle.cat.value)
