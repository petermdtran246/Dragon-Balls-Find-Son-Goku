print('''
`\-.   `
                      \ `.  `
                       \  \ |
              __.._    |   \.       S O N - G O K U
       ..---~~     ~ . |    Y
         ~-.          `|    |
            `.               `~~--.
              \                    ~.
               \                     \__. . -- -  .
         .-~~~~~      ,    ,            ~~~~~~---...._
      .-~___        ,'/  ,'/ ,'\          __...---~~~
            ~-.    /._\_( ,(/_. 7,-.    ~~---...__
           _...>-  P""6=`_/"6"~   6)    ___...--~~~
            ~~--._ \`--') `---'   9'  _..--~~~
                  ~\ ~~/_  ~~~   /`-.--~~
                    `.  ---    .'   \_
                      `. " _.-'     | ~-.,-------._
                  ..._../~~   ./       .-'    .-~~~-.
            ,--~~~ ,'...\` _./.----~~.'/    /'       `-
        _.-(      |\    `/~ _____..-' /    /      _.-~~`.
       /   |     /. ^---~~~~       ' /    /     ,'  ~.   \
      (    /    (  .           _ ' /'    /    ,/      \   )
      (`. |     `\   - - - - ~   /'      (   /         .  |
       \.\|       \            /'        \  |`.           /
       /.'\\      `\         /'           ~-\         .  /\
      /,   (        `\     /'                `.___..-      \
     | |    \         `\_/'                  //      \.     |
     | |     |                 _Seal_      /' |       |     |
     ''')

print("Welcome to Dragon Balls")
print("Your mission is to find Son-Goku")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'left':
  choice2 = input('You\'ve batteled with a dragon. Type "fight" or "run"\n').lower()
  if choice2 == 'run':
    choice3 = input("You arrive at the Kame House. here are 3 doors. One red, one yellow and one blue. Which color do you choose?? \n").lower()
    if choice3 == 'red':
      print('It\'s a room full of fire. Game Over.')
    elif choice3 == 'yellow':
      print('You found Son-Goku! You Win')
    elif choice3 == 'blue':
      print('You enter a room of beasts. Game Over.')
  else:
    print('You are killed by the dragon. Game Over.')
else:
  print('You found the wrong person. Game Over')



