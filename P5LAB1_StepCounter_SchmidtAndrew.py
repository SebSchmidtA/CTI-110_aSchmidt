def feet_to_steps(user_feet):
    steps_walked = user_feet / 2.5
    return int(steps_walked)
    



if __name__ == '__main__':
    feet = float(input())

    print(feet_to_steps(feet))
