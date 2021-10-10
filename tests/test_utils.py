import src.utils
import src.dirs

def test_get_filenames_in_dir():
    nb_dir = src.dirs.project_dir / 'notebooks'
    files = src.utils.get_filenames_in_dir(nb_dir)
    assert len(files) > 0


class TestAdd():
    def test_add1(self):
        assert src.utils.add(-1,1) == 0
    def test_add2(self):
        assert src.utils.add(-1,-1) == -2
    def test_add3(self):
        assert src.utils.add(15,-4) == src.utils.add(-4,15)
    def test_add4(self):
        assert src.utils.add(1,2,3) == 6
