import os
import random
import shutil
import lazynlp
from pybloom import BloomFilter

def create_reddit_data():
    main_path = "/gpfs/gpfsfpo/reddit_urls/reddit_urls_p1"
    urls = os.listdir(main_path)
    for url in urls:
        print(url)
        tmp_path = os.path.join(main_path, url)
        lazynlp.download_pages(tmp_path, "/gpfs/gpfsfpo/reddit_dataset", timeout=30, default_skip=True, extensions=[], domains=[])

def main():
    create_reddit_data()

if __name__ == '__main__':
        main()