class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError('missing name')
        if not house:
            raise ValueError('missing house')
        
            
        self.name = name ,
        self.house = house



def main():
    student = get_student()
    print(f'student {student.name} from {student.house}')
    

    

def get_student():
    name = input('Name: ')
    house = input('House: ')
    try:
        student = Student(name,house)
    except ValueError:
        ...
        

    return student


if __name__ == "__main__":
    main()