from django.forms import ValidationError

from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMinLength(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) <= self.min_length:
            raise ValidationError(
                f'The field must be at least {self.min_length} characters long.'
            )
    
    def __eq__(self, other):
        return self.min_length == other.min_length
        