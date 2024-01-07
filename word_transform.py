############################################
#author: Soumya Dayal
#username: sd9829
############################################

import collections
import sys


def wordGraph(filename, begin_word, end_word):
    with open(filename) as file:
        words = [line.rstrip() for line in file]

    if end_word not in words:
        print("No solution.")

    required_len = len(begin_word)
    required_words = []
    for word in words:
        if len(word) == required_len:
            required_words.append(word)

    adjacency_list = collections.defaultdict(list)
    for word in required_words:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            adjacency_list[pattern].append(word)

    visited_list = {begin_word}
    q = collections.deque([begin_word])
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == end_word:

                # print("soms check", visited_list)
                string_answer = '\n '.join(visited_list)
                print(string_answer)
                exit()
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for adjacent_word in adjacency_list[pattern]:
                    visited_list.add(adjacent_word)
                    q.append(adjacent_word)



def main():
    # args = sys.argv[1:]
    # filename = args[0]
    # begin_word = args[1]
    # end_word = args[2]
    wordGraph("exampleWords","short","abort")

main()
