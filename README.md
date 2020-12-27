# Djnago를 이용한 RESTful API 구축

- 이 프로젝트를 위한 가상환경 생성 (venv)
    - `virtualenv venv --python=python3`

- `python3 -m pip install django`
- `python3 -m pip install djangorestframework`
- `python3 -m pip install django-filter`


### 데이터베이스와 sync하는 코드
`python3 manage.py migrate`

### admin 계정 생성
`python3 manage.py createsuperuser --email {자기이메일} --username admin`

### Serializer
- 첫번째 단계로, serializer를 정의한다.
- 새로운 모듈 이름인 tutorial/quickstart/serializers.py 를 생성한다.

```python3
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```

- 우리는 hyperlinked 관계를 `HyperlinkedModelSerializer`를 이용해 사용한다.
- 기본키와 다른 여러 관계들을 사용 할 수 있다.
- 하지만 hyperlinking은 아주 좋은 RESTful 설계이다.

### Views

- 간단한 view를 생성해보자.
- tutorial/quickstart/views.py를 다음과 같이 수정한다.
