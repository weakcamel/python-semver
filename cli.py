"""python-semver CLI
Semantic Versioning Command Line Interface"""

import argparse
import semver


def create_parser():
    parser = argparse.ArgumentParser(description='Semantic Versioning CLI.')
    parser.add_argument('--compare', nargs=2, metavar=('a', 'b'),
                        help='Compare version `a` with version `b`')
    parser.add_argument('--bump_major', nargs=1, metavar='a',
                        help='Bump major version `a`')
    parser.add_argument('--bump_minor', nargs=1, metavar='a',
                        help='Bump minor version `a`')
    parser.add_argument('--bump_patch', nargs=1, metavar='a',
                        help='Bump patch version `a`')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Print python-semver version')
    return parser


def parse_args(args):
    if args.compare is not None:
        s = semver.compare(*args.compare)
    elif args.bump_major is not None:
        s = semver.bump_major(*args.bump_major)
    elif args.bump_minor is not None:
        s = semver.bump_minor(*args.bump_minor)
    elif args.bump_patch is not None:
        s = semver.bump_patch(*args.bump_patch)
    elif args.version:
        s = semver.__version__
    else:
        return
    return s


def main():
    parser = create_parser()
    args = parser.parse_args()
    s = parse_args(args)
    if s is None:
        parser.print_help()
    else:
        print(s)

if __name__ == '__main__':
    main()
