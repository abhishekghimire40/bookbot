def words_count(str):
    words = file_contents.split()
    count = {}
    for i in words:
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

with open('/media/abhishek/Volume3/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()
    total_count = words_count(file_contents)
    print(total_count)