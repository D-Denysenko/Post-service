def get_request_data(serializer_cls, request, *args, **kwargs):
    serializer = serializer_cls(data=request.data, *args, **kwargs)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data


def get_filter_params(request):
    params_for_exclude = [
        "no_page",
        "ordering",
        "limit",
        "offset",
        "page",
        "sortingBy",
        "location",
    ]
    filter_params = dict(request.GET.items())
    for param in params_for_exclude:
        filter_params.pop(param, None)

    return filter_params
