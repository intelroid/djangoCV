from django.shortcuts import render
# from cv_app import form as contact_form
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse
from django_user_agents.utils import get_user_agent


def is_mobile(request):
    user_agent = get_user_agent(request)
    user_using_mobile = False
    if user_agent.is_mobile or user_agent.is_tablet:
        user_using_mobile = True
    return user_using_mobile


def cv(request):
    return render(request, 'cv.html', {'user_using_mobile': is_mobile(request)})


def about(request):
    return render(request, 'about_me.html', {'user_using_mobile': is_mobile(request)})


def skills(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, 'skill.html', {'user_using_mobile': True})
    return render(request, 'skill_prototype.html')


def skills_detailed(request):
    return render(request, 'skill.html', {'user_using_mobile': False})


def experience(request):
    return render(request, 'experience.html', {'user_using_mobile': is_mobile(request)})


def education(request):
    return render(request, 'education.html', {'user_using_mobile': is_mobile(request)})


def portfolio(request):
    return render(request, 'portfolio_cv.html', {'user_using_mobile': is_mobile(request)})


def contact(request):
    #if request.method == 'GET':
    #    form = contact_form.ContactForm()
    #else:
    #    form = contact_form.ContactForm(request.POST)
    #    if form.is_valid():
    #        subject = form.cleaned_data['subject']
    #        from_email = form.cleaned_data['from_email']
    #        message = form.cleaned_data['message']
    #        try:
    #            send_mail(subject, message, from_email, ['rekoc13@example.com'])
    #        except BadHeaderError:
    #            return HttpResponse('Invalid header found.')
            # return redirect('success')
    user_using_mobile = is_mobile(request)
    return render(request, 'contact_cv.html', {'user_using_mobile': is_mobile(request)})


def blog(request):
    return render(request, 'blog.html')
