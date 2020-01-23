import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from sudosearch import SudoSearch

def main():
    search_keyword = input('Enter Search Keyword: ')

    ss = SudoSearch()
    print(ss.find_json(search_keyword))

if __name__ == '__main__':
    main()
