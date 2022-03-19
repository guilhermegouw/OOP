import datetime

# Store the next available id for all new notes.
last_id = 0


class Note:
    """
    Represent a note in the notebook. Match against a string in searchs and
    store tags for each note.
    """

    def __init__(self, memo: str, tag: str = "") -> None:
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter: str) -> bool:
        """
        Determine if this note matches the filter text.
        Search is case-sensitive and matchs both text and tags.
        Args:
            filter (str): string to be used as a filter.

        Returns:
            bool: Return True if it matches, False otherwise.
        """
        return filter in self.memo or filter in self.tag


class Notebook:
    """Represent a collection of notes that can be tagged, modified, and
    searched."""

    def __init__(self) -> None:
        self.notes = []

    def new_note(self, memo: str, tag: str = ""):
        """Create a new note and add it to the list.

        Args:
            memo (str): Note content.
            tags (str, optional): tag to help search. Defaults to "".
        """
        self.notes.append(Note(memo, tag))

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            else:
                None

    def modify_memo(self, note_id: int, new_memo: str):
        """Find the note with the given id and change its memo to the given
        value.

        Args:
            note_id (int): Id of the note to be modified.
            new_memo (str): new valeu for the note memo.
        """
        self._find_note(note_id).memo = new_memo

    def modify_tag(self, note_id: int, new_tag: str):
        """Find the note with the given id and change its tag to the given
        value.

        Args:
            note_id (int): Id of the note to be modified.
            new_tag (str): new valeu for the note tag.
        """
        self._find_note(note_id).tag = new_tag

    def search(self, filter: str):
        return [note for note in self.notes if note.match(filter)]
