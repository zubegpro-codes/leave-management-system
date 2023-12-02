from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import CustomUser, Leaves
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
import json
from django.shortcuts import get_object_or_404
from base.forms import MyUserCreationForm, UserForm, LeaveForm


def home(request):
    q = request.GET.get('h') if request.GET.get('h') != None else ''
    leaves = Leaves.objects.filter(Q(user__username__icontains=q) |
                                   Q(description__icontains=q))
    unapproved_leaves = Leaves.objects.filter(status='unapproved')
    unapproved_count = unapproved_leaves.count()
    approved_leaves = Leaves.objects.filter(status='Approved')
    approved_count = approved_leaves.count()
    # leaves = Leaves.objects.all()
    leave_count = leaves.count()
    context = {'leaves': leaves, 'leave_count': leave_count, 'unapproved_count': unapproved_count,
               'approved_count': approved_count}
    return render(request, 'base/index.html', context)


def leave_tables(request):
    unapproved_leaves = Leaves.objects.filter(status='unapproved')
    unapproved_count = unapproved_leaves.count()
    approved_leaves = Leaves.objects.filter(status='Approved')
    approved_count = approved_leaves.count()
    context = {'unapproved_leaves': unapproved_leaves, 'unapproved_count': unapproved_count,
               'approved_leaves': approved_leaves, 'approved_count': approved_count}
    return render(request, 'base/leavetables.html', context)

@login_required(login_url='login')
def leave(request, pk):
    leaves = Leaves.objects.filter(id=pk)
    leave = Leaves.objects.get(id=pk)
    context = {'leaves': leaves}
    return render(request, 'base/leave.html', context)


@login_required(login_url='login')
def createleave(request):
    form = LeaveForm(request.POST)
    if form.is_valid():
        leave = form.save(commit=False)
        leave.user = request.user
        leave.save()
        return redirect('home')
    else:
        messages.error(request, form.errors)

    context = {'form': form, }
    return render(request, 'base/leave_form.html', context)


def update_leave_status(request):
    data = json.loads(request.body)
    print('hello this is the previous function', data)
    leaveId = data['leaveId']
    action = data['action']
    instance = get_object_or_404(Leaves, id=leaveId)
    if action == 'Approved':
        instance.status = action
        instance.save()
    elif action == 'Declined':
        instance.status = action
        instance.save()

    print('action', action)
    print('leaveId', leaveId)

    return JsonResponse({'message': 'itemwasadded'})


def set_email(request):
    return render(request, 'base/emailset.html', )


def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    page = 'Register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            print(user.email)
            print(user.username)
            subject= 'Welcome to Computerised Leave Mangement System '
            message= f'hi,{user.username} you are succecfully registerd in CLM system '
            email_from = settings.EMAIL_HOST_USER
            recipient_email = [user.email,]
            send_mail(subject,message,email_from,recipient_email)
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'There was an error in the form submission.')
    return render(request, 'base/login_register.html', {'form': form, 'page': page})

@login_required(login_url='login')
def sendEmail(request):
    user = request.user
    if request.method == 'POST':
        receiver_email = request.POST.get('eaddress')
        subject = 'Welcome to Computerised Leave Mangement System '
        print(user)

        messageme = f'hi,{user} you are succecfully registerd in CLM system '
        print(messageme)
        email_from = settings.EMAIL_HOST_USER
        recipient_email = [receiver_email]
        send_mail(subject, messageme, email_from, recipient_email)

    return render(request, 'base/mailing.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')