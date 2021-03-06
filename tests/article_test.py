import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('https://images.cointelegraph.com/images/1200_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS91cGxvYWRzLzIwMjEtMDkvMzczZjNkMjMtMTExMS00NTEwLWEwNDgtZWQyNmMwN2JhMjhmLmpwZw==.jpg','El Salvador’s Bitcoin detractors: Opposition mounts despite crypto rollout - Cointelegraph','2021-09-11T05:07:00Z','https://cointelegraph.com/news/el-salvador-s-bitcoin-detractors-opposition-mounts-despite-crypto-rollout','Jinia Shawdagor','Cointelegraph')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
