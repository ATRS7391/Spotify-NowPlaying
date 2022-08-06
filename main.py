import win32gui


class Spotify:
    def __init__(self):
        self.title = ""
        self.artist = ""

    def nowplaying(self):
        def _find_spotify_uwp(hwnd, _windows):
            if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and not win32gui.GetWindowText(hwnd).startswith("Spotify") and win32gui.GetWindowText(hwnd) != "":
                windows.append(win32gui.GetWindowText(hwnd))

        windows = []
        win32gui.EnumWindows(_find_spotify_uwp, windows)
        if windows:
            self.artist, self.title = [name.strip() for name in windows[0].split("-", 1)]


if __name__ == "__main__":
    spotify = Spotify()
    spotify.nowplaying()
    print(spotify.artist)
    print(spotify.title)
