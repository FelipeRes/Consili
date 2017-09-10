from rest_framework import serializers
from core.models import *


class UserSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:user-detail")
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', User.USERNAME_FIELD, 'full_name', 'is_active',)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:profile-detail")

    class Meta:
        model = Profile
        fields = ('url', 'id', 'username', 'full_name', 'email',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:category-detail")

    class Meta:
        model = Category
        fields = ('url', 'id', 'name',)


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:task-detail")
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field="name")

    class Meta:
        model = Task
        fields = ('url', 'id', 'title', 'description', 'category',)


class PurchaseSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:purchase-detail")

    class Meta:
        model = Purchase
        fields = ('url', 'id', 'title', 'description', 'price',)


class RiskSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="api:risk-detail")

    class Meta:
        model = Risk
        fields = ('url', 'id', 'title', 'description', 'probability',)


class UserDetailSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active',)


class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'full_name', 'email', 'tasks',)


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'color', 'tasks')


class TaskDetailSerializer(serializers.HyperlinkedModelSerializer):

    risks = RiskSerializer(many=True, read_only=True)
    purchases = PurchaseSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'category', 'risks', 'purchases')


class RiskDetailSerializer(serializers.HyperlinkedModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ('id', 'title', 'description', 'probability', 'tasks',)


class PurchaseDetailSerializer(serializers.HyperlinkedModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = ('id', 'title', 'description', 'price', 'tasks',)