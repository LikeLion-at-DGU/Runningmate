from django.test import TestCase
import json, datetime
from django.http import JsonResponse


date_num = "15"
year = datetime.date.today().year
month = datetime.date.today().month
# calendar = Calendar.objects.filter(datetime__contains=datetime.date(
#     year, month, int(date_num))).order_by('datetime')
# if calendar.length != 0:
#     if calendar.length == 1:
#         c0_title = calendar[0].title
#         c0_datetime = calendar[0].datetime
#         c1_title = None
#         c1_datetime = None
#     elif calendar.length > 0:
#         c0_title = calendar[0].title
#         c0_datetime = calendar[0].datetime
#         c1_title = calendar[1].title
#         c1_datetime = calendar[1].datetime
#     context = {
#         "status": "exist",
#         "title1": c0_title,
#         "datetime1": c0_datetime,
#         "title2": c1_title,
#         "datetime2": c1_datetime,
#     }
# else:
#     context = {"status": "null"}
# return JsonResponse(context)
# asdf = calendar.length
print(type(year))