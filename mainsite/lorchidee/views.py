from django.shortcuts import render
from django.http import HttpResponse, Http404
from os import path
from tabula import convert_into
from pandas import read_csv
from . import forms
from . import models


def index(request):
    """ Main page of the application """

    return render(request, "lorchidee/index.html")


def insertPlanning(request):
    """ Insert a new schedule """

    if request.method == 'POST':
        try:
            myDate = request.POST.get('laDate')
            myFile = request.FILES.get('srcfile')
            currentPath = path.dirname(__file__)
            csvFolder = path.join(currentPath, "csv")
            csvFile = path.join(csvFolder, "output.csv")
            # Converting the pdf file into csv file
            convert_into(myFile, csvFile, output_format="csv", pages='all')
            # Retrieving csv file and converting it into dataframe set
            dataSet = read_csv(csvFile)
            data = dataSet.values[:, :]
            for line in data:
                col = []
                for column in line:
                    col.append(column)
                new_entry = models.TimePlan.objects.create(
                    jour=myDate,
                    heure=col[0],
                    patient=col[1],
                    addrTel=col[2],
                    cotation=col[3],
                    assure=col[4],
                    honoraire=col[5],
                    finTraitement=col[6],
                    commentaires=" ",
                )

            return render(request, "lorchidee/insertplan.html", {'insertOK': True})

        except:
            return render(request, "lorchidee/insertplan.html", {'insertNOK': True})

    form = forms.DateForm()
    return render(request, "lorchidee/insertplan.html", locals())


def viewPlanning(request):
    """ View for schedule """

    if request.method == 'POST':
        try:
            day = request.POST.get("laDate")
            daysWork = models.TimePlan.objects.filter(jour=day).order_by('id')
            if daysWork:
                return render(request, "lorchidee/viewplan.html", {'daysWork': daysWork})
            else:
                return render(request, "lorchidee/viewplan.html", {'daysEmpty': True})
        except:
            pass

    return render(request, "lorchidee/viewplan.html", {'data': 'first'})


def saveComment(request):
    """ Saving the note """

    if request.method == 'POST':
        try:
            note = request.POST.get('note')
            number = request.POST.get('number')
            entry = models.TimePlan.objects.get(pk=number)
            entry.commentaires = note
            entry.save()
        except:
            return HttpResponse("This note has not been saved")

    return HttpResponse("This entry has been correctly saved to the database")




