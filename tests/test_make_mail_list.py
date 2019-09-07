import unittest
import os
import sys
import logging
from mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import make_mail_list
from make_mail_list import MailListMaker, FileReader


class TestMailListMaker(unittest.TestCase):
    def setUp(self):
        self.mlm = MailListMaker()
        self.case = ["test.email+alex@leetcode.com",
                     "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    def test_init_with_list(self):
        self.mlm = MailListMaker(self.case)  # replace mlm from setUp
        self.assertEqual(self.mlm.mails, self.case)

    def test_init_with_empty_list(self):
        self.assertEqual(self.mlm.mails, [])

    def test_get_from_list(self):
        self.mlm.get_from_list(self.case)
        self.assertEqual(self.mlm.mails, self.case)

    @patch.object(FileReader, '_read_lines')
    def test_read_from_txt(self, mock_read_lines):
        mock_read_lines.return_value = self.case
        self.mlm.read_from_txt("file_path")
        self.assertEqual(self.mlm.mails, self.case)

    def test_read_from_nonexistent_txt(self):
        with self.assertRaises(FileNotFoundError):
            self.mlm.read_from_txt("wrong way")

    def test_find_target_mails(self):
        self.mlm.mails = self.case
        result = self.mlm.find_target_mails()
        required = {"testemail@leetcode.com", "testemail@lee.tcode.com"}
        self.assertCountEqual(result, required)

    @patch.object(MailListMaker, "find_target_mails")
    def test_count_target_mails(self, mock_find_target_mails):
        mock_find_target_mails.return_value = {"testemail@leetcode.com", "testemail@lee.tcode.com"}
        result = self.mlm.count_target_mails()
        self.assertEqual(result, 2)
