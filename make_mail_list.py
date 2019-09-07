import os
import logging


class FileReader:
    """
    Reads text file and returns array of lines.
    
    Makes warning if file is empty.
    """

    def read_from_txt(self, file_path):
        """
        Gets text file, reads lines and returns them.
        
        :param file_path: path to text file.
        :type file_path: str
        """
        self.mails = self._read_lines(file_path)
            
    def _read_lines(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input text file {file_path} is not found.")
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if not lines: logging.warning("Input file is empty!")
        return lines


class MailListMaker(FileReader):
    """
    Class for filter mail list. 
    Class gets list of mails, skips dots and parts after '+' in local names, 
    and after that returns only unique addresses.

    Can be init with *list*, or get mails from list/file after init.

    :param mails: list of mails, non-required parameter, empty on default.
    :type mails: list
    """

    def __init__(self, mails=[]):
        self.mails = mails

    def get_from_list(self, lst):
        """
        Save list of males to object attribute *mails*.

        :param lst: list of mails.
        :type lst: list
        """
        self.mails = lst

    def find_target_mails(self):
        """
        Filters list of mails. 
        
        Skips dots and parts after '+' in local names, 
        and after that returns only unique addresses.

        :return: unique addresses.
        :rtype: set
        """
        unique_mails = set()
        for i in self.mails:
            local, domain = i.split("@")
            local = self._filter_local_name(local)
            unique_mails.add(f"{local}@{domain}")      
        return unique_mails
    
    def _filter_local_name(self, local):
        """"""
        plus_position = local.find("+")
        if plus_position != -1: local = local[:plus_position]
        local = local.replace(".", "")
        return local

    def count_target_mails(self):
        """
        Returns count of unique mail addresses.

        :return: count of unique mail adresses.
        :rtype: int
        """
        return len(self.find_target_mails())
