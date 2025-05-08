# Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.


# class A define kkia (top of diamond)
class A:
    def show(self):
        print("show method of class A")  # Ye method class A ka hai

    
    # class b, class A se inherit kar rhati hai
class B(A):
    def show(self):
        print("show method of class B")  # Ye method class B ka hai


# class c, class A se inherit kar rhati hai
class C(A):
    def show(self):
        print("show method of class C")  # Ye method class C ka hai")


class D(B, C):
    def show(self):
        print("show method of class D")  # Ye method class D ka hai

# Object create kar rahe hain class D ka
d = D()  # D ka object banaya

# show() method call kar rahe hain — MRO ke mutabiq decide hoga kaun sa method chalega
d.show()  # D ka show method call kiya
            