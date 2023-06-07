def character_count(str):
    count = {}
    for i in str:
        if not i.isalpha():
          continue 
        i = i.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

with open('/media/abhishek/Volume3/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()
    total_words = len(file_contents.split())
    total_count = character_count(file_contents)
    sorted_count = sorted(total_count.items(),key=lambda item: item[1],reverse=True)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{total_words} words found in the document\n")
    for k,v in sorted_count:
        print(f"The '{k}' character was found {v} times")
    print(f"--- End Report ---")
        
    
    