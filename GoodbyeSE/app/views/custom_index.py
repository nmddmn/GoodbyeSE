from flask_appbuilder import IndexView

class CustomIndexView(IndexView):
    index_template = 'custom_index.html'