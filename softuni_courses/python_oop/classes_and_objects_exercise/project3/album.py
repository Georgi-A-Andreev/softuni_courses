from softuni_courses.python_oop.classes_and_objects_exercise.project3.song import Song

class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name: str):
        for s in self.songs:
            if s.name == song_name and self.published:
                return "Cannot remove songs. Album is published."
            if s.name == song_name and not self.published:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + '\n'.join([f"== {s.get_info()}" for s in self.songs])
