from django.shortcuts import render , get_object_or_404 , redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Board,Topic,Post
from django.urls import reverse_lazy , reverse
from .forms import TopicForm ,BoardForm , PostForm
from django.views.generic import View, CreateView , UpdateView, ListView , DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator

# Create your views here.


class BoardListView(ListView):
    model=Board
    context_object_name = 'board'
    template_name = 'home.html'

class TopicListView(ListView):
    model=Topic
    context_object_name = 'topic'
    template_name = 'topics.html'

    def get(self, request, pk, *args, **kwargs):
        board = Board.objects.get(pk=pk)
        return render(request, self.template_name, { "board": board})




    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super(SignUpView, self).form_valid(form)
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.method == 'POST':
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = request.user  
#             topic.save()
#             Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=request.user 
#             )
#             return redirect('board_topic', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form=TopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})

class NewBoardView(CreateView):
    model=Board
    form_class=BoardForm
    success_url = reverse_lazy('home')
    template_name='new_board.html'


class PostListView(ListView):
    model=Post
    context_object_name = 'post'
    template_name = 'topic_post.html'

    def get(self, request, pk,topic_pk, *args, **kwargs):
        board = Board.objects.get(id=pk)
        topic=Topic.objects.get(pk=topic_pk)
        return render(request, self.template_name, { "board": board,"topic": topic})

# @login_required
# def reply_topic(request,pk,topic_pk):
    
#     topic=get_object_or_404(Topic,board_id=pk,pk=topic_pk)
    
#     if request.method=="POST":
#         form=PostForm(request.POST)
    
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.topic=topic
#             post.created_by=request.user
#             post.save()
#             return redirect('topic_posts',pk=pk,topic_pk=topic_pk)

#     else:
#         form=PostForm()

#     return render(request,'reply_topic.html',{'topic':topic,'form':form})

class ReplyTopicView(CreateView):
   
    def get(self, request, pk,topic_pk , *args, **kwargs):
        topic = Topic.objects.get(board_id=pk , pk=topic_pk)
        context = {'form': PostForm,'topic':topic}
        return render(request, 'reply_topic.html', context)

    def post(self, request,pk,topic_pk , *args, **kwargs):
        form =PostForm(request.POST)
        if form.is_valid():
            topic=Topic.objects.get(board_id=self.kwargs['pk'],pk=self.kwargs['topic_pk'])
            post= form.save(commit=False)
            post.topic=topic
            post.created_by=request.user
            post.save()
            return HttpResponseRedirect(reverse('topic_posts', kwargs={'pk': topic.board.id , 'topic_pk':topic.id })) 


class NewTopicView(CreateView):
   
    def get(self, request, pk, *args, **kwargs):
        board = Board.objects.get(pk=pk)
        context = {'form': TopicForm(),'board':board}
        return render(request, 'new_topic.html', context)

    def post(self, request,pk, *args, **kwargs):
        form =TopicForm(request.POST)
        if form.is_valid():
            board=Board.objects.get(pk=self.kwargs['pk'])
            topic = form.save(commit=False)
            topic.board=board
            topic.starter=request.user
            topic.save()
            Post.objects.create(message=topic.message,topic=topic,created_by=request.user)
            return HttpResponseRedirect(reverse('board_topic', kwargs={'pk': board.id })) 
        
    



class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

class DeleteTopicView(DeleteView):
    model=Board,Topic
    context_object_name='topic'
    success_url = reverse_lazy('board_topic')

    def get(self,request,pk,topic_pk,*args,**kwargs):
        board=Board.objects.get(id=pk)
        topic=Topic.objects.get(pk=topic_pk)
        topic.delete()
        return render(request, 'topics.html', {"board": board})














