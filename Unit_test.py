import unittest
from tkinter import Tk
import student_form

rootVal = Tk()
sm = student_form.StudentManagement(rootVal)

class TestPractise(unittest.TestCase):

    def test_babble_sort(self):
        list=[('23','sabdya','sandhya@gmail.com','23','female','Bsc Hons incomputing', '345679','wertyu'),
              ('34','amantika','amantika@gmail.com','32','female','Bsc Hons in EthicalHacking','2345','dfghjk'),
              ('45','nikita','nikita@gmail.com','34', 'female','Bsc Hons in EthicalHacking','45678','asdfghj')]
        exp_list = [('23', 'sabdya', 'sandhya@gmail.com', '23', 'female', 'Bsc Hons incomputing', '345679', 'wertyu'),
                ('34', 'amantika', 'amantika@gmail.com', '32', 'female', 'Bsc Hons in EthicalHacking', '2345',
                  'dfghjk'),
                 ('45', 'nikita', 'nikita@gmail.com', '34', 'female', 'Bsc Hons in EthicalHacking', '45678', 'asdfghj')]


        sm.combo_sort.set("StdID")
        ac_result=sm.Sort(list)
        print('Sort test')
        self.assertEqual(exp_list, ac_result)

    def test_search(self):
        list= [('23','sabdya','sandhya@gmail.com','23','female','Bsc Hons incomputing', '345679','wertyu'),
              ('34','amantika','amantika@gmail.com','32','female','Bsc Hons in EthicalHacking','2345','dfghjk'),
              ('45','nikita','nikita@gmail.com','34','Bsc Hons in EthicalHacking','45678','asdfghj')]
        exp_result=[('45', 'nikita', 'nikita@gmail.com', '34', 'Bsc Hons in EthicalHacking', '45678', 'asdfghj')]

        sm.txt_search.delete(0,'end')
        sm.txt_search.insert(0,'nikita')

        ac_result=sm.search(list)

        print('Search test')


        self.assertEqual(exp_result, ac_result)

if __name__=='__main__':
    unittest.main()


