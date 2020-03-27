from Activity import Activity


class ActivityBoard:
    def __init__(self):
        self.activities = []

    def is_present(self, name):
        for i in self.activities:
            if i.get_name() == name:
                return True

        return False

    def add(self, activity: Activity):
        if not self.is_present(activity.get_name()):
            self.activities.append(activity)
            return True
        else:
            return False

    def update(self, activity: Activity):
        for i in self.activities:
            if i.get_name() == activity.get_name():
                self.activities.remove(i)
                self.activities.append(activity)
                return True
        return False

    def retrieve(self, name):
        for i in self.activities:
            if i.get_name() == name:
                return i

        print("The activity with the name:", name, " is not found.")

    def delete(self, name):
        for i in self.activities:
            if i.get_name() == name:
                self.activities.remove(i)
                return True

        return False
