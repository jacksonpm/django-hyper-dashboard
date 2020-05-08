from django import forms
from django.db import models
from django.forms import CharField
from django.forms import Textarea, ClearableFileInput, CheckboxInput, DateInput
from django.forms.widgets import TimeInput, TextInput
from django.utils.safestring import mark_safe


class TimePickerInput(TimeInput):
    template_name = 'widgets/timepicker.html'


class URLDisplayInput(TextInput):
    template_name = 'widgets/url.html'
    pre = ''
    is_required = False
    show_full_url = True

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['pre'] = self.pre
        context['widget']['show_full_url'] = self.show_full_url
        return context


class DisplayInput(TextInput):
    template_name = 'widgets/display.html'
    is_required = False


class DisplayField(CharField):
    widget = DisplayInput

    def __init__(self, *largs, **kwargs):
        kwargs['required'] = False
        super().__init__(*largs, **kwargs)


class URLDisplay(CharField):
    widget = URLDisplayInput

    def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', pre='', **kwargs):
        self.widget.pre = pre
        kwargs['required'] = False
        super().__init__(max_length=max_length, min_length=min_length, strip=strip, empty_value=empty_value, **kwargs)

    def widget_attrs(self, widget):
        return super().widget_attrs(widget)


class AutosizedTextarea(Textarea):
    """
    AutoSized TextArea - TextArea height dynamically grows based on user input
    """

    def __init__(self, attrs=None):
        new_attrs = _make_attrs(attrs, {"rows": 2}, "autosize form-control")
        super(AutosizedTextarea, self).__init__(new_attrs)

    @property
    def media(self):
        return forms.Media(js=('suit/js/autosize.min.js',))

    def render(self, name, value, attrs=None, renderer=None):
        output = super(AutosizedTextarea, self).render(name, value, attrs, renderer)
        output += mark_safe(
            "<script type=\"text/javascript\">django.jQuery(function () { autosize(document.getElementById('id_%s')); });</script>"
            % name)
        return output


class CharacterCountTextarea(AutosizedTextarea):
    """
    TextArea with character count. Supports also twitter specific count.
    """

    def render(self, name, value, attrs=None, renderer=None):
        output = super(CharacterCountTextarea, self).render(name, value, attrs, renderer)
        output += mark_safe(
            "<script type=\"text/javascript\">django.jQuery(function () { django.jQuery('#id_%s').suitCharactersCount(); });</script>"
            % name)
        return output


class ImageWidget(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super(ImageWidget, self).render(name, value, attrs, renderer)
        if not value or not hasattr(value, 'url') or not value.url:
            return html
        html = u'<div class="ImageWidget"><div class="float-xs-left">' \
               u'<a href="%s" target="_blank"><img src="%s" width="75"></a></div>' \
               u'%s</div>' % (value.url, value.url, html)
        return mark_safe(html)


class EnclosedInput(TextInput):
    """
    Widget for bootstrap appended/prepended inputs
    """

    def __init__(self, attrs=None, prepend=None, append=None, prepend_class='addon', append_class='addon'):
        """
        :param prepend_class|append_class: CSS class applied to wrapper element. Values: addon or btn
        """
        self.prepend = prepend
        self.prepend_class = prepend_class
        self.append = append
        self.append_class = append_class
        super(EnclosedInput, self).__init__(attrs=attrs)

    def enclose_value(self, value, wrapper_class):
        if value.startswith("fa-"):
            value = '<i class="fa %s"></i>' % value
        return '<span class="input-group-%s">%s</span>' % (wrapper_class, value)

    def render(self, name, value, attrs=None, renderer=None):
        output = super(EnclosedInput, self).render(name, value, attrs, renderer)
        div_classes = set()
        if self.prepend:
            div_classes.add('input-group')
            self.prepend = self.enclose_value(self.prepend, self.prepend_class)
            output = ''.join((self.prepend, output))
        if self.append:
            div_classes.add('input-group')
            self.append = self.enclose_value(self.append, self.append_class)
            output = ''.join((output, self.append))

        return mark_safe('<div class="%s">%s</div>' % (' '.join(div_classes), output))


def _make_attrs(attrs, defaults=None, classes=None):
    result = defaults.copy() if defaults else {}
    if attrs:
        result.update(attrs)
    if classes:
        result["class"] = " ".join((classes, result.get("class", "")))
    return result


class DateInputCustom(EnclosedInput, DateInput):

    def __init__(self, attrs=None, prepend=None, append=None, prepend_class='addon', append_class='addon'):
        attrs = {'data-input-br': 'true'}
        super().__init__(attrs, prepend, append, prepend_class, append_class)


class SwitchInput(CheckboxInput):
    input_type = 'checkbox'
    template_name = 'widgets/switch.html'

    def __init__(self, attrs=None, check_test=None):
        if attrs is None:
            attrs = {'data-switch' : 'success'}
        else:
            attrs.update({'data-switch': 'success'})

        super().__init__(attrs, check_test)


formfield_overrides_base = {
    models.DateField: {'widget': DateInputCustom(append='fa-calendar'), },
    models.TextField: {'widget': AutosizedTextarea()},
    models.BooleanField: {'widget': SwitchInput()}
}
