from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
#     def get(self, request):
#         exsisting_data = Review.objects.get(id = 1)
#         form = ReviewForm(instance=exsisting_data)
#         return render(request, "reviews/review.html",{
#             "form":form
#         })
    form_class = ReviewForm
    model = Review
    # fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank_you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():   Validation handeled by FormView Class
#             form.save()
#             return HttpResponseRedirect("/thank_you")
#         return render(request, "reviews/review.html",{
#             "form":form
#         })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works!"
        return context
    
class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    
class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        print(review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
    