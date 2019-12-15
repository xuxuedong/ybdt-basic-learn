import sys
import os
import shutil

def usage():
    if len(sys.argv) != 3:
        print("Usage for linux: python3 ./tmp.py path_to_dir path_to_new_dir");
        sys.exit(0);
    else:
        global path_to_dir, path_to_new_dir, items;
        path_to_dir = sys.argv[1];
        path_to_new_dir = sys.argv[2]
        items = os.listdir(path_to_dir);

def unify_format():
    print(items);
    for item in items:
        if "-" in item or "_" in item or "——" in item:
            pass;
        else:
            item_full_path = os.path.join(path_to_dir, item);
            shutil.move(item_full_path, path_to_new_dir);

def main():
    usage();
    unify_format();

main()
