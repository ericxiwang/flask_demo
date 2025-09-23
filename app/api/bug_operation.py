import time
from datetime import datetime
class bug_operation:

    def __init__(self,bug_title,bug_desc,bug_level,bug_assignee,bug_status,bug_category,bug_keywords):
        self.bug_datetime = int(time.time())
        self.real_datatime = datetime.fromtimestamp(self.bug_datetime)
        self.bug_title = bug_title
        self.bug_desc = bug_desc
        self.bug_level = bug_level
        self.bug_assignee = bug_assignee
        self.bug_status = bug_status
        self.bug_category = bug_category
        self.bug_keywords = bug_keywords
        print(self.real_datatime)

    def create_bug(self):
        return (self.bug_datetime,self.bug_level)

    def assign_bug(self):
        pass

    def edit_bug(self):
        pass








if __name__ == '__main__':
    a = bug_operation("test","test","test","test","test","test","test")
    print(a.create_bug())