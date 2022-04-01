from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics_page(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic_page(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if not _check_topic_owner(request, topic):
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            curr_topic = form.save(commit=False)
            curr_topic.owner = request.user
            curr_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry_page(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if not _check_topic_owner(request, topic):
        raise Http404

    if request.method != 'POST':
        form = EntryForm
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry_page(request, entry_id):
    edit_entry = Entry.objects.get(id=entry_id)
    topic = edit_entry.topic
    if not _check_topic_owner(request, topic):
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=edit_entry)
    else:
        form = EntryForm(instance=edit_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': edit_entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def _check_topic_owner(request, topic):
    if request.user == topic.owner:
        return True
    return False
