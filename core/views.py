from django.views.generic import TemplateView

from task.models import Task
from user.models import Worker


class IndexView(TemplateView):
    template_name = "core/index.html"
    
    def get_context_data(self, **kwargs: object) -> object:
        context = super().get_context_data(**kwargs)
        context["num_workers"] = Worker.objects.count()
        context["num_not_completed_tasks"] = Task.objects.filter(is_completed=False).count()
        context["num_not_completed_fast_track_tasks"] = Task.objects.filter(
            is_completed=False,
            priority="Fast Track"
        ).count()
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits
        return context
