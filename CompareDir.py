import sys
import os

def matchString(str1, str2):
    tokens1 = list(filter(lambda word: len(word) > 1, str1.lower().split(' ')))
    tokens2 = list(filter(lambda word: len(word) > 1, str2.lower().split(' ')))
    match = len(set(tokens1) & set(tokens2))

    return match / len(tokens1), match / len(tokens2)


def compareLines(dir1Files, dir2Files):
    threshold = 0.4
    distinct1 = set(dir1Files)
    distinct2 = set(dir2Files)
    matched = set()

    for file in dir1Files:
        for file2 in dir2Files:
            match = matchString(file, file2)
            if match[0] >= threshold and match[1] >= threshold:
                # if file in distinct1:
                distinct1.remove(file)
                # dir1Files.remove(file)
                matched.add(file2)
                break

    # for file in distinct2:
    #     if file in matched:
    #         distinct2.remove(file)

    return list(distinct1), list(distinct2 - matched)


def printLines(col1, col2):
    charLen = 50

    print("Folder 1: ")
    for file in col1:
        print(file[:charLen])

    print("\n" * 3)
    print("Folder 2: ")
    for file in col2:
        print(file[:charLen])

    print(len(distinct1))
    print(len(distinct2))


if __name__ == '__main__':
    # a = "Qudrat Ke Usoolon Mein Full (Audio) Song ｜ Pankaj Udhas ＂Mahek＂ Album Songs [74ISjGq7aDs].mp4"
    # b = "Qudrat Ke Usoolon Mein Full (Audio) Song _ Pankaj Udhas 'Mahek' Album Songs [74ISjGq7aDs].webm"
    # print(matchString(a, b))
    if len(sys.argv) != 3:
        print("Usage: %s <dir1> <dir2>" % sys.argv[0])
        sys.exit(1)

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        print("Error: %s is not a directory" % dir1)
        sys.exit(1)

    distinct1, distinct2 = compareLines(os.listdir(dir1), os.listdir(dir2))
    compareLines(distinct1, distinct2)
    printLines(distinct1, distinct2)


