from rest_framework import viewsets

from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents video model crud
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def update(self, request, *args, **kwargs):
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        print('headers')
        print(pp.pprint(request.META))
        # print('stream')
        # print(request.stream.read())
        print('body')
        print(request.body)
        print('data')  # <QueryDict: {}>  , empty query dict when using a different json parser
        print(request.data)
        return super(VideoViewSet, self).update(request, *args, **kwargs)
