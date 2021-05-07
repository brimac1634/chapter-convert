import json

# chars_to_ignore = input('Enter characters to ignore:')

chapter_string = open('chapters.txt', 'r').read().replace('\n', ' ')

details_list = chapter_string.split(' ')

time_first = ':' in details_list[0]
final_chapter_list = []
current_chapter_name = ''
current_chapter_time = None

properties = ['number', 'title', 'time']

def add_to_list(title, time):
    current_chapter = {}
    
    current_chapter[properties[0]] = str(len(final_chapter_list) + 1)
    current_chapter[properties[1]] = str(title)
    current_chapter[properties[2]] = float(time)

    final_chapter_list.append(current_chapter)

print(details_list)
for item in details_list:
    if item == '':
        continue
    elif ':' not in item:
        current_chapter_name += f' {item}' if len(current_chapter_name) >= 1 else item
    else:
        chapter_timing = item.split(':')
        minutes = float(chapter_timing[0]) * 60
        seconds = float(chapter_timing[1])
        time = '%.2f' % round(minutes + seconds, 2)
        

        if time_first and len(current_chapter_name) >= 1:
            add_to_list(current_chapter_name, current_chapter_time)
            current_chapter_name = ''
            current_chapter_time = time
        elif time_first and len(current_chapter_name) < 1:
            current_chapter_time = time
        elif not time_first:
            add_to_list(current_chapter_name, time)
            current_chapter_name = ''

        

print(json.dumps(final_chapter_list, indent=4, sort_keys=False))
