from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Candidate
from .forms import CandidateForm


class CandidateCreateView(generic.CreateView):
    model = Candidate
    form_class = CandidateForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class CandidateListView(generic.ListView):
    model = Candidate
    template_name = "candidate_list.html"
    context_object_name = "candidates"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("candidate_id"):
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get("s")

        if query:
            return Candidate.objects.filter(
                first_name__icontains=query
            )

        return Candidate.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("candidate_id"):
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

class LoginView(generic.TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        login = request.POST.get("login")
        password = request.POST.get("password")
        captcha = request.POST.get("captcha")

        if captcha != "5":
            return self.get(
                request,
                error="Неверная CAPTCHA"
            )

        candidate = Candidate.objects.filter(
            login=login,
            password=password
        ).first()

        if candidate:
            request.session["candidate_id"] = candidate.id
            return redirect("candidate_list")

        return self.get(
            request,
            error="Неверный логин или пароль"
        )

    def get(self, request, error=None, *args, **kwargs):
        return self.render_to_response(
            {"error": error}
        )

    def get(self, request, error=None, *args, **kwargs):
        return self.render_to_response(
            {"error": error}
        )