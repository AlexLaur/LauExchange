import os
from uuid import uuid1
import nuke


def run_import(path=None):
    """This function import the file

    :param path: The path of the file, defaults to None
    :type path: str, optional
    :return: The path of the file
    :rtype: str
    """
    return nuke.nodePaste(path)


def run_export(path=None):
    """This function export the selection to a file

    :param path: The path for the file, defaults to None
    :type path: str, optional
    :return: The file created
    :rtype: str
    """
    return nuke.nodeCopy(os.path.join(path, '%s.nk' % str(uuid1())))