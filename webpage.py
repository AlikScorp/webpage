from tpage import TPage

tplPage = TPage()

tplPage.set_title('Hello, World!!!')
tplPage.add_to_content('<h2>Hello, World!!!</h2>')
tplPage.add_to_content('<p>This is a new test for body!!!</p>')
tplPage.add_to_content('<p>Styled Font Awesome icons (size, color, and shadow):</p>')

tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:24px;"></i>')
tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:36px;"></i>')
tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:48px;color:red;"></i>')
tplPage.add_to_content(
    '<i class="fa fa-cloud" style="font-size:60px;color:lightblue;text-shadow:2px 2px 4px #000000;"></i>')

# tplPage.set_meta('charset', 0, 'utf-8')
# tplPage.set_meta('name', "viewport", "width=device-width, initial-scale=1")
# tplPage.set_meta('name', 'author', 'Albert Ishmukhamedov')
# tplPage.set_meta('name', 'description', 'Testing of TPage class')
# tplPage.set_meta('name', 'keywords', 'HTML, CSS, XML, XHTML, JavaScript, Python')
# tplPage.set_meta('http-equiv', 'refresh', '30')
tplPage.set_link('stylesheet', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
tplPage.set_link('stylesheet', 'https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css')
tplPage.add_style("@import url('https://fonts.googleapis.com/css?family=Spicy+Rice');")
tplPage.add_style("body{ font-family: 'Spicy Rice', cursive; }")

hFile = open("test.html", 'w')

if hFile.write(tplPage.render()):
    print('All changes successful applied!!!')
else:
    print('Failed to write changes into the file!')
