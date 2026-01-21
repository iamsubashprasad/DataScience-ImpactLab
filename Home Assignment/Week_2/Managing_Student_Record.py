"""
Requirements:
a) Create a class named Student.
b) Inside the class, define the following attributes:
1. name → string
2. grade → string
3. department → string
c) Implement the following methods:
1. print_info() → prints all details of the student.
2. update_grade(new_grade) → updates the student’s grade.

d) In the main section (if __name__ == "__main__":):
 Create at least three Student objects with different details.
 Print each student’s information.
 Update the grade of one student and print the updated details.
 Manage and display multiple student records separately.
"""






class student:

    def __init__(self,name,grade,department):
        self.name = name
        self.grade=grade
        self.department= department


    def print_info(self):
        print("Student Details")
        print("Name", self.name)
        print("Grade",self.grade)
        print("Department",self.department)
        print("------------------------")


    def update_grade(self,new_grade):
        self.grade = new_grade
        print("Updated Grade is",self.grade )


record1 = student ("Subash","A","Computer Science")
record2 = student ("Manoj","B","Information Technology")
record3 = student ("Pavanthan","C","MBBS")


record1.print_info()
record2.print_info()
record3.print_info()
record3.update_grade("A++")
record3.print_info()

