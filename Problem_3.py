'''
3. Music Festival Playlist Organization
Objective:
The aim of this assignment is to develop your skills in using Python loops with sets, 
particularly for organizing and managing playlists for a music festival. 
You will work with sets to handle various artists and genres, ensuring no duplicates and maintaining a well-organized collection.

Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. 
Using a loop, compile these artist names into a set to create a unique lineup without duplicates.

Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
Expected Outcome:
A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.
'''

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

artist_names = sorted(artist_names)
for name in artist_names:
    if name not in unique_artists:
        unique_artists.add(name)
        
    else:
        print(f"\nDuplicates have been found: {name}")
print(f"\nAfter clearing the duplicates, we end with: {unique_artists}")
print("\n")
