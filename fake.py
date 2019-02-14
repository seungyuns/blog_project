from faker import faker

myfake = Faker()
#Faker 인자안에 'ko_KR' 을 쓰면 한국말 가능.
#faker의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼지 결정 가능
# ex myfake.name(), address(), text(), state() .....random_number()
#같은 랜덤 faker결과를 출력하기 위해 seed 를쓴다.
myfake.seed(#번호 지정)
printf(myfake.name())
