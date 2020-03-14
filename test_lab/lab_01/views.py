import time
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django import forms


# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'lab_01/index.html')


class About(View):

    def get(self, request):
        return render(request, 'lab_01/about.html')


class Blog(View):

    def __init__(self):
        self.blog_term = ["Food",
                          "Technology",
                          "Politics",
                          "Lifestyle",
                          ]
    
    def get(self, request):
        return render(request, 'lab_01/blog.html')


class BlogDetails(View):
    
    def get(self, request):
        return render(request, 'lab_01/blog-details.html')


class BlogView(View):
    
    def post(self, request):
        form_blog = UserEmailMessage()
        if form_blog.is_valid():
            html = """<div class="comment-list left-padding">
                       <div class="single-comment justify-content-between d-flex">
                         <div class="user justify-content-between d-flex">
                           <div class="thumb">
                            <img src="{% static "lab_01/img/blog/c2.jpg" alt="" %}">
                           </div>
                           <div class="desc">
                           <h5>
                    """
            html += f'<a href="#">{form_blog.data["name"]}</a>'
            html += """</h5>
                        <p class="date">{time.ctime()}</p>
                        <p class="comment">
                    """
            html += f"{form_blog.data['message']}</p>"
            html += """</div></div>
                       <div class="reply-btn">
                       <a href="#" class="btn-reply text-uppercase">reply</a>
                       </div></div></div>
                    """
            return HttpResponse(html)


class Contact(View):

    def get(self, request):
        return render(request, 'lab_01/contact.html')


class UserEmailMessage(forms.Form):
    name = forms.CharField(label="name", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Enter your name"}))
    email = forms.CharField(label="email", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Enter email address"}))
    subject = forms.CharField(label="subject", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Enter subject"}))
    message = forms.CharField(label="message", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Enter your message"}))


class MessageView(View):

    def post(self, request):
        form = UserEmailMessage(request.POST)
        if form.is_valid():
            html = f"<html><body> name: {form.data['name']}<br>email: {form.data['email']}<br>subject: {form.data['subject']}<br>\
                    message: {form.data['message']}<br></body></html>"
            return HttpResponse(html)
        else:
            html = "<html><body> Form is not valid </body></html>"
            return HttpResponse(html)

 
class Services(View):
    
    def get(self, request):
        return render(request, 'lab_01/services.html')


class UserEmail(forms.Form):
    email = forms.CharField(label="EMAIL", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Enter email address"}))


class EmailView(View):

    def get(self, request):
        e_form = UserEmail()
        return render(request, 'lab_01/services.html')

    def post(self, request):
        e_form = UserEmail(request.POST)
        if e_form.is_valid():
            html = f"<html><body> email: {form.data['email']}<br></body></html>"
            return HttpResponse(html)
        else:
            html = "<html><body> Not e-mail </body></html>"
            return HttpRespponse(html)

