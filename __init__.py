from Member import Member
from MemberDatabase import MemberDatabase

sb = Member()
sb.student_ID = "SB"
sb.first_name = "脑瘫"
sb.last_name = "不学习"

b2 = Member()
b2.student_ID = "2B"

print(sb.get_id())
print(sb.get_name())
print(b2.get_id())

d = MemberDatabase()
d.add(sb)
d.add(b2)

print(d.retrieve("2B").student_ID)

print(d.retrieve("SB").get_name())
d.delete("SB")
print(d.retrieve("SB").get_name())
