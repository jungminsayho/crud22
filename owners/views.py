import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body) # request의 body를 json형태에서 dictionary형태로 바꿔주기
        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        dogs = Dog.objects.all()
        # dogs = owner.dogs_set.all() # 강아지 역참조해서 불러오기
        results = []
        for owner in owners: 
            results.append(
                {
                    "name": owner.name,
                    "email": owner.email,
                    "age": owner.age,
                    "dogs": [{'name': dog.name, 'age': dog.age} for dog in dogs if dog.owner.name == owner.name]                    
                }
            )
        return JsonResponse({'results': results}, status=200)



class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dog.objects.create(
            owner = Owner.objects.get(name=data['owner']),
            name = data['name'],
            age = data['age']
        )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs: 
            results.append(
                {
                    "owner": dog.owner.name,
                    "name": dog.name,
                    "age": dog.age
                }
            )
        return JsonResponse({'results': results}, status=200) 
