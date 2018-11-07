import unittest
from datetime import datetime
from CA4_bigdata import get_commits, read_file

print(datetime.strptime('2015-11-26', '%Y-%m-%d'))
class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('Jimmy', commits[420]['author'])
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
				'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
				commits[24]['comment'])
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                commits[20]['changed_path'])
    
    def test_statistics(self):    
        self.assertEqual(2,tot_lines.at['Dave','number_of_lines'])
        self.assertEqual(234,tot_lines.at['Thomas','number_of_lines'])
        self.assertEqual(80,tot_lines.at['Vincent','number_of_lines'])
        self.assertEqual(30,tot_date.at[datetime.strptime('2015-11-26', '%Y-%m-%d'),'number_of_lines'])
        self.assertEqual(20,tot_date.at[datetime.strptime('2015-11-20', '%Y-%m-%d'),'number_of_lines'])
        self.assertEqual(19,tot_date.at[datetime.strptime('2015-11-12', '%Y-%m-%d'),'number_of_lines'])
        self.assertEqual(5.552631578947368,release_no['number_of_lines'].mean())
        self.assertEqual(1.3151658767772512,df['number_of_lines'].mean())
        
if __name__ == '__main__':
    unittest.main()
