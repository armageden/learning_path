def ping_pong_battle(thing1, thing2):
  if thing1['label'] > thing2['label']:
    return 1
  if thing1['label'] < thing2['label']:
    return -1
  
  if thing1['time_value']<thing2['time_value']:
    return 1
  if thing1['time_value']>thing2['time_value']:
    return -1
    
  return 0

def do_the_shuffle(waiting_list):
  for farhan in range(1, len(waiting_list)):
    this_one = waiting_list[farhan]
    han = farhan - 1
    #this time worked with han >= 0
    while han >= 0 and ping_pong_battle(waiting_list[han], this_one) > 0:
      waiting_list[han + 1] = waiting_list[han]
      han -= 1
      
    waiting_list[han + 1] = this_one

def start_the_madness():
  try:
    how_many = int(input())
    #kor kor kaj kor
    some_stuff = []
    for _ in range(how_many):
      a_sentence = input()
      chunks = a_sentence.split()
      
      label = chunks[0]
      clock_text = chunks[-1]
      hr, min = map(int, clock_text.split(':'))
      
      time_value = hr * 60 + min
      
      some_stuff.append({
        "label": label,
        "time_value": time_value,
        "full_sentence": a_sentence
      })
      
    do_the_shuffle(some_stuff)
    
    for item in some_stuff:
      print(item["full_sentence"])
      
  except (ValueError, IndexError):
    print("bad input")

start_the_madness()