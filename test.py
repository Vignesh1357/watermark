import main
import os
import pytest


def test_logo():
    assert main.logo_search('./PPT - Logo - Images - Assignment') is not None


def test_altered_images():
    assert len(os.listdir('./altered_images')) > 1
