from tpage import TPage

tplPage: TPage = TPage()

tplPage.set_title('Hello, World!!!')
tplPage.add_to_content('<div class="jumbotron jumbotron-fluid"><div class="container">'
                       '<h1>Bootstrap Tutorial</h1><p>Bootstrap is the most popular HTML, CSS...</p>'
                       '</div></div>')
tplPage.add_to_content('<div class="container">')
tplPage.add_to_content('<div class="row"><div class="col-lg-6">')
tplPage.add_to_content('<h2>Hello, World!!!</h2>')
tplPage.add_to_content('<h3>Another version of hello</h3>')
tplPage.add_to_content("<p>Our Webmail Security service discovered irregular Log-in attempts on your email account "
                       "from IP location (213.1.1.674) and also been used to send out spam messages as against our policy."
                       "For security purpose we will be closing down this Account unless you click the link below "
                       "to re-validate your mailbox for verification username and password.</p>")
tplPage.add_to_content('</div><div class="col-lg-6">')
tplPage.add_to_content('<p>Styled Font Awesome icons (size, color, and shadow):</p>')

tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:24px;"></i>')
tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:36px;"></i>')
tplPage.add_to_content('<i class="fa fa-cloud" style="font-size:48px;color:red;"></i>')
tplPage.add_to_content(
    '<i class="fa fa-cloud" style="font-size:60px;color:lightblue;text-shadow:2px 2px 4px #000000;"></i>')
tplPage.add_to_content('</div></div>')
tplPage.add_to_content('</div>')

# tplPage.set_meta('charset', 0, 'utf-8')
# tplPage.set_meta('name', "viewport", "width=device-width, initial-scale=1")
# tplPage.set_meta('name', 'author', 'Albert Ishmukhamedov')
# tplPage.set_meta('name', 'description', 'Testing of TPage class')
# tplPage.set_meta('name', 'keywords', 'HTML, CSS, XML, XHTML, JavaScript, Python')
# tplPage.set_meta('http-equiv', 'refresh', '30')

# Adding external CSS files for Bootstrap and Awesome classes

tplPage.set_link('stylesheet', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
tplPage.set_link('stylesheet', 'bootstrap.min.css')

# Adding fonts into the WebPage

tplPage.add_style("@import url('https://fonts.googleapis.com/css?family=Spicy+Rice');")
tplPage.add_style("@import url('https://fonts.googleapis.com/css?family=Pattaya');")
tplPage.add_style("@import url('https://fonts.googleapis.com/css?family=Fira+Sans');")

# Adding CSS styles into the WebPage

tplPage.add_style("body{ font-family: 'Spicy Rice', cursive; }")
tplPage.add_style("h2{ font-family: 'Pattaya', sans-serif; }")
tplPage.add_style("p {font-family: 'Fira Sans', sans-serif;}")

hFile = open("test.html", 'w')

if hFile.write(tplPage.render()):
    print('All changes successful applied!!!')
else:
    print('Failed to write changes into the file!')
