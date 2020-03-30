name = input ('What\'s your name? ')
age = input ('How old are you? ')
sex = input ('Are you male or female? ')
answer = input ('Do you want to know your future - answer yes or no? ')
if answer.startswith('y') or answer.startswith('Y') :
    from time import sleep
    for i in range(27):
        print('Ok. Where should I start...'[i], sep='', end='', flush=False);
        sleep(0.1)
    if int(age) < 18:
        for i in range(55):
            print('\nYou will live a long life. Everything is ahead of you.'[i], sep='', end='', flush=False);
            sleep(0.1)
    if 18 < int(age) < 50:
        for i in range(42):
            print('\nYou are entering the middle of your life.'[i], sep='', end='', flush=False);
            sleep(0.1)
    if int(age) > 50:
        for i in range(65):
            print('\nYou are in the second half of your life. Enjoy it while you can.'[i], sep='', end='', flush=False);
            sleep(0.1)
    if sex.startswith('m') or sex.startswith('M'):
        if int(age) < 18:
            for i in range(36):
                print('\nYou will get into a lot of trouble.'[i], sep='', end='', flush=False);
                sleep(0.1)
        if 18 < int(age) < 50:
            for i in range(39):
                print('\nYou will be very rich and very bored...'[i], sep='', end='', flush=False);
                sleep(0.1)
        if int(age) > 50:
            for i in range(24):
                print('\nYou will start fishing.'[i], sep='', end='', flush=False);
                sleep(0.1)
    if sex.startswith('f') or sex.startswith('F'):
        if int(age) < 18:
            for i in range(32):
                print('\nYou will make a lot of friends.'[i], sep='', end='', flush=False);
                sleep(0.1)
        if 18 < int(age) < 50:
            for i in range(71):
                print('\nYou will find love, and lose it. And find it again. And lose it again.'[i], sep='', end='', flush=False);
                sleep(0.1)
        if int(age) > 50:
            for i in range(30):
                print('\nYou will rediscover yourself.'[i], sep='', end='', flush=False);
                sleep(0.1)
    if name[0] < 'N' or name[0] < 'n':
        for i in range(59):
            print('\nOh, and fun fact - your name\'s first letter is between A-M'[i], sep='', end='', flush=False);
            sleep(0.1)
    else:
        for i in range(59):
            print('\nOh, and fun fact - your name\'s first letter is between N-Z'[i], sep='', end='', flush=False);
            sleep(0.1)
    for i in range(36):
        print('\nDid you know your name starts with '[i], sep='', end='', flush=False);
        sleep(0.1)
    print(name[0] + "? ")
    for i in range(22):
        print('It means you\'re lucky!'[i], sep='', end='', flush=False);
        sleep(0.1)
else:
    from time import sleep
    for i in range(13):
        print('\nYour loss...'[i], sep='', end='', flush=False);
        sleep(0.1)
