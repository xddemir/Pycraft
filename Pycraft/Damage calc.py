while True:
    health = int(input("Enter characters health: ")) # num of hearts *4
    ActualArmour = int(input("Enter actual armour: ")) # num of armour *4
    Damage = float(input("Enter damage value: ")) # damage value (10 = 10 damage)
    Shield = int(input("Enter shield effectivenes: ")) # higher = better

    Damage = (Damage*5)
    Shield = 100-(Shield/50)

    ans = 10*(((1*Damage)/Shield)/ActualArmour)
    healthNUM = (health-ans)-0.12
    heartsNUM = ((health-ans)/4)-0.12

    if healthNUM <= -100:
        print("Character is dead, game over")
    else:
        print("health = ",round(healthNUM,0))
        print("hearts = ",round(heartsNUM,2), "/", health/4)
