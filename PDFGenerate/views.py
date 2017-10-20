from django.http import HttpResponse, HttpResponseRedirect
from django.http import  Http404
from django.template import loader
from django.shortcuts import render
from django.views import  generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Test.settings import BASE_DIR
from .models import pdf
from django.template.loader import get_template
from django.template import Context
from django.conf import settings


from .models import Comment
from .models import pdf

from .forms import AddCommentForm
from .forms import AddIdForm

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


class AddCommentView(CreateView):
    comment_form_class = AddCommentForm
    template_name = 'PDFGenerate/base.html'

    def post(self, request):
        comment_form = self.comment_form_class(request.POST, prefix='comment', auto_id=False)

        if comment_form.is_valid():
            comment = Comment()
            comment.message = comment_form.cleaned_data['message']

            return HttpResponseRedirect('/thanks/')
        return render(request, self.template_name, {
            "comment_form": comment_form
        })


def forms(request):
    template_name = 'PDFGenerate/base.html'
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        id_form=AddIdForm(request.POST,request.FILES)
        print (id_form)
        if form.is_valid():
            return render(request, 'PDFGenerate/pdf_form.html', {
                "field": pdf
            })
        elif id_form.is_valid():
            post = id_form.save(commit=False)
            post.user = request.user
            post.save()
        else:
            return HttpResponseRedirect('/thanks/')
    else:
        form = AddCommentForm()
    return render(request, template_name, {
        "comment_form": form
    })

'''

class form(CreateView):
    model = pdf
    fields =['name','org','talk','person_image']

    comment_form_class = AddCommentForm
    id_form_class = AddIdForm
    template_name = 'PDFGenerate/base.html'

    def post(self, request):
        comment_form = self.comment_form_class(request.POST, prefix='comment', auto_id=False)
        id_form = self.id_form_class(request.POST, prefix='comment', auto_id=True)
        pf = AddIdForm(request.POST, request.FILES)
        print(pf)

        if pf.is_valid():
            pf.save()
            return HttpResponseRedirect('/thanks/')
            #pf.name=id_form.cleaned_data['name']
            #pf.org= id_form.cleaned_data['org']
            #pf.talk = id_form.cleaned_data['talk']
            #pf.person_image = id_form.cleaned_data[' person_image']
        elif comment_form.is_valid():
            return render(request, 'PDFGenerate/pdf_form.html', {
                "field": pdf
            })

        return render(request, self.template_name, {
            "comment_form": comment_form
        })



'''
class view(generic.ListView):

    template_name = 'PDFGenerate/done.html'
    def get_queryset(self):
        return pdf.objects.all()



class admin(generic.ListView):
    template_name = 'PDFGenerate/admin.html'
    def get_queryset(self):
        return pdf.objects.all()


class gen(generic.ListView):
    template_name = 'PDFGenerate/done.html'


    def render_to_pdf(self,template_src, context_dict,id):
        #template = get_template(template_src)
        #context =Context({"data": context_dict})  # data is the context data that is sent to the html file to render the output.
        #html = template.render(context)  # Renders the template with the context data.
        html=get_template(template_src).render({
            "data": context_dict,
            "img" :BASE_DIR+context_dict.person_image.url
        })
        pdfkit.from_string(html, 'out'+str(id)+'.pdf')
        #pdf = open("out"+id+".pdf")
        #response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
        #response['Content-Disposition'] = 'attachment; filename=output.pdf'
        #pdf.close()
        # os.remove("out.pdf")  # remove the locally created pdf file.
        #return response  # returns the response.

    def myview(self):
        # Retrieve data or whatever you need
        for pdfs in pdf.objects.all():
            self.render_to_pdf('PDFGenerate/temp.html',pdfs,pdfs.id)


    def get_queryset(self):
        self.myview()
        return pdf.objects.all()



