from library_item import LibraryItem
def test_default_rating():
    key = LibraryItem("Tom and Jerry", "Fred Quimby" ,0)
    assert key.name == "Tom and Jerry"
    assert key.director == "Fred Quimby"
    assert key.rating == 0
    assert key.play_count == 0

def test_video_details():
    key = LibraryItem("Tom and Jerry", "Fred Quimby" ,4)
    assert key.name == "Tom and Jerry"
    assert key.director == "Fred Quimby"
    assert key.rating == 4
    assert key.play_count == 0

def test_info():
    key = LibraryItem("Tom and Jerry", "Fred Quimby" ,4)
    assert key.info() == "Tom and Jerry - Fred Quimby ****"

def test_stars():
    key = LibraryItem("Tom and Jerry", "Fred Quimby" ,4)
    assert key.stars() == "****"

def test_play_count():
    key = LibraryItem("Tom and Jerry", "Fred Quimby" ,4)
    key.play_count +=1
    assert key.play_count == 1
