Кастомные комманды:
 - python3 manage.py csu
   (Создание суперюзера)
 - python3 manage.py cmu
   (создание модератора)
 - python3 manage.py cbu
   (создание обычного юзера)

 - python manage.py fill_payment
   НЕОБХОДИМ экзепляр Course.objects.get(pk=2)

   (Создание каждому юзеру экземляр модели Payment)