def convert(number):
    raindrops = ''
    if number % 3 == 0 :
        raindrops = raindrops + 'Pling'
    
    if number % 5 == 0 :
        raindrops = raindrops + 'Plang'

    if number % 7 == 0 :
        raindrops = raindrops + 'Plong'

    return str(number) if raindrops == '' else raindrops