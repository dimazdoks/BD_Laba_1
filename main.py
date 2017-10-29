import pickle

class Database:
    def __init__(self):
        try:
            self.data = pickle.load(open('database.p', 'rb'))
        except:
            self.data = {}
            self.data['universitys'] = []
            self.data['facultys'] = []

            pickle.dump(self.data, open('database.p', 'wb'))

# Universitys -------------

class Universitys:
    def __init__(self, main):
        self.main = main

    def select_universitys(self, key=None, value=None):
        if not key:
            return db.data['universitys']

        university_array = []

        for university in db.data['universitys']:
            if university[key] == value:
                university_array.append(university)

        return university_array

    def print_universitys(self, universitys):
        #print(len(universitys))
        for university in universitys:
            print('{0} {1} {2}'.format(university['name'], university['accreditation'], university['dean_age']))

    def filter_universitys(self):
        universitys_result = []

        for university in db.data['universitys']:
            if int(university['dean_age']) < 50:
                universitys_result.append(university)

        return universitys_result

class University:
    def __init__(self, main):
        self.main = main

    def create_university(self, name, accreditation, dean_age):

        if len(u_tys.select_universitys('name', name)) > 0:
            raise Exception('Error: university with name \'{0}\' already exists'.format(name))

        try:
            int(dean_age)
        except:
            raise Exception('Error: dean_age must be a number')

        print(name, ' is appended?')
        db.data['universitys'].append({
            'name': name,
            'accreditation': accreditation,
            'dean_age': dean_age,
        })
        print(name, ' is appended?')

    def update_university(self, name, key, value):
        for university in db.data['universitys']:
            if university['name'] == name:
                if (key == 'name') and (value != university['name']) and (len(u_tys.select_universitys('name', value)) > 0):
                    raise Exception('Error: university with name \'{0}\' already exists'.format(value))
                if (key == 'dean_age'):
                    try:
                        int(value)
                    except:
                        raise Exception('Error: dean_age must be a number')

                university[key] = value
                break

    def delete_university(self, name):
        for university in list(db.data['universitys']):
            if university['name'] == name:
                for faculty in list(db.data['facultys']):
                    if faculty['university_name'] == university['name']:
                        db.data['facultys'].remove(faculty)

                db.data['universitys'].remove(university)
                break


# Facultys ----------
class Facultys:
    def __init__(self, main):
        self.main = main

    def select_facultys(self, key=None, value=None):
        if not key:
            return db.data['facultys']

        faculty_array = []

        for faculty in db.data['facultys']:
            if faculty[key] == value:
                faculty_array.append(faculty)

        return faculty_array

    def print_facultys(self, facultys):
        #print(len(facultys))
        for faculty in facultys:
            print('{0} {1} {2}'.format(faculty['name'], faculty['students_number'], faculty['university_name']))


class Faculty:
    def __init__(self, main):
        self.main = main

    def create_faculty(self, name, students_number, university_name):
        if len(f_ys.select_facultys('name', name)) > 0:
            raise Exception('Error: faculty with name \'{0}\' already exists'.format(name))
        if len(u_tys.select_universitys('name', university_name)) == 0:
            raise Exception('Error: there is no university with name \'{0}\''.format(university_name))

        try:
            int(students_number)
        except:
            raise Exception('Error: students_number must be a number')

        db.data['facultys'].append({
            'name': name,
            'students_number': students_number,
            'university_name': university_name,
        })

    def update_faculty(self, name, key, value):
        for faculty in db.data['facultys']:
            if faculty['name'] == name:
                if (key == 'name') and (value != faculty['name']) and (len(f_ys.select_facultys('name', value)) > 0):
                    raise Exception('Error: faculty with name \'{0}\' already exists'.format(value))
                if (key == 'university_name') and (len(u_tys.select_universitys('university_name', value)) == 0):
                    raise Exception('Error: there is no university with name \'{0}\''.format(university_name))
                if (key == 'students_number'):
                    try:
                        int(value)
                    except:
                        raise Exception('Error: students_number must be a number')

                faculty[key] = value
                break

    def delete_faculty(self, name):
        for faculty in list(db.data['facultys']):
            if faculty['name'] == name:
                db.data['facultys'].remove(faculty)
                break



db = Database()

u_tys = Universitys('Universitys')
u_ty = University('University')
f_y = Faculty('F-y')
f_ys = Facultys('F-ys')


while True:
    print('')
    print('Select table:')
    print('1. universitys')
    print('2. facultys')
    print('e. Exit program')
    menu_input_table = input()

    if menu_input_table == '1':
        while True:
            print('')
            print('Select action for table \'universitys\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('5. Filter')
            print('e. Go back')
            menu_input_table_universitys = input()

            if menu_input_table_universitys == '1':
                try:
                    print('')
                    print('Type university \'name\', \'accreditation\', \'dean_age\' separated by spaces:')
                    input_university = input().split(' ')
                    if len(input_university) < 3:
                        raise Exception('Error: you must provide three arguments')
                    #print("One sec", input_university[0], input_university[1], input_university[2])
                    u_ty.create_university(input_university[0], input_university[1], input_university[2])
                    #print(input_university[0], input_university[1], input_university[2], " is working..?")
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_universitys == '2':
                try:
                    print('')
                    print('Enter university name that you want to update')
                    university_name = input()

                    if len(u_tys.select_universitys('name', university_name)) == 0:
                        raise Exception('Error: there is no university with name \'{0}\''.format(university_name))

                    print('')
                    print('Enter field that you want to update (\'name\', \'accreditation\', \'dean_age\')')
                    update_field = input()
                    if (update_field != 'name') and (update_field != 'accreditation') and (update_field != 'dean_age'):
                        raise Exception('Error: invalid field')

                    print('')
                    print('Enter value:')
                    update_value = input()

                    u_ty.update_university(university_name, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_universitys == '3':
                try:
                    print('')
                    print('Enter university name that you want to delete')
                    university_name = input()

                    if len(u_tys.select_universitys('name', university_name)) == 0:
                        raise Exception('Error: there is no university with name \'{0}\''.format(university_name))

                    u_ty.delete_university(university_name)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_universitys == '4':
                try:
                    print('')
                    print(
                    'Enter field that you want to filter (\'name\', \'accreditation\', \'dean_age\'), or leave blank to list all')
                    input_field = input()
                    if (input_field != 'name') and (input_field != 'accreditation') and (
                        input_field != 'dean_age') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        u_tys.print_universitys(u_tys.select_universitys())
                        continue

                    print('')
                    print('Enter \'{0}\' value:'.format(input_field))
                    input_value = input()
                    print('')
                    u_tys.print_universitys(u_tys.select_universitys(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_universitys == '5':
                try:
                    print('')
                    print('Showing universities, where dean age is less then 50:')
                    print('')
                    u_tys.print_universitys(u_tys.filter_universitys())
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_universitys == 'e':
                break
    elif menu_input_table == '2':
        while True:
            print('')
            print('Select action for table \'facultys\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('e. Go back')
            menu_input_table_facultys = input()

            if menu_input_table_facultys == '1':
                try:
                    print('')
                    print('Type faculty \'name\', \'students_number\', \'university_name\' separated by spaces:')
                    input_faculty = input().split(' ')
                    if len(input_faculty) < 3:
                        raise Exception('Error: you must provide three arguments')
                    f_y.create_faculty(input_faculty[0], input_faculty[1], input_faculty[2])
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_facultys == '2':
                try:
                    print('')
                    print('Enter faculty name that you want to update')
                    faculty_name = input()

                    if len(f_ys.select_facultys('name', faculty_name)) == 0:
                        raise Exception('Error: there is no faculty with name \'{0}\''.format(faculty_name))

                    print('')
                    print('Enter field that you want to update (\'name\', \'students_number\', \'university_name\')')
                    update_field = input()
                    if (update_field != 'name') and (update_field != 'students_number') and (
                        update_field != 'university_name'):
                        raise Exception('Error: invalid field')

                    print('')
                    print('Enter value:')
                    update_value = input()

                    f_y.update_faculty(faculty_name, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_facultys == '3':
                try:
                    print('')
                    print('Enter faculty name that you want to delete')
                    faculty_name = input()

                    if len(f_ys.select_facultys('name', faculty_name)) == 0:
                        raise Exception('Error: there is no faculty with name \'{0}\''.format(faculty_name))

                    f_y.delete_faculty(faculty_name)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_facultys == '4':
                try:
                    print('')
                    print(
                    'Enter field that you want to filter (\'name\', \'students_number\', \'university_name\'), or leave blank to list all')
                    input_field = input()
                    if (input_field != 'name') and (input_field != 'students_number') and (
                        input_field != 'university_name') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        f_ys.print_facultys(f_ys.select_facultys())
                        continue

                    print('')
                    print('Enter \'{0}\' value:'.format(input_field))
                    input_value = input()
                    print('')
                    f_ys.print_facultys(f_ys.select_facultys(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_facultys == 'e':
                break
    elif menu_input_table == 'e':
        break

pickle.dump(db.data, open('database.p', 'wb'))