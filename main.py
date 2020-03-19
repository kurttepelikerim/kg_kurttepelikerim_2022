import sys

def is_one_to_one(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    else:
        return len(set(s1)) >= len(set(s2))



if __name__ == '__main__':
    #error handling for illegal command line arguments not dealt with
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if is_one_to_one(s1,s2):
        print("true", file=sys.stdout)
    else:
        print("false", file=sys.stdout)
