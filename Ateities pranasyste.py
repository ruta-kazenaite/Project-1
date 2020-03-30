name = input ('What\'s your name? ')
age = input ('How old are you? ')
sex = input ('Are you male or female? ')
answer = input ('Do you want to know your future - answer yes or no? ')
if answer.startswith('y') or answer.startswith('Y') :
    print('Ok. Where should I start...')
    if int(age) < 18:
        print('You will live a long life. Everything is ahead of you.')
    if 18 < int(age) < 50:
        print('You are entering the middle of your life.')
    if int(age) > 50:
        print('You are in the second half of your life. Enjoy it while you can.')
    if sex.startswith('m') or sex.startswith('M'):
        if int(age) < 18:
            print('You will get into a lot of trouble.')
        if 18 < int(age) < 50:
            print('You will be very rich and very bored...')
        if int(age) > 50:
            print('You will start fishing.')
    if sex.startswith('f') or sex.startswith('F'):
        if int(age) < 18:
            print('You will make a lot of friends.')
        if 18 < int(age) < 50:
            print('You will find love, and lose it. And find it again. And lose it again.')
        if int(age) > 50:
            print('You will rediscover yourself.')
    if name[0] < 'N':
        print('Oh, and fun fact - your name\'s first letter is between A-M')
    else:
        print('Oh, and fun fact - your name\'s first letter is between N-Z')
    print('Did you know your name starts with ' + name[0] + "? " +
    'It means you\'re lucky!')
else:
    print('Your loss...')