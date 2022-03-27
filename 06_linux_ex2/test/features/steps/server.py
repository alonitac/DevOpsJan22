from behave import *
main = __import__('06_linux_ex2.tls_webserver.app')


@given('server is up and running')
def step_impl(context):
    main()


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False