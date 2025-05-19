class Counter :
    object_count = 0

    def __init__(self):
        Counter.object_count += 1

    @classmethod    
    def show_count(cls):
        print(f'Total objects created: {cls.object_count}')

a = Counter()
b = Counter()
c = Counter()
d =  Counter()
e =  Counter()

Counter.show_count()
