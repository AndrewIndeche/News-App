import unittest
from ..models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        '''
        self.new_source = Sources('cnn-international','CNN')

    def test_source(self):
        '''
        test for creation of a new instance
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        '''
        '''
        self.new_source.id = 'cnn-international'
        self.new_source.name='CNN'

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()