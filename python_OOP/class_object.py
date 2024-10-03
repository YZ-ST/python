from abc import ABC, abstractmethod
class AngryBird(ABC):
    def fly(self):
        pass

    def tweet(self):
        pass

    @abstractmethod
    def description(self):
        pass

class Red(AngryBird):
    def fly(self):
        print("Red flies in a straight line")

    def tweet(self):
        print("Red tweets 'Wii'")

    def description(self):
        print("A bird named Red")

class Chuck(AngryBird):
    def fly(self):
        print("Chuck flies fast")

    def tweet(self):
        print("Chuck is mute and does not tweet")

    def description(self):
        print("A bird named Chuck")

if __name__ == "__main__":
    red = Red()
    red.fly()
    red.tweet()
    red.description()

    chuck = Chuck()
    chuck.fly()
    chuck.tweet()
    chuck.description()