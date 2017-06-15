from time import strftime


def write_table(html, name='out-'):
    try:
        filename = "".join(i for i in name if i not in "\/:*?<>|^;~`!&")
        f = open(filename + strftime('%Y-%m-%d_%H-%M-%S') + '.html', 'w')
        f.write(html)
        f.close()
    except:
        print('write table error!')


def make_table(headers, data, name='out-', other_info=''):
    from html import escape
    html = '<!DOCTYPE html><html><body>'
    html += '''
    <script src="https://kryogenix.org/code/browser/sorttable/sorttable.js"></script> 
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">'''
    html += '<code>Generated: ' + strftime('%Y-%m-%d %H:%M:%S') + '</code>'
    if other_info:
        html += '<small> %s </small>' % other_info
    table = '<table class="table table-bordered table-hover sortable"> <tr>'
    for i in headers:
        table += '<th> %s </th>' % escape(i)
    table += '</tr>'
    for i in data:
        table += '<tr>'
        for j in i:
            table += '<td> %s </td>' % escape(j)
        table += '</tr>'
    html += table + '</table></body></html>'
    try:
        f = open(name + strftime('%Y-%m-%d_%H-%M-%S') + '.html', 'w')
        f.write(html)
        f.close()
    except:
        print('Oh no! Wrong name or something went wrong. Save emercy table')
        f = open('emercy_save' + strftime('%Y-%m-%d_%H-%M-%S') + '.html', 'w')
        f.write(html)
        f.close()

    print('end make table')


def make_body():
    pass


if __name__ == '__main__':
    head = ['one', 'two', 'tree']
    data = [('1', '2', 'w'), ('dd', 'u8i', 'dd')]
    make_table(head, data, other_info='151412 LLLs')
