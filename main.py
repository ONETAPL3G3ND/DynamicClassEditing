class Test:
    ...

def Example(self):
    print(self.name)

if __name__ == "__main__":
    Test.TestExample = Example
    Test.name = "Vasya"

    t = Test()
    t.TestExample()
