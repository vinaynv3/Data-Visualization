import json
from Main_class import get_country_code
from pygal.style import RotateStyle
from pygal.maps.world import World

file='population_data.json'
with open(file) as f:
    pop_data=json.load(f)

country_pop={}
for op in pop_data:
    if op['Year']=='2010':
        country=op['Country Name']
        population=int(float(op['Value']))
        code=get_country_code(country)
        if code:
            country_pop[code]=population
        #else:
            #print('ERROR', country)

cc_pop1,cc_pop2,cc_pop3={},{},{}
for cc,pop in country_pop.items():
    if pop <10000000:
        cc_pop1[cc]=pop
    elif pop <1000000000:
        cc_pop2[cc]=pop
    else:
        cc_pop3[cc]=pop
print(len(cc_pop1),len(cc_pop2),len(cc_pop3))

vi=World()
vi_style = RotateStyle('#336699')
vi= World(style=wm_style)
vi.title='Population of the world in 2010'
vi.add('0-10m', cc_pop1)
vi.add('10m-1bn', cc_pop2)
vi.add('>1bn', cc_pop3)
vi.render_to_file('newpopul.svg')

