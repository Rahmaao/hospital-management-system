import graphene
from graphene_django import DjangoObjectType
from core.models import Hospital


class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital
        field = ("id", "name", "address", "email", "phone_number", "website", "capacity")


class Query(graphene.ObjectType):
    list_hospitals = graphene.List(HospitalType)
    read_hospital = graphene.Field(HospitalType, id=graphene.Int())

    def resolve_list_hospitals(root, info):
        return Hospital.objects.all()

    def resolve_read_hospital(root, info, id):
        print(id)
        return Hospital.objects.get(id=id)


schema = graphene.Schema(query=Query)
