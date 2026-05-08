import re

YT_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.7 15.5V8.5l6.3 3.5-6.3 3.5z"/></svg>'

def yt_block(vid_id, title, url):
    return (
        f'<h2>{title}</h2></div>\n'
        f'      <div class="video-wrap">\n'
        f'        <iframe src="https://www.youtube.com/embed/{vid_id}" allowfullscreen title="{title}"></iframe>\n'
        f'      </div>\n'
        f'      <div class="lesson-body">\n'
        f'        <div class="lesson-links">\n'
        f'          <a class="yt-link" href="{url}" target="_blank" rel="noopener">\n'
        f'            {YT_SVG}\n'
        f'            Watch on YouTube\n'
        f'          </a>'
    )

updates = [
    # module-01
    ('module-01.html', 'Create a New Project and C++ File in Visual Studio', '_1YSudub4Ss', 'https://youtu.be/_1YSudub4Ss'),
    ('module-01.html', 'C++ Fundamentals', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-01.html', 'Program Structure and Programming Process', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-01.html', 'Variables and Data Types', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-01.html', 'Basic Input and Output (I/O)', 'GNGIEZbu3n4', 'https://youtu.be/GNGIEZbu3n4'),
    ('module-01.html', 'Stream Manipulators', '7oNIoRnq6wQ', 'https://youtu.be/7oNIoRnq6wQ'),
    ('module-01.html', 'File Input and Output (I/O)', '_1YSudub4Ss', 'https://youtu.be/_1YSudub4Ss'),
    # module-02
    ('module-02.html', 'Assignments and Arithmetic Operators', 'YWzkSTASApk', 'https://youtu.be/YWzkSTASApk'),
    ('module-02.html', 'while Iteration Statement', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-02.html', 'do-while Iteration Statement', '1V7M-bEGPUs', 'https://youtu.be/1V7M-bEGPUs'),
    ('module-02.html', 'for Iteration Statement', 'QKqVEcettbs', 'https://youtu.be/QKqVEcettbs'),
    ('module-02.html', 'Nested Loops and Exit Statement', 'i-7z7Y7weok', 'https://youtu.be/i-7z7Y7weok'),
    # module-03
    ('module-03.html', 'Introduction to Functions', 'B4rkvRKwgUM', 'https://youtu.be/B4rkvRKwgUM'),
    ('module-03.html', 'Calling a Function', 'nKzLwgje_3E', 'https://youtu.be/nKzLwgje_3E'),
    ('module-03.html', 'Function Prototypes', '-FZyR0HsVwU', 'https://youtu.be/-FZyR0HsVwU'),
    ('module-03.html', 'Sending Data into a Function', '3XtfOn-eHbY', 'https://youtu.be/3XtfOn-eHbY'),
    ('module-03.html', 'Return a Value from a Function', '3XtfOn-eHbY', 'https://youtu.be/3XtfOn-eHbY'),
    ('module-03.html', 'Local and Global Variables', '3XtfOn-eHbY', 'https://youtu.be/3XtfOn-eHbY'),
    ('module-03.html', 'Static Local Variables and Default Arguments', 'ZIxDOrt2dWM', 'https://youtu.be/ZIxDOrt2dWM'),
    ('module-03.html', 'Reference Variables and Function Overloading', 'iY4Lubp8NsY', 'https://youtu.be/iY4Lubp8NsY'),
    # module-04
    ('module-04.html', 'Introduction to Arrays', 'WOfc5dvMukI', 'https://youtu.be/WOfc5dvMukI'),
    ('module-04.html', 'Accessing Array Contents', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-04.html', 'Array Initialisation and Assignment', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-04.html', 'Operations on Arrays', 'JI_iDgFNvWw', 'https://youtu.be/JI_iDgFNvWw'),
    ('module-04.html', 'Arrays in a Function', 'IgbseILd61k', 'https://youtu.be/IgbseILd61k'),
    ('module-04.html', 'Introduction to 2D Arrays', 'AaoZiklEVow', 'https://youtu.be/AaoZiklEVow'),
    ('module-04.html', 'Operations on 2D Arrays', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
    ('module-04.html', '2D String Array', 'pTeXqpiCI20', 'https://youtu.be/pTeXqpiCI20'),
]

base = 'public/programming/Cpp/'

for fname, title, vid_id, url in updates:
    path = base + fname
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    pattern = re.escape(f'<h2>{title}</h2></div>') + r'\s*\n\s*<div class="lesson-body">\s*\n\s*<div class="lesson-links">'
    replacement = yt_block(vid_id, title, url)
    new_html, n = re.subn(pattern, replacement, html)
    if n == 0:
        print(f'NO MATCH: {fname} / {title}')
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'OK ({n}): {fname} / {title}')

# Fix lesson 1-7 title from "Variables and Data Types" to "Variables & Data Types"
path = base + 'module-01.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<h2>Variables and Data Types</h2>', '<h2>Variables &amp; Data Types</h2>')
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Title fix: Variables & Data Types')
