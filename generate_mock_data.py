import random

def generate_picks(items, generated_string):

    picks_temp = []

    for _ in range(0,20):
        k = random.randint(1,3)
        picks = random.sample(items, k)
        picks.sort()
        if picks not in picks_temp:
            picks_temp.append(picks)

        generated_string += '"'
        
        for pick in picks:    
            generated_string += f'{pick},'

        generated_string = generated_string[:-1] + '",'
    
    return generated_string[:-1] + "]"


def main():
    maturity = ["Ideating", "Prototyping", "Commercializing", "Scaling", "Funding"]
    industry = ["Information technology and services"
            ,"Hospital & Health care"
            ,"Construction"
            ,"Retail"
            ,"Education"
            ,"Financial services"
            ,"Accounting"
            ,"Automotive"
            ,"Consulting"
            ,"Real Estate"
            ,"Food & Beverages"
            ,"Telecommunications"
            ,"Agriculture"
            ,"Chemicals"
            ,"Hospitality"
            ,"Mechanical and electrical engineering"
            ]
    expertise = ["Development"
            ,"Market research"
            ,"Engineering"
            ,"Design"
            ,"Testing and quality assurance"
            ,"Marketing"
            ,"Sales"
            ,"Manufacturing"
            ,"Patenting"
            ,"Strategy"
            ,"Finance"
            ,"Legal"
            ,"HR"
            ]

    maturity_str = "["
    industry_str = "["
    expertise_str = "["

    print(generate_picks(maturity, maturity_str))
    print(generate_picks(industry, industry_str))
    print(generate_picks(expertise, expertise_str))   


if __name__ == "__main__":
    main()
