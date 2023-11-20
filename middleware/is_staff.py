class IsStaffMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.is_staff = request.user.groups.filter(name='staff').exists()
        return self.get_response(request)