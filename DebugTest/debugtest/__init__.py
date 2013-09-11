from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('test-1', '/test-1')
    config.add_route('test-2', '/test-2')
    config.add_route('test-3', '/test-3')
    config.add_route('test-4', '/test-4')
    config.add_route('test-5', '/test-5')


    config.add_subscriber(\
        "debugtest.subscribers.BeforeRender",
        "pyramid.events.BeforeRender")


    config.scan()
    return config.make_wsgi_app()
