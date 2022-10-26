def test_home(api):
    """Page loads"""
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'URL' in resp.data

def test_no_url(api):
    """/12345 triggers a 404"""
    resp = api.get('/12345')
    assert resp.status == '404 NOT FOUND'

def test_takes_url(api):
    """/POST creates the url"""
    form_data = {'url_to_shorten': 'https://www.google.co.uk/'}
    resp = api.post('/', data=form_data)
    assert resp.status == '201 CREATED'
    assert b'localhost' in resp.data