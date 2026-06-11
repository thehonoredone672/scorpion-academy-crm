from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render  # Custom import for direct file rendering

from sports.views_scheduling import BatchSchedulingView
from sports.views_progression import ProgressionEngineView
from students.views_enrollments import StudentEnrollmentView
from students.views_attendance import LiveAttendanceCheckInView
from finance.views import InvoiceCreatePaymentView

# 1. Define explicit rendering functions for your frontend pages
def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def attendance_view(request):
    return render(request, 'attendance.html')

def batches_view(request):
    return render(request, 'batches.html')

def events_view(request):
    return render(request, 'events.html')

def exams_view(request):
    return render(request, 'exams.html')

def fees_view(request):
    return render(request, 'fees.html')

def leads_view(request):
    return render(request, 'leads.html')

def settings_view(request):
    return render(request, 'settings.html')

def students_view(request):
    return render(request, 'students.html')

def vault_view(request):
    return render(request, 'vault.html')


def home(request):
    """Optional live status path for Render monitoring"""
    return JsonResponse({
        "status": "online",
        "application": "Scorpion Academy CRM",
        "message": "API is running successfully"
    })


urlpatterns = [
    # 🌟 CORE FRONTEND PAGES MAP (Explicitly rendered) 🌟
    path('', login_view, name='login_page'),
    path('dashboard/', dashboard_view, name='dashboard_page'),
    path('attendance/', attendance_view, name='attendance_page'),
    path('batches/', batches_view, name='batches_page'),
    path('events/', events_view, name='events_page'),
    path('exams/', exams_view, name='exams_page'),
    path('fees/', fees_view, name='fees_page'),
    path('leads/', leads_view, name='leads_page'),
    path('settings/', settings_view, name='settings_page'),
    path('students/', students_view, name='students_page'),
    path('vault/', vault_view, name='vault_page'),


    # ⚙️ BACKEND API ENDPOINTS ⚙️
    path('api/status/', home, name='api_status'),
    path('admin/', admin.site.urls),
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
