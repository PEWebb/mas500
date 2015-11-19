import logging
import unittest
import MC_HW1intermediateV2


class TestMediaCloudAPICall (unittest.TestCase):
	def testMediaCloudAPICall (self):
		res= MC_HW1intermediateV2.callMediaCloud()
		assert res!=None 


logging.basicConfig(filename="sample.log", level=logging.DEBUG)

logging.debug('This Works')
logging.info('So should this')
logging.warning('And this, too')
logging.error("An error has happened!")



if __name__ == "__main__":
    unittest.main()