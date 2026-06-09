import pytest
from jar import Jar

def test_init():
   jar = Jar(15)
   assert jar.capacity == 15
   assert jar.size == 0

   cookie = Jar()
   assert cookie.capacity == 12
   assert cookie.size == 0

   jar = Jar(24)
   assert jar.capacity == 24
   assert jar.size == 0

def test_str():
   jar = Jar()
   assert str(jar) == ""
   jar.deposit(1)
   assert str(jar) == "🍪"
   jar.deposit(11)
   assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
   jar = Jar()
   jar.deposit(2)
   assert jar.size == 2
   jar.deposit(6)
   assert jar.size == 8
   with pytest.raises(ValueError):
      jar.deposit(6)

def test_withdraw():
   jar = Jar()
   jar.deposit(8)
   jar.withdraw(2)
   assert jar.size == 6
   jar.withdraw(4)
   assert jar.size == 2
   with pytest.raises(ValueError):
      jar.withdraw(4)


