import pytest
from project import number_of_notes, add_note, delete_note, search_note


def test_note_app():
    delete_note("all")
    assert number_of_notes() == 0
    add_note("This is a note")
    assert number_of_notes() == 1
    add_note("This is the second note")
    assert number_of_notes() == 2


def test_add_method():
    assert add_note("This is a note") == "Added sucessfully"
    assert add_note("This is the second note") == "Added sucessfully"


def test_search_method():
    assert search_note("restaraunt") == "Notes not found!"


def test_delete_method():
    delete_note("all")
    assert number_of_notes() == 0
    add_note("This is a note")
    assert number_of_notes() == 1
    delete_note("1")
    assert number_of_notes() == 0


def test_number_of_notes():
    delete_note("all")
    assert number_of_notes() == 0
    add_note("This is a note")
    assert number_of_notes() == 1
    add_note("This is the second note")
    assert number_of_notes() == 2
