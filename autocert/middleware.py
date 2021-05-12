# coding: utf-8
import logging
from django.http import HttpResponse, Http404
from .models import Challenge
from django.utils.deprecation import MiddlewareMixin
log = logging.getLogger(__name__)


class AcmeChallengeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith(u'/.well-known/acme-challenge/'):
            try:
                challenge = Challenge.objects.filter(path=request.path).latest()
            except Challenge.DoesNotExist:
                raise Http404
            else:
                return HttpResponse('{}'.format(challenge.validation))
