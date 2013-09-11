
def BeforeRender(event):
    request = event.get("request") or threadlocal.get_current_request()
    if request.path_info[:7] == '/test-3':
        raise ValueError("route matches test3")
