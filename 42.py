# You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.
# Even worse, she saved the duplicate files with random, embarrassing names ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).
#
# Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them, since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return a list of tuples ↴ where:
#
# the first item is the duplicate file
# the second item is the original file
# For example:
#
#   [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
#  ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
# You can assume each file was only duplicated once.




# Solution
# We walk through our whole file system iteratively. As we go, we take a "fingerprint" of each file in constant time by hashing the first few, middle few, and last few bytes. We store each file's fingerprint in a dictionary as we go.
#
# If a given file's fingerprint is already in our dictionary, we assume we have a duplicate. In that case, we assume the file edited most recently is the one created by our friend.

import os
import hashlib

def find_duplicate_files(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    # we'll track tuples of (duplicate_file, original_file)
    duplicates = []

    while len(stack):

        current_path = stack.pop()

        # if it's a directory,
        # put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # if it's a file
        else:

            # get its hash
            file_hash = sample_hash_file(current_path)

            # get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_hash in files_seen_already:

                existing_last_edited_time, existing_path = \
                    files_seen_already[file_hash]

                if current_last_edited_time > existing_last_edited_time:
                    # current file is the dupe!
                    duplicates.append((current_path, existing_path))

                else:
                    # old file is the dupe!
                    duplicates.append((existing_path, current_path))

                    # but also update files_seen_already to have
                    # the new file's info
                    files_seen_already[file_hash] = \
                        (current_last_edited_time, current_path)

            # if it's a new file, throw it in files_seen_already
            # and record its path and last edited time,
            # so we can tell later if it's a dupe
            else:
                files_seen_already[file_hash] = \
                    (current_last_edited_time, current_path)

    return duplicates


def sample_hash_file(path):

    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())

        else:
            num_bytes_between_samples = \
                (total_bytes - num_bytes_to_read_per_sample * 3) / 2

            # read first, middle, and last bytes
            for offset_multiplier in xrange(3):
                start_of_sample = offset_multiplier * \
                    (num_bytes_to_read_per_sample + num_bytes_between_samples)
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()

# We've made a few assumptions here:
#
# Two different files won't have the same fingerprints. It's not impossible that two files with different contents will have the same beginning, middle, and end bytes so they'll have the same fingerprints. Or they may even have different sample bytes but still hash to the same value (this is called a "hash collision"). To mitigate this, we could do a last-minute check whenever we find two "matching" files where we actually scan the full file contents to see if they're the same.
#
# The most recently edited file is the duplicate. This seems reasonable, but it might be wrong—for example, there might be files which have been edited by daemons (programs that run in the background) after our friend finished duplicating them.
#
# Two files with the same contents are the same file. This seems trivially true, but it could cause some problems. For example, we might have empty files in multiple places in our file system that aren't duplicates of each-other.
#
# Given these potential issues, we definitely want a human to confirm before we delete any files. Still, it's much better than combing through our whole file system by hand!
#
# Some ideas for further improvements:
#
# If a file wasn't last edited around the time your friend got a hold of your computer, you know it probably wasn't created by your friend. Similarly, if a file wasn't accessed (sometimes your filesystem stores the last accessed time for a file as well) around that time, you know it wasn't copied by your friend. You can use these facts to skip some files.
# Make the file size the fingerprint—it should be available cheaply as metadata on the file (so you don't need to walk through the whole file to see how long it is). You'll get lots of false positives, but that's fine if you treat this as a "pre-processing" step. Maybe you then take hash-based fingerprints only on the files which which have matching sizes. Then you fully compare file contents if they have the same hash.
# Some file systems also keep track of when a file was created. If your filesystem supports this, you could use this as a potentially-stronger heuristic for telling which of two copies of a file is the dupe.
# When you do compare full file contents to ensure two files are the same, no need to read the entire files into memory. Open both files and read them one block at a time. You can short-circuit as soon as you find two blocks that don't match, and you only ever need to store a couple blocks in memory.
# Complexity
# Each "fingerprint" takes O(1)O(1) time and space, so our total time and space costs are O(n)O(n) where nn is the number of files on the file system.
#
# If we add the last-minute check to see if two files with the same fingerprints are actually the same files (which we probably should), then in the worst case all the files are the same and we have to read their full contents to confirm this, giving us a runtime that's order of the total size of our files on disc.
#
# Bonus
# If we wanted to get this code ready for a production system, we might want to make it a bit more modular. Try separating the file traversal code from the duplicate detection code. Try implementing the file traversal with a generator!
#
# What about concurrency? Can we go faster by splitting this procedure into multiple threads? Also, what if a background process edits a file while our script is running? Will this cause problems?
#
# What about link files (files that point to other files or folders)? One gotcha here is that a link file can point back up the file tree. How do we keep our file traversal from going in circles?
#
# What We Learned
# The main insight was to save time and space by "fingerprinting" each file.
#
# This question is a good example of a "messy" interview problem. Instead of one optimal solution, there's a big knot of optimizations and trade-offs. For example, our hashing-based approach wins us a faster runtime but it can give us false positives.
#
# For messy problems like this, focus on clearly explaining to your interviewer what the trade-offs are for each decision you make. The actual choices you make probably don't matter that much, as long as you show a strong ability to understand and compare your options.
