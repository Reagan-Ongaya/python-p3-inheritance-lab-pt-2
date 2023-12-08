class Student:
    def hello(self):
        print("Hello, I'm a student.")

    def raise_hand(self):
        print("Raising hand respectfully to get the teacher's attention.")


class ChattyStudent(Student):
    def hello(self):
        print("Hello, I'm a chatty student. Did you watch the latest TV show?")

    def raise_hand(self):
        for _ in range(10):
            print("Raising hand respectfully to get the teacher's attention.")


