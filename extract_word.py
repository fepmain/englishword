import re

pattern_word = r"(?a)\b\w+\b"
pattern_word_object = re.compile(pattern_word)



def find_word(p,s):
    w = []
    words= p.findall(s)
    for word in words:
        w.append(word.lower())
    return set(w)


s = """
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	LICENSE

no changes added to commit (use "git add" and/or "git commit -a")

"""




if __name__ == '__main__':
    w01 = find_word(pattern_word_object,s)
    print(w01)