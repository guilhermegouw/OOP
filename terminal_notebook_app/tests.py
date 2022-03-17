import unittest
from notebook import Note, Notebook


class NoteTests(unittest.TestCase):
    def setUp(self):
        self.note1 = Note("First note")

    def test_note_id(self):
        self.assertEqual(self.note1.id, 1)

    def test_note_match(self):
        self.assertEqual(self.note1.match("First"), True)

    def test_note_match_case_sensitive(self):
        self.assertEqual(self.note1.match("first"), False)


class NotebookTests(unittest.TestCase):
    def setUp(self):
        self.nb = Notebook()
        self.nb.notes = [Note("Example note", "")]
        self.nb.notes[0].id = 1

    def tearDown(self) -> None:
        self.nb.notes = [Note("Example note", "")]

    def test_new_note(self):
        self.nb.new_note("New note")
        self.assertEqual(self.nb.notes[1].memo, "New note")
        self.assertEqual(self.nb.notes[1].tag, "")

    def test_find_note(self):
        self.assertEqual(self.nb.notes[0], self.nb._find_note(1))

    def test_modify_memo(self):
        self.nb.modify_memo(1, "Modified note")
        self.assertEqual(self.nb.notes[0].memo, "Modified note")

    def test_modify_tag(self):
        self.nb.modify_tag(1, "Modified tag")
        self.assertEqual(self.nb.notes[0].tag, "Modified tag")

    def test_search(self):
        self.assertIn(self.nb.notes[0], self.nb.search("Example"))


if __name__ == "__main__":
    unittest.main()
