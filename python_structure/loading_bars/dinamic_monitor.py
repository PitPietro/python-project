from tqdm import tqdm
import os.path

"""
Dynamic Monitor/Meter:
You can use a tqdm as a meter which is not monotonically increasing. This could be because n decreases (e.g. a CPU
usage monitor) or total changes. One example would be recursively searching for files. The total is the number of
objects found so far, while n is the number of those objects which are files (rather than folders).
"""


def find_files_recursively(path, show_progress=True):
    files = []
    # total=1 assumes `path` is a file
    t = tqdm(total=1, unit="file", disable=not show_progress, ncols=100)
    if not os.path.exists(path):
        raise IOError("Cannot find:" + path)

    def append_found_file(file):
        # print("File: {}".format(file))
        files.append(file)
        t.update()

    def list_found_dir(path_list_found):
        """returns os.listdir(path) assuming os.path.isdir(path)"""
        listing = os.listdir(path_list_found)
        # subtract 1 since a "file" we found was actually this directory
        t.total += len(listing) - 1
        # fancy way to give info without forcing a refresh
        t.set_postfix(dir=path_list_found[-10:], refresh=False)
        t.update(0)  # may trigger a refresh
        return listing

    def recursively_search(path_rec_search):
        if os.path.isdir(path_rec_search):
            for f in list_found_dir(path_rec_search):
                recursively_search(os.path.join(path_rec_search, f))
        else:
            append_found_file(path_rec_search)

    recursively_search(path)
    t.set_postfix(dir=path)
    t.close()
    return files


if __name__ == '__main__':
    find_files_recursively('/home/pietro/Documents')
