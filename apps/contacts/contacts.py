
class RequestLoggingMiddleware(object):
    def process_request(self, request):
        print request.method
        return None
