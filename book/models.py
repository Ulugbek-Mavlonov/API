from django.db import models

# Create your models here.


class Talaba(models.Model):
    ism=models.CharField(max_length=30)
    familiya=models.CharField(max_length=30)
    age=models.IntegerField()
    image=models.ImageField()
    # country=(
    #     ("uzb","+998"),
    #     ("rus","+721"),
    #     ("usa","+132"),
    # )
    # phone=models.CharField(max_length=13, choices=country)
    # def __str__(self) -> str:
    #     return self.ism
    phone = models.CharField(max_length=15, verbose_name='Phone', help_text='Phone number in the format +998(__)_______')

    def __str__(self):
        return self.ism

    def get_phone_formatted(self):
        return f'+998({self.phone[:2]}) {self.phone[2:5]} {self.phone[5:]}'


    
    