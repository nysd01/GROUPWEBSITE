# Middleware to ensure session exists
class EnsureSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.session_key:
            request.session.create()
        response = self.get_response(request)
        return response