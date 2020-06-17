import os
from uuid import uuid1
from maya import cmds


def _export_selected(path=None, filename=None):
    """This function export the selection inside maya

    :param path: The path to save the file, defaults to None
    :type path: str, optional
    :param filename: The name of the file, defaults to None
    :type filename: str, optional
    :return: The path of the file
    :rtype: str
    """
    path_file = os.path.join(path, '%s.ma' % filename)
    cmds.file(path_file, exportSelected=True, force=True,
              options="v=0", type="mayaAscii")
    return path_file


def _import_file(path=None):
    """This function import the given path

    :param path: The path to import, defaults to None
    :type path: str, optional
    :return: The path imported
    :rtype: str
    """
    cmds.file(path, r=True, options="v=0;p=17;f=0", type="mayaAscii",
              ignoreVersion=True, mergeNamespacesOnClash=False,
              groupLocator=True)
    return path


def run_import(path=None):
    """This function import the file to the scene

    :param path: The path of the file, defaults to None
    :type path: str, optional
    :return: The path of the file
    :rtype: str
    """
    return _import_file(path=path)


def run_export(path=None):
    """This function export the selection to a file

    :param path: The path for the file, defaults to None
    :type path: str, optional
    :return: The file created
    :rtype: str
    """
    filename = str(uuid1())
    return _export_selected(path=path, filename=filename)