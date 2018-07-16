''' A Controller defines controller methods which handle http requests '''

class BlogController:
    def show(self):
        return view('blog')
