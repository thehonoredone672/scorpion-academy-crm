from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.generic import TemplateView

def home(request):
    """Optional live status path for Render monitoring"""
    return JsonResponse({
        "status": "online",
        "application": "Scorpion Academy CRM",
        "message": "API is running successfully"
    })


urlpatterns = [
    # 🌟 CORE FRONTEND PAGES MAP 🌟
    # Root URL serves the login page
    path('', TemplateView.as_view(template_name='login.html'), name='login_page'),
    
    # Dashboard & Management Sections
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard_page'),
    path('attendance/', TemplateView.as_view(template_name='attendance.html'), name='attendance_page'),
    path('batches/', TemplateView.as_view(template_name='batches.html'), name='batches_page'),
    path('events/', TemplateView.as_view(template_name='events.html'), name='events_page'),
    path('exams/', TemplateView.as_view(template_name='exams.html'), name='exams_page'),
    path('fees/', TemplateView.as_view(template_name='fees.html'), name='fees_page'),
    path('leads/', TemplateView.as_view(template_name='leads.html'), name='leads_page'),
    path('settings/', TemplateView.as_view(template_name='settings.html'), name='settings_page'),
    path('students/', TemplateView.as_view(template_name='students.html'), name='students_page'),
    path('vault/', TemplateView.as_view(template_name='vault.html'), name='vault_page'),


    # ⚙️ BACKEND API ENDPOINTS ⚙️
    # System Status
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
