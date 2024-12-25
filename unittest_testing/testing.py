import unittest
from main import Teacher, SubjectTeacher

class TestTeacher(unittest.TestCase):
    teacher_1 = Teacher('test_name_1', 'test_education_1', 6)
    teacher_2 = Teacher('test_name_2', 'test_education_2', 6)

    def test_getters(self):
        self.assertEqual(TestTeacher.teacher_1.name, 'test_name_1')
        self.assertEqual(TestTeacher.teacher_1.education, 'test_education_1')
        self.assertEqual(TestTeacher.teacher_1.experience, 6)
    
    def test_experience_setter(self):
        TestTeacher.teacher_2.experience = 7
        self.assertEqual(TestTeacher.teacher_2.experience, 7)
    
    def test_get_teacher_data(self):
        self.assertEqual(TestTeacher.teacher_1.get_teacher_data(), 'test_name_1, образование: test_education_1, опыт: 6 года.')
    
    def test_add_mark(self):
        self.assertEqual(TestTeacher.teacher_1.add_mark('test_student', 4), 'Учитель test_name_1 поставил 4 ученику test_student.')

    def test_remove_mark(self):
        self.assertEqual(TestTeacher.teacher_1.remove_mark('test_student', 4), 'Учитель test_name_1 удалил оценку 4 у ученика test_student.')
    
    def test_give_consultation(self):
        self.assertEqual(TestTeacher.teacher_1.give_consultation('test_group'), 'Учитель test_name_1 провёл консультацию в test_group.')
    
    def test_fire_teacher(self):
        length = len(Teacher.all_teachers)
        TestTeacher.teacher_1.fire_teacher()
        self.assertEqual(len(Teacher.all_teachers), length - 1)
    
    def test_dislpay_teachers(self):   
        string = TestTeacher.teacher_1.get_teacher_data() + '\n' + TestTeacher.teacher_2.get_teacher_data() + '\n' + Teacher.all_teachers[2].get_teacher_data()
        self.assertEqual(TestTeacher.teacher_2.display_teachers(), string) 
    
class TestSubjectTeacher(unittest.TestCase):
    teacher_1 = SubjectTeacher('test_name_1', 'test_education_1', 6, 'test_subject', 'test_title')

    def test_getters(self):
        self.assertEqual(TestSubjectTeacher.teacher_1.subject, 'test_subject')
        self.assertEqual(TestSubjectTeacher.teacher_1.job_title, 'test_title')

    def test_job_title_setter(self):
        TestSubjectTeacher.teacher_1.job_title = 'test_title_1'
        self.assertEqual(TestSubjectTeacher.teacher_1.job_title, 'test_title_1')

    def test_get_teacher_data(self):
        self.assertEqual(TestSubjectTeacher.teacher_1.get_teacher_data(), 'test_name_1, образование: test_education_1, опыт: 6 года.\nПредмет: test_subject, должность: test_title.')
    
    def test_add_mark(self):
        self.assertEqual(TestSubjectTeacher.teacher_1.add_mark('test_student', 4), 'Учитель test_name_1 поставил 4 ученику test_student.\nПредмет: test_subject')

    def test_remove_mark(self):
        self.assertEqual(TestSubjectTeacher.teacher_1.remove_mark('test_student', 4), 'Учитель test_name_1 удалил оценку 4 у ученика test_student.\nПредмет: test_subject')
    
    def test_give_consultation(self):
        self.assertEqual(TestSubjectTeacher.teacher_1.give_consultation('test_group'), 'Учитель test_name_1 провёл консультацию в test_group.\nПо предмету: test_subject, как test_title.')

    
if __name__ == '__main__':
    unittest.main()