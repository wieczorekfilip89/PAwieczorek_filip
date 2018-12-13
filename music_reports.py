
ARTIST = 0
ALBUM = 1
YEAR = 2
GENRE = 3
DURATION = 4

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by


    :returns: all albums of given genre
    :rtype: list
    """
    result = []
    for album in albums:
        if album[GENRE] == genre:
            result.append(album)
    if not result:
        raise ValueError("Wrong genre")
    return result


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    result = {}

    for album in albums:
        if not album[GENRE] in result:
            result[album[GENRE]] = 1
        else:
            result[album[GENRE]] += 1
    return result


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    result = albums[ARTIST]
    for album in albums:
        if int(album[YEAR]) <= int(result[YEAR]):
            result = album
    return result



def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    return get_last_oldest(get_albums_by_genre(albums,genre))


def get_longest_album(albums):
    """
    Get album with biggest value in length field

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    result = albums[0]
    for album in albums:
        if to_time(album[DURATION]) > to_time(result[DURATION]):
            result = album
    return result

def to_time(str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    SEC_IN_MIN = 60
    min_sec = str.split(':')
    return int(min_sec[0])*SEC_IN_MIN + int(min_sec[1])

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    durations = map(lambda album: to_time(album[DURATION]), albums)
    total = sum(durations)
    return int(total / 60) + ((total % 60)/ 60)
