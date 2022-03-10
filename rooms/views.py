from math import ceil
from django.shortcuts import render
from . import models

def all_rooms(request):
    page = request.GET.get("page", 1) # url로부터 page 값을 가지고 옴
    page = int(page or 1) # '?page=' 처럼 불완전한 링크 처리용 코드
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit] # 특정 범위 데이터만 보여주는 코드
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {
            "all_rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count+1),
        },
    )