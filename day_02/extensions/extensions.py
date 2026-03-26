'''
.gif .jpg .jpeg .png  image/
.pdf                  application/pdf
.txt                  text/plain
.zip                  application/zip
application/octet-stream
'''

file_name = input("File name: ").lower().strip()
ext = file_name[file_name.rfind('.'):]

match ext:
    case '.gif' | '.png':
        print(f'image/{ext[1:]}')
    case '.jpg' | '.jpeg':
        print('image/jpeg')
    case '.pdf' | '.zip':
        print(f'application/{ext[1:]}')
    case '.txt':
        print('text/plain')
    case _:
        print('application/octet-stream')
