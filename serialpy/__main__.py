import argparse
from serialpy import search, replace

def main():
    parser = argparse.ArgumentParser(description='Search and replace functionality for serialized data files.')
    
    subparsers = parser.add_subparsers(dest='command')

    # Search Command
    search_parser = subparsers.add_parser('search', help='Search for a word in serialized data.')
    search_parser.add_argument('file', type=str, help='Path to the data file.')
    search_parser.add_argument('word', type=str, help='Word to search for.')
    search_parser.add_argument('--find', choices=['key', 'value', 'all'], default='all', help='Search scope.')
    search_parser.add_argument('--ret', choices=['key', 'value', 'all'], default='all', help='Output format.')

    # Replace Command
    replace_parser = subparsers.add_parser('replace', help='Replace occurrences of a word in serialized data.')
    replace_parser.add_argument('file', type=str, help='Path to the data file.')
    replace_parser.add_argument('word', type=str, help='Word to replace.')
    replace_parser.add_argument('replacement', type=str, help='Replacement word.')
    
    args = parser.parse_args()

    if args.command == 'search':
        if args.find == "all":
            search.all(args.file, args.word, args.ret)
        if args.find == "key":
            search.keys(args.file, args.word, args.ret)
        if args.find == "value":
            search.values(args.file, args.word, args.ret)
    elif args.command == 'replace':
        replace.all(args.file, args.word, args.replacement)

if __name__ == '__main__':
    main()
