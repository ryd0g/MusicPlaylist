from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current = self.__first_song
    count = 0
    while current != None:
        if current.get_title() == title:
            return count
        else:
            count += 1
            current = current.__next_song
    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    previous = None
    target = self.__first_song
    while target != None:
      if target.get_title() == title:
        if previous:
          previous.set_next_song(get_next_song())
        else:
          self.__first_song = target.get_next_song()
        return True
      previous = target
      target = target.get_next_song()
    
    return False

        

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current = self.__first_song
    count = 0
    if current != None:
      count += 1
      current = current.get_next_song()
    return count


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    count = 0
    if current != None:
      count += 1
      print(f'{count}. {current.get_title()}')

  