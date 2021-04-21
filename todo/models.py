from django.db import models


# Create your models here.
class Item(models.Model):
    # Char = character, ie a text field
    # 'max_length' is an attribute, in this case max 50. the 'null' means cannot have a todo item without a name.
    # 'blank=False' will make the field required
    name = models.CharField(max_length=50, null=False, blank=False)
    # the 'default=False' makes the doto item not done by default
    done = models.BooleanField(null=False, blank=False, default=False)

    # taking the class itself as its own arguement - 'self'
    def __str__(self):
        return self.name
