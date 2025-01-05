##
#
# File:    FeaturesTest.py
# Author:  E. Peisach
# Date:    08-Oct-2018
# Version: 0.001
#
# Updates:
#
##
"""
Test cases for ensuring skipping of tests works.
"""
__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "peisach@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"

import os
import unittest

from wwpdb.utils.testing.Features import Features


class FeaturesTests(unittest.TestCase):
    """
    Test cases for skipping
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @unittest.skipUnless(Features().haveApi(), "skipping if lack of API")
    def testHaveApi(self) -> None:
        """Test should be run all the time"""
        self.assertTrue(Features().haveApi())

    @unittest.skipIf(Features().haveApi(), "requires API to run")
    def testNotHaveApi(self) -> None:
        self.fail("Test should have been skipped")

    @unittest.skipUnless(Features().testNever(), "tests for never execution")
    def testNever(self) -> None:
        self.fail("Test should have been skipped")

    def testMySqlTestServer(self) -> None:
        self.assertFalse(Features().haveMySqlTestServer())
        os.environ["MYSQLUP"] = "True"
        self.assertTrue(Features().haveMySqlTestServer())
        del os.environ["MYSQLUP"]

    def testRbmqTestServer(self) -> None:
        # Might need to handle true case
        self.assertFalse(Features().haveRbmqTestServer())

    def testCvsTestServer(self) -> None:
        self.assertFalse(Features().haveCvsTestServer())

    def testSvnTestServer(self) -> None:
        self.assertFalse(Features().haveSvnTestServer())

    def testSftpTestServer(self) -> None:
        self.assertFalse(Features().haveSftpTestServer())

    def testToolsRuntime(self) -> None:
        self.assertFalse(Features().haveToolsRuntime())

    def testHaveCCD(self) -> None:
        self.assertFalse(Features().haveCCD())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
