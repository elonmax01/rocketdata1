from rest_framework import serializers

from shop.models import Factory, Dealer, Distributor, Retailer, IE, Employee, Product


class FactorySerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()

    def create(self, validated_data):
        return Factory.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('debt',)

class DistributorSerializer(serializers.ModelSerializer):
    factory = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    def create(self, validated_data):
        return Distributor.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    class Meta:
        model = Distributor
        fields = '__all__'
        read_only_fields = ('debt',)

class DealerSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    supplier = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Dealer.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    def get_supplier(self, obj):
        if obj.distributor:
            return DistributorSerializer(obj.distributor).data
        elif obj.factory:
            return FactorySerializer(obj.factory).data
        else:
            return None

    class Meta:
        model = Dealer
        fields = 'name', 'supplier', 'address', 'email', 'debt', 'created_on'
        read_only_fields = ('debt',)


class RetailerSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    supplier = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Retailer.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    def get_supplier(self, obj):
        if obj.dealer:
            return DealerSerializer(obj.dealer).data
        elif obj.distributor:
            return DistributorSerializer(obj.distributor).data
        elif obj.factory:
            return FactorySerializer(obj.factory).data
        else:
            return None

    class Meta:
        model = Retailer
        fields = 'name', 'supplier', 'address', 'email', 'debt', 'created_on'
        read_only_fields = ('debt',)

class IESerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    supplier = serializers.SerializerMethodField()

    def create(self, validated_data):
        return IE.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    def get_supplier(self, obj):
        if obj.retailer:
            return RetailerSerializer(obj.retailer).data
        elif obj.dealer:
            return DealerSerializer(obj.dealer).data
        elif obj.distributor:
            return DistributorSerializer(obj.distributor).data
        elif obj.factory:
            return FactorySerializer(obj.factory).data
        else:   
            return None

    class Meta:
        model = IE
        fields = 'name', 'supplier', 'address', 'email', 'debt', 'created_on'
        read_only_fields = ('debt',)

class EmployeeSerializer(serializers.ModelSerializer):
    display_company = serializers.SerializerMethodField()

    def get_display_company(self, obj):
        if obj.factory:
            return FactorySerializer(obj.factory).data
        elif obj.distributor:
            return DistributorSerializer(obj.distributor).data
        elif obj.dealer:
            return DealerSerializer(obj.dealer).data
        elif obj.retailer:
            return RetailerSerializer(obj.retailer).data
        elif obj.ie:
            return IESerializer(obj.ie).data
        else:   
            return None
        

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    class Meta:
        model = Employee
        fields = 'name', 'position', 'display_company'
        


class ProductSerializer(serializers.ModelSerializer):
    plant = serializers.StringRelatedField()
    dealers = DealerSerializer(many=True)
    distributors = DistributorSerializer(many=True)
    retailers = RetailerSerializer(many=True)
    ies = IESerializer(many=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

    class Meta:
        model = Product
        fields = 'name', 'plant', 'dealers', 'distributors', 'retailers', 'ies', 'model', 'price', 'date_of_birth'
