class Playlist:

    def __init__(self, name: str, songs: list[str] = None) -> None:
        self.name = name
        if songs is None:
            self.songs = []
        else:
            self.songs = songs

    def __str__(self) -> str:
        string = f"{self.name}:"
        if self.songs:
            for i, song in enumerate(self.songs):
                string += f"\n{i + 1}. {song}"
        else:
            string += "\nno songs"
        return string

    def __repr__(self) -> str:
        if self.songs:
            return f"Playlist(\"{self.name}\" ,{len(self.songs)} songs)"
        return f"Playlist(\"{self.name}\" , no songs)"

    def __getitem__(self, index) -> list[str]:
        return self.songs[index]

    def __setitem__(self, index, song) -> None:
        if 0 <= index < len(self.songs):
            self.songs[index] = song

    def __len__(self) -> int:
        return len(self.songs)

    def __eq__(self, other: Playlist) -> bool:
        if len(self.songs) != len(other.songs):
            return False
        is_equal = True
        for i, song in enumerate(self.songs):
            if song != other.songs[i]:
                is_equal = False
        return is_equal

    def __add__(self, other: Playlist) -> Playlist:
        return Playlist(self.name + " " + other.name, self.songs + other.songs)

    def __contains__(self, song: str) -> bool:
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)

    def __bool__(self) -> bool:
        if not self.songs:
            return False
        return True

    def __iadd__(self, song_or_playlist: str | list | Playlist) -> Playlist:
        if isinstance(song_or_playlist, str):
            self.songs.append(song_or_playlist)
        elif isinstance(song_or_playlist, list):
            self.songs += song_or_playlist
        else:
            self.songs += song_or_playlist.songs
        return self


p1 = Playlist("fried", ["hazak", "ale_katan"])
p2 = Playlist("ben_david", ["maminim", "mashiah"])
p3 = Playlist("potolsky")
p4 = p1 + p2
p5 = p2 + p3
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print([p1, p2, p3, p4, p5])