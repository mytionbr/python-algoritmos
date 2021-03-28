from __future__ import annotations
from abc import ABC,abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):

    def useful_function_a(self) -> str:
        return "O resultado do produto A1"


class ConcreteProductA2(AbstractProductA):

    def useful_function_a(self) -> str:
        return "O resultado do produto A2"

class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> str:
        pass

class ConcreteProductB1(AbstractProductB):

    def useful_function_b(self) -> str:
        return "O resultado do produto B1"



class ConcreteProductB2(AbstractProductB):

    def useful_function_b(self) -> str:
        return "O resultado do produto B2"


def client_code(factory: AbstractFactory) -> None:

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()


if __name__ == "__main__":

    print("Client: testando o codigo do cliente com o primeiro tipo de fabrica")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: testando o codigo do cliente com o segundo tipo de fabrica:")
    client_code(ConcreteFactory2())