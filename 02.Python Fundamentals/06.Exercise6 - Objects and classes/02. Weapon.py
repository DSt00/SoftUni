class Weapon:
    bullets = 0

    def __init__(self, bullets):
        Weapon.bullets = bullets

    def shoot(self):
        if Weapon.bullets > 0:
            Weapon.bullets -= 1
            return "shooting..."
        else:
            return 'no bullets left'

    def __repr__(self):
        return f'Remaining bullets: {Weapon.bullets}'

