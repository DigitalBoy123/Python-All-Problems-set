dictionary = {
    "Vegetables":88,
    "Fruits": 99,
    "cereals": 34,
    "Meant": 23,
}

Values_unique = dictionary.values()
man_vlaues = set(Values_unique)
sorted_value = sorted(man_vlaues)
print(sorted_value)


favorite_songs= {
    "Song1": "Aritst1",
    "Song3": "Aritst3",
    "Song4": "Aritst4",
    "Song5": "Aritst5",
}

playlist_Songs = {
    "Song6": "Aritst6",
    "Song7": "Aritst7",
    "Song4": "Aritst4",
    "Song5": "Aritst5",
}

favorite_set = set(favorite_songs)
playlist_set = set(playlist_Songs)
symmetric_dif = favorite_set.symmetric_difference(playlist_set)
print(symmetric_dif)
