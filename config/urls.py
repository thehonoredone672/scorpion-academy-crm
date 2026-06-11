from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import TemplateView  # Standard view module for direct template parsing

from sports.views_progression import ProgressionEngineView
from students.views_enrollments import StudentEnrollmentView
from sports.views_scheduling import BatchSchedulingView
from students.views_attendance import LiveAttendanceCheckInView
from finance.views import InvoiceCreatePaymentView


def home(request):
    """
    Optional API status health check view.
    Moved from root path to keep system visibility separate from UI routing.
    """
    return JsonResponse({
        "status": "online",
        "application": "Scorpion Academy CRM",
        "message": "API is running successfully"
    })


urlpatterns = [
    # FIXED: Root URL now processes your custom frontend login.html directly
    path('', TemplateView.as_view(template_name='login.html'), name='login_page'),

    # Optional: Dedicated live status path for Render monitoring
    path('api/status/', home, name='api_status'),

    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication
    path('api/auth/', include('accounts.urls')),

    # Core Modules
    path('api/sports/', include('sports.urls')),
    path('api/branches/', include('branches.urls')),
    path('api/students/', include('students.urls')),
    path('api/', include('leads.urls')),

    # Sports Scheduling
    path(
        'api/sports/scheduling/batches/',
        BatchSchedulingView.as_view(),
        name='batch_scheduling'
    ),

    # Progression Engine
    path(
        'api/sports/<str:sport_id>/progression/',
        ProgressionEngineView.as_view(),
        name='progression_engine'
    ),

    # Student Enrollment
    path(
        'api/students/<str:student_id>/enroll/',
        StudentEnrollmentView.as_view(),
        name='student_enrollment'
    ),

    # Attendance Check-in
    path(
        'api/sessions/<str:session_id>/checkin/',
        LiveAttendanceCheckInView.as_view(),
        name='live_attendance_checkin'
    ),

    # Finance Ledger
    path(
        'api/finance/ledger/',
        InvoiceCreatePaymentView.as_view(),
        name='financial_ledger'
    ),
]
