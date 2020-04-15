from Member import Member
from AttendanceRecord import AttendanceRecord
from Activity import Activity
from datetime import datetime
mem1 = Member("sb", "sb", "sb", "sb")

mem1.set_face_id()

start = datetime(2020,2,2,12,20,00)
end = datetime(2020,2,2,13,20,00)
act = Activity("sb", start, end, "sb", 1)
rec = AttendanceRecord(act)

rec.take_attendance(mem1)

print(rec.get_status())

