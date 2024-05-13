class Subject:
    '''
    A class representing a subject.
    '''
    lst_subjects = []

    def __init__(self, ptr):
        '''
        Initialize the subject with its details.
        '''
        ptr = ptr.split(';')
        self.subject = ptr[0]
        info = ptr[1].split(',')
        self.days = []
        self.nums = []
        self.rooms = []
        self.lecturers = []
        self.day_num = []
        self.full = []
        for day in info:
            self.days.append(day.split('-')[0])
            self.nums.append(int(day.split('-')[1]))
            self.day_num.append([day.split('-')[0], int(day.split('-')[1])])
            self.rooms.append(day.split('-')[2])
            self.lecturers.append(day.split('-')[3])
            self.full.append(day.split('-'))
        self.hours = ptr[2]
        self.groups = ptr[3].split(',')
        Subject.lst_subjects.append(self)

    def __str__(self):
        return self.subject

    def __repr__(self):
        return str(self.subject)


class Time:
    '''
    A class representing class time slots.
    '''
    all_classes = {}

    def __init__(self, ptr):
        ptr = ptr.split(';')
        self.num = int(ptr[0])
        self.time = ptr[1]
        Time.all_classes[self.num] = self.time

    def __str__(self):
        return self.num, self.time

    def __repr__(self):
        return str(f'{self.num}, {self.time}')


class Schedule:
    '''
    A class representing a schedule.
    '''
    days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб']

    @classmethod
    def make_day(cls, group, day):
        '''
        Generate the schedule for a specific day and group.
        '''
        day_schedule_subj = []
        for subj in Subject.lst_subjects:
            if day in subj.days and str(group) in subj.groups:
                day_schedule_subj.append(subj)

        final_subj = {}

        for i in day_schedule_subj:
            final_subj[i] = []
        subj_day_num = {}

        for subj in day_schedule_subj:
            subj_day_num[subj] = subj.full

        for subj in subj_day_num:
            for data in subj_day_num[subj]:
                if data[0] == day:
                    final_subj[subj].append(data)

        dict_num_subj = {}

        for subj in final_subj.keys():
            for data in final_subj[subj]:
                data.append(subj)
                dict_num_subj[int(data[1])] = data
        sorted_dict = dict(sorted(dict_num_subj.items()))

        schedule_str = f'День недели: {day}{'\n'}'

        for num in sorted_dict:
            schedule_str += (
                f'{num} пара. Предмет:'
                f' {sorted_dict[num][-1]}{(20 - len(str(sorted_dict[num][-1]))) * ' '}'
                f' Преподаватель:'
                f' {sorted_dict[num][3]}{(20 - len(str(sorted_dict[num][3]))) * ' '}'
                f'Кабинет:'
                f' {sorted_dict[num][2]}{(10 - len(str(sorted_dict[num][2]))) * ' '}'
                f'Время:'
                f' {Time.all_classes[num]}{(10 - len(str(sorted_dict[num][2]))) * ' '}{'\n'}')

        return schedule_str

    @classmethod
    def make_schedule(cls):
        '''
        Generate the schedule for a group for a week.
        '''
        group = str(input('Введите номер группы: '))
        for day in Schedule.days:
            print(Schedule.make_day(group, day))


with open('schedule.txt', 'r', encoding='utf-8') as f:
    for ptr in f:
        Subject(ptr)

with open('time_schedule.txt', 'r', encoding='utf-8') as f:
    for ptr in f:
        Time(ptr[:-1])

print(Time.all_classes[3])
print(Subject.lst_subjects)
print(Subject.lst_subjects[0].full)
print(Subject.lst_subjects[0].nums)
print(Subject.lst_subjects[0].rooms)
print(Subject.lst_subjects[0].groups)
print(Subject.lst_subjects[0].day_num)
print()

print(Schedule.make_day(22704, 'пн'))
Schedule.make_schedule()
