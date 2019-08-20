from django.views.generic.edit import CreateView

from .models import Post

class CreatePostView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['text', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)