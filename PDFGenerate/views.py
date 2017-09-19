from django.http import  HttpResponse
from django.http import  Http404
from django.template import loader
from django.shortcuts import render
from django.views import  generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import pdf
import pdfkit

'''


def index(request):

    users=pdf.objects.all()
    context={
        'allUsers':users,
    }
        #pdfkit.from_file('PDFGenerate/templates/PDFGenerate/pdf_form.html', 'out.pdf')

    return render(request,'PDFGenerate/pdf_form.html',context)

def pdfgen(request):

    # Create a  URL of our project and go to the template route
    projectUrl = request.get_host() + '/template'
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response
'''
class form(CreateView):
    model = pdf
    fields =['name','org','talk','person_image']

class view(generic.ListView):

    template_name = 'PDFGenerate/done.html'
    def get_queryset(self):
        return pdf.objects.all()

class admin(generic.ListView):
    template_name = 'PDFGenerate/admin.html'
    def get_queryset(self):
        return pdf.objects.all()

