class TestStatus:
   
    def __init__(self, testcaseid, status):
        self.testcaseid = testcaseid
        self.status = status


    def DisplayTestResult(self):
        print("Test Case ID:", self.testcaseid)
        print("Status:", self.status)



test1 = TestStatus(90, "Passed")


test1.DisplayTestResult()
