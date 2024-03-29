from django.shortcuts import redirect

def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type!='doctor':
            return redirect('patient-dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view



def patient_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type!='patient':
            return redirect('doctor-dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view