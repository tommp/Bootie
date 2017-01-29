from index.models import FrontpageContext


def base_context(request):
    data = {}
    frontpageData = FrontpageContext.objects.order_by('-created')
    if frontpageData:
        data['frontpageData'] = frontpageData[0]
    else:
        data['frontpageData'] = []

    return data
