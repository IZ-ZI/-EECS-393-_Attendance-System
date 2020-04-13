from unittest import TestCase
from datetime import datetime
from Activity import Activity


class TestActivity(TestCase):
    start = datetime(2020,2,2,12,20)
    end = datetime(2020,2,2,15,20)
    id1 = "1"
    name1 = "act1"
    loc1 = "location1"
    act = Activity(id1, name1, start, end, loc1)
    def test_get_id(self):
        self.assertTrue(self.act.get_id() == "1")

    def test_get_name(self):
        self.assertTrue(self.act.get_name() == "act1")

    def test_get_start_time(self):
        self.assertTrue(self.act.get_start_time() == self.start)

    def test_get_end_time(self):
        self.assertTrue(self.act.get_end_time() == self.end)

    def test_get_location(self):
        self.assertTrue(self.act.get_location() == self.loc1)

