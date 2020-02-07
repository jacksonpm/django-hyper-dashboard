from django.forms.widgets import TimeInput


class TimePickerInput(TimeInput):
    template_name = 'widgets/timepicker.html'

