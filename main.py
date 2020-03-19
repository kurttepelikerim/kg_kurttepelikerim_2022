import sys

def is_one_to_one(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    else:
        char_map = {}
        for i,c1 in enumerate(s1):
            if c1 not in char_map:
                char_map[c1] = ord(s2[i])
            elif char_map[c1] != ord(s2[i]):
                return False
        return True


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python main.py <string1> <string2>",file=sys.stderr)
        exit()
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if is_one_to_one(s1,s2):
        print("true", file=sys.stdout)
    else:
        print("false", file=sys.stdout)
