from django.db import models

DROPDOWN1 = (
    ('ch', 'Choose'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

DROPDOWN2 = (
    ('ch', 'Choose'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


class Friend (models.Model):
    form_id = models.CharField (max_length=100, unique=True)
    drop_down_1 = models.CharField (max_length=3, choices=DROPDOWN1)
    drop_down_2 = models.CharField (max_length=3, choices=DROPDOWN2)
    check_box_1 = models.BooleanField ()
    Integer_box = models.IntegerField ()
    text_box = models.CharField (max_length=100, null=True, blank=True)
    dob = models.DateField (auto_now=False, auto_now_add=False)
    new_check_box_1 = models.BooleanField ()
    new_check_box_2 = models.BooleanField ()
    new_check_box_A = models.BooleanField ()
    new_check_box_B = models.BooleanField ()
    new_check_box_C = models.BooleanField ()
    new_check_box_D = models.BooleanField ()
    integerbox_A = models.IntegerField ()
    integerbox_B = models.IntegerField ()
    integerbox_C = models.IntegerField ()
    integerbox_D = models.IntegerField ()

    def __str__(self):
        return self.form_id
