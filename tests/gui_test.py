import unittest
import sys

sys.path.append("./")

from gui.app import App


class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = App()
        self.root.bind("<Key>", lambda e: print(self.root, e.keysym))

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_npc_frame(self):
        # Simulate clicking sidebar buttons
        self.root.sidebar.npc_button.invoke()
        assert self.root.current_frame == self.root.npc_frame

    def test_attack_frame(self):
        self.root.sidebar.attack_button.invoke()
        assert self.root.current_frame == self.root.attack_frame

    def test_construction_frame(self):
        self.root.sidebar.construction_button.invoke()
        assert self.root.current_frame == self.root.construction_frame

    def test_recruitment_frame(self):
        self.root.sidebar.recruitment_button.invoke()
        assert self.root.current_frame == self.root.recruitment_frame

    def test_lookup_frame(self):
        self.root.sidebar.lookup_button.invoke()
        assert self.root.current_frame == self.root.lookup_frame


if __name__ == "__main__":
    unittest.main()
