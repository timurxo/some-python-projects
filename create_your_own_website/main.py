import os
import webbrowser


class HtmlFrame(object):

    def __init__(self, name, contents):
        self.start = '<{}>'.format(name)
        self.end = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start}{0.contents}{0.end}".format(self)

    # write to html file
    def write_to_file(self, file=None):
        print(self, file=file)


# ======================== CREATE HEAD ==============================
class HtmlHead(HtmlFrame):

    # create 'head' tag and add 'title'
    def __init__(self, page_name):
        super().__init__('head', '')
        self._page_frame = HtmlFrame('title', page_name)
        self.contents = str(self._page_frame)


# ======================== CREATE BODY ==============================
class HtmlBody(HtmlFrame):

    # create '<body>' with contents
    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    # add various (any) tags to the body
    def add_stuff(self, name, contents):
        new_stuff = HtmlFrame(name, contents)
        self._body_contents.append(new_stuff)   # keep track of body contents

    # write from list to html file
    def write_to_file(self, file=None):
        for i in self._body_contents:
            self.contents += str(i)

        super().write_to_file(file=file)


# ======================== CREATE HTML DOC ==============================
class CreateHtml(object):

    def __init__(self, title=None):
        self._head = HtmlHead(title)
        self._body = HtmlBody()

    def add_stuff(self, name, contents):
        self._body.add_stuff(name, contents)

    def write_to_file(self, file=None):
        print('<html>', file=file)
        self._head.write_to_file(file=file)
        self._body.write_to_file(file=file)
        print('</html>', file=file)


# ======================== WRITE TO FILE ==============================
if __name__ == '__main__':

    user_name = input("Enter your name: ")
    website_name = input("How do you want to name your website? ")
    header1 = input("Please enter header: ")
    header2 = input("Please enter sub-header: ")
    website_body = input("Enter body for your website: ")
    img = input("Do you want to include image? (y/n): ")

    web_page = CreateHtml(website_name)
    web_page.add_stuff('h1', header1)
    web_page.add_stuff('h2', header2)
    web_page.add_stuff('p', website_body)
    web_page.add_stuff('h2', "By " + user_name)

    with open('website.html', 'w') as test_doc:
        print('<!DOCTYPE html>', file=test_doc)
        web_page.write_to_file(file=test_doc)
        if img == 'y'.casefold():
            print('<img src="image.jpeg" alt="Logo">', file=test_doc)

    # automatically open
    webbrowser.open('file://' + os.path.realpath('website.html'))




