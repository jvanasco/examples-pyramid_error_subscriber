from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'DebugTest'}


class Test1(object):
    def __init__(self,request):
        self.request = request
        raise ValueError('Error in Test1.__init__')
    
    @view_config(route_name='test-1', renderer='templates/mytemplate.pt')
    def test_1(self):
        return {'project': 'DebugTest'}
        
        
class Test2(object):
    def __init__(self,request):
        self.request = request
        
    @view_config(route_name='test-2', renderer='templates/mytemplate.pt')
    def test_2(self):
        raise ValueError('Error in Test2.test_2')
        return {'project': 'DebugTest'}



class Test3(object):
    def __init__(self,request):
        self.request = request
        
    @view_config(route_name='test-3', renderer='templates/mytemplate.pt')
    def test_3(self):
        return {'project': 'DebugTest'}
