def get_int_param(request, param_name, default_value):
    try:
        return int(request.GET.get(param_name, default_value))
    except (ValueError, TypeError):
        return default_value
    
def get_page_param(request, param_name, default_value, num_pages):
    page = get_int_param(request, param_name, default_value)
    if page > num_pages:
        return num_pages
    return page