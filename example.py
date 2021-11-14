from main import Person, Director, Teacher, Student

dr1 = Director('John', 'Sandler', 36, 839472)
dr2 = Director('Casey', 'Baker', 27, 635402)

tc1 = Teacher('Hasan', 'August', 53, 639864)
tc2 = Teacher('Andy', 'Chandler', 23, 837403)

st1 = Student('Nursultan', 'Mirlanov', 20, 520480)
st2 = Student('Amina', 'Sarazhieva', 18, 836745)

# person = Person()

all = [dr1, dr2, tc1, tc2, st1, st2]
for i in all:
    print(i, i.get_fn() + ',',
          'Age:', str(i.get_age()) + ',',
          'ID:', i.get_id())