from jinja2.ext import  contextfunction, Markup
import wtforms


def setup_jinja2_environment(app):
    # Set global variables.
    app.jinja_env.globals.update({
        # 'render_hidden_fields': render_hidden_fields,
        'render_field': render_field,
        'render_form': render_form,
        'render_form_errors': render_form_errors,
    })
    return


@contextfunction
def render_text_field(field):

    error_class = 'has-error' if field.errors else ''

    label = """
        <label for="%s" class="col-lg-2 control-label">
            %s
        </label>
    """ % (field.id, field.label.text)

    input = """<div class="col-lg-10">
                   <input type="text" class="form-control" id="%s" name="%s" value="">
               </div>
            """ % (field.id, field.id)

    values = {
        'error_class':  error_class,
        'label':        label,
        'input':        input,
    }

    html = """
        <div class="form-group %(error_class)s">
            %(label)s
            %(input)s
        </div>
    """ % values

    return Markup(html)


@contextfunction
def render_password_field(field):
    error_class = 'has-error' if field.errors else ''

    label = """
        <label for="%s" class="col-lg-2 control-label">
            %s
        </label>
    """ % (field.id, field.label.text)

    input = """<div class="col-lg-10">
                   <input type="password" class="form-control" id="%s" name="%s" value="">
               </div>
            """ % (field.id, field.id)

    values = {
        'error_class':  error_class,
        'label':        label,
        'input':        input,
    }

    html = """
        <div class="form-group %(error_class)s">
            %(label)s
            %(input)s
        </div>
    """ % values

    return Markup(html)


@contextfunction
def render_textarea_field(field):
    error_class = 'has-error' if field.errors else ''

    label = """
        <label for="%s" class="col-lg-2 control-label">
            %s
        </label>
    """ % (field.id, field.label.text)

    input = """<div class="col-lg-10">
                   <textarea rows=30 class="form-control" id="%s" name="%s" value=""></textarea>
               </div>
            """ % (field.id, field.id)

    values = {
        'error_class':  error_class,
        'label':        label,
        'input':        input,
    }

    html = """
        <div class="form-group %(error_class)s">
            %(label)s
            %(input)s
        </div>
    """ % values

    return Markup(html)


@contextfunction
def render_field(context, field, form_name, label=None, single=False):

    if field.type == 'TextField':
        return render_text_field(field)
    if field.type == 'PasswordField':
        return render_password_field(field)
    if field.type == 'TextAreaField':
        return render_textarea_field(field)


@contextfunction
def render_form(context, form):

    single = len([field for field in form.__iter__() if not isinstance(field.widget, wtforms.widgets.HiddenInput)]) == 1
    html = ''.join([render_field(context, field, form.__class__.__name__, single=single) for field in form.__iter__()])
    errors = render_form_errors(context, form)

    return Markup('%s%s' % (errors, html))


@contextfunction
def render_form_errors(context, form):

    if not form.errors:
        return ''

    error = '<div class="alert alert-danger">' \
            'There were errors with your form submission. Please correct to continue. ' \
            '</div>'

    return Markup(error)
