from django.shortcuts import render


def homepage(request):
    """ Homepage of the application """

    home = True
    return render(request, 'cinetic/index.html', locals())

'''
def services(request):
    """ Page Services of the application """

    services = True
    return render(request, 'cinetic/services.html', locals())
'''

def projets(request):
    """ Page Projects of the application """

    projets = True
    return render(request, 'cinetic/projets.html', locals())


def contact(request):
    """ Page Contact of the application """

    contact = True
    return render(request, 'cinetic/contact.html', locals())
