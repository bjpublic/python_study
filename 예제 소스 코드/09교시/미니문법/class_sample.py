# 직업 클래스
class Character:
    def __init__(self, job):
        self.job_class = job

    def fireball(self):
        if self.job_class == "magician":
            print("fireball >> ***")
        else: 
            print("I can't do it")

# 마법사 만들기
new_character = Character("magician")
# 파이어볼 쏘기
new_character.fireball()

# 도둑 만들기
new_character2 = Character("theif")
# 파이어볼 쏘기
new_character2.fireball()