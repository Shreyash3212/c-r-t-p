# middleware.py
# from django.http import HttpResponseRedirect

# class DesktopOnlyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

#         # Check if the user agent indicates a mobile or tablet device
#         if 'mobile' in user_agent or 'tablet' in user_agent:
#             return HttpResponseRedirect('/mobile-access-denied')  # Redirect to a mobile access denied page

#         response = self.get_response(request)
#         return response
