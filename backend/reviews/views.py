from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from reviews.models import Review
from .forms import ReviewForm


class ReviewView(LoginRequiredMixin, FormView):
    model = Review
    template_name = 'reviews/user_review.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse_lazy('rate_user', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        initial = super().get_initial()
        try:
            review = Review.objects.get(
                reviewer__exact = self.request.user,
                reviewed__exact = get_user_model().objects.get(id=self.kwargs['pk'])
            )
            initial['rating'] = review.rating
            initial['review'] = review.review
        except:
            initial['rating'] = -1
            initial['review'] = ""
        return initial

    #def form_invalid(self, form):
    #    import pdb;pdb.set_trace()

    def form_valid(self, form):
        data = form.cleaned_data
        obj, created = Review.objects.update_or_create(
            reviewer = self.request.user,
            reviewed = get_user_model().objects.get(id=self.kwargs['pk']),
            defaults={
                'rating': data['rating'],
                'review': data['review'],
            },
        )
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
       context = super().get_context_data(*args, **kwargs)
       context['reviewed'] = self.kwargs['pk']
       return context
