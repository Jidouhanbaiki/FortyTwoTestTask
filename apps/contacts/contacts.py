from .models import RequestLog
import time


class RequestLoggingMiddleware(object):
    def process_request(self, request):
        if request.is_ajax():
            return None
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            remote_addr=request.META.get('REMOTE_ADDR') or "No data",
            http_user_agent=request.META.get('HTTP_USER_AGENT') or "No data",
            username=request.META.get('USERNAME') or "No data",
            time=time.time(),
        )
        return None
