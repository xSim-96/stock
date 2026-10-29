
import json

def all_products(): #on - final
    # 1. Prikaži vse artikle
    print(f"{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}{"Zaloga": <12}{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <15}")
    print("-"*115)

    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
    
    for ID, item in products.items():
        name = item["name"]
        category = item["category"]
        current_stock = item["current_stock"]
        minimum_stock = item["minimum_stock"]
        unit = item["unit"]
        purchase_price = item["purchase_price"]
        
        print(
            f"{ID: <17}"
            f"{name: <20}"
            f"{category: <23}"
            f"{current_stock: <12}"
            f"{minimum_stock: <15}"
            f"{unit: <15}"
            f"{purchase_price: <4.2f} €"
        )
        
    print()

    while True:
        option = input("1 - meni, 0 - zapri: ")
        print()
        if option == "1":
            run()
            break
        elif option == "0":
            close_app()
            break
        else:
            print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")
            
def add_product(): #on - final
    # 2. Dodaj nov artikel
    # program določi šifro, vpraša po nazivu, kategoriji, začetni količini, minimalni zalogi, enoti mere in nabavni ceni
    # količina ne sme biti negativna, cena ne sme biti negativna, naziv ne sme biti prazen - v nasprotnem opozorilo + ponoven vnos
    
    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
      
    last_ID_num = list(products.keys())[-1][-3:]
    last_ID_num = int(last_ID_num) + 1
    last_ID_num = str(last_ID_num).zfill(3) 
    last_ID_art = list(products.keys())[-1][0:4]
    
    ID = last_ID_art+last_ID_num
    print(ID)

    while True: #name
        name = input("Naziv: ").strip() 
        if name == "0":
            print()
            run()
            break
        break

    while True: #category
        try:
            category = input("Kategorija: ").lower().strip()            
            if category == "embalaža":
                break                
            elif category == "pisarniški material":
                break
            elif category == "zaščitna oprema":
                break
            elif category == "pritrdilni material":
                break
            elif category == "čistila in higiena":
                break
            elif category == "orodje":
                break
            elif category == "električni material":
                break
            elif category == "0":
                print()
                run()
                break
            else:
                print("\033[31mVnesi pravilno kategorijo.\033[0m")
                option = input("\033[4mPritisni 8 za navodila ali enter za ponovni vnos:\033[0m ")
                if option == "8":
                    rules()
                else:
                    continue
        except ValueError:
            print("\033[31mVnesti moraš besedilo.\033[0m")
    
    while True: #current_stock
        try:
            current_stock = float(input("Zaloga: "))
            if current_stock == 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                print()
                run()
                break
            elif current_stock <= 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mVnesi \033[1m\033[4mštevilo\033[0m \033[31min uporabi decimalno \033[1m\033[4mpiko\033[0m.")
    
    while True: #minimum_stock
        try:
            minimum_stock = float(input("Minimalna zaloga: "))
            if minimum_stock == 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                print()
                run()
                break
            elif minimum_stock < 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mVnesi \033[1m\033[4mštevilo\033[0m \033[31min uporabi decimalno \033[1m\033[4mpiko\033[0m.")

    while True: #unit
        unit = input("Merska enota: ").lower().strip()
        if unit == "kos":
            break
        elif unit == "rola":
            break
        elif unit == "par":
            break
        elif unit == "paket":
            break
        elif unit == "kg":
            break
        elif unit == "m":
            break
        elif unit == "l":
            break
        elif unit == "0":
            print()
            run()
            break
        else:
            print("\033[31mVnesi pravilno mersko enoto.\033[0m")
            option = input("\033[4mPritisni 8 za navodila ali enter za ponovni vnos:\033[0m ")
            if option == "8":
                rules()
            else:
                continue
    
    while True: #purchase_price
        try:
            purchase_price = float(input("Nabavna cena: "))
            if purchase_price == 0:
                print("\033[31mVrednost mora biti pozitivna.\033[0m")
                print()
                run()
                break
            elif purchase_price < 0:
                print("\033[31mVrednost mora biti pozitivna.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mVnesi \033[1m\033[4mštevilo\033[0m \033[31min uporabi decimalno \033[1m\033[4mpiko\033[0m.")
        
    products[ID] = {
        "name": name,
        "category": category.capitalize(),
        "current_stock": current_stock,
        "minimum_stock": minimum_stock,
        "unit": unit.lower(),
        "purchase_price": purchase_price
    }

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print()
    print("\033[0;32mUspešen vnos!\033[0m")
    print()
    run()
    print()
    
def receive_stock(): #on - final
    # 3. Prevzem blaga
    # program vpraša po šifri in količini, ki smo jo prejeli
    # artikel mora obstajati, količina pozitivno število, program izpiše prejšnjo in novo količino - v nasprotnem opozorilo + ponoven vnos

    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
        
    while True: #ID
        ID = input("Šifra artikla: ").upper()
        if ID in products:
            print(f"\033[1m{products[ID]["name"]}\033[0m")
            break
        elif ID == "0":
            print()
            run()
            break
        else:
            print("\033[31mŠifra artikla ne obstaja.\033[0m")
            option = input("\033[4mPritisni 1 za seznam artiklov ali enter za ponovni vnos:\033[0m ")
            if option == "1":
                all_products()
            else:
                continue

    while True: #received_stock
        try:
            received_stock = float(input("Prejeta količina: "))
            if received_stock == 0:
                print()
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                print()
                run()
                break
            elif received_stock < 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mVnesi \033[1m\033[4mštevilo\033[0m \033[31min uporabi decimalno \033[1m\033[4mpiko\033[0m.")


    old_stock = products[ID]["current_stock"]
    products[ID]["current_stock"] = products[ID]["current_stock"] + received_stock

    print()
    print(f"\033[1m{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}\033[0m\033[31m{"Staro stanje": <16}\033[0m\033[1m{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <4}\033[0m")    
    print(
        f"{" ": <17}"
        f"{" ": <20}"
        f"{" ": <23}"
        f"\033[31m{old_stock: <16}\033[0m"
        f"{" ": <15}"
        f"{" ": <15}"
        f"{" ": <4}"
    )
    
    print(f"\033[3m{ID: <17}{products[ID]["name"]: <20}{products[ID]["category"]: <23}\033[0m\033[32m{"Novo stanje": <16}\033[0m\033[3m{products[ID]["minimum_stock"]: <15}{products[ID]["unit"]: <15}{products[ID]["purchase_price"]: <4.2f} €\033[0m")    
    print(
        f"{" ": <17}"
        f"{" ": <20}"
        f"{" ": <23}"
        f"\033[32m{products[ID]["current_stock"]: <16}\033[0m"
        f"{" ": <15}"
        f"{" ": <15}"
        f"{" ": <4}"
    )
    
    #še naredit izpis uspešno dodano (al pa ne?) in nadaljnjo izbiro , menu ali zapreti ... to gre izpod json.dump

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    while True:
            option = input("1 - meni, 0 - zapri: ")
            print()
            if option == "1":
                run()
                break
            elif option == "0":
                close_app()
                break
            else:
                print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")

def issue_stock(): #on - final
    # 4. Izdaja blaga
    # artikel mora obstajati, količina pozitivna, po uspešni izdaji prikazati novo količino, izdaja ne sme povzročiti negativne zaloge - v nasprotnem opozorilo + ponoven vnos
    
    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
        
    while True: #ID
        ID = input("Šifra artikla: ").upper()
        if ID in products:
            print(products[ID]["name"])
            break
        elif ID == "0":
            print()
            run()
            break
        else:
            print("\033[31mŠifra artikla ne obstaja.\033[0m")
            option = input("\033[4mPritisni 1 za seznam artiklov ali enter za ponovni vnos:\033[0m ")
            if option == "1":
                all_products()
            else:
                continue

    while True: #issued_stock
        try:
            issued_stock = float(input("Izdana količina: "))
            if issued_stock == 0:
                print()
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                print()
                run()
                break
            elif issued_stock < 0:
                print("\033[31mKoličina mora biti pozitivna.\033[0m")
                continue
            elif issued_stock > products[ID]["current_stock"]:
                print()
                print("\033[31mIzdana količina ne more biti večja od trenutne zaloge\033[0m")
                print()
                continue
            break
        except ValueError:
            print("\033[31mVnesi \033[1m\033[4mštevilo\033[0m \033[31min uporabi decimalno \033[1m\033[4mpiko\033[0m.")


    old_stock = products[ID]["current_stock"]
    products[ID]["current_stock"] = products[ID]["current_stock"] - issued_stock

    print()
    print(f"\033[1m{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}\033[0m\033[31m{"Staro stanje": <16}\033[0m\033[1m{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <4}\033[0m")    
    print(
        f"{" ": <17}"
        f"{" ": <20}"
        f"{" ": <23}"
        f"\033[31m{old_stock: <16}\033[0m"
        f"{" ": <15}"
        f"{" ": <15}"
        f"{" ": <4}"
    )
    
    print(f"\033[3m{ID: <17}{products[ID]["name"]: <20}{products[ID]["category"]: <23}\033[0m\033[32m{"Novo stanje": <16}\033[0m\033[3m{products[ID]["minimum_stock"]: <15}{products[ID]["unit"]: <15}{products[ID]["purchase_price"]: <4.2f} €\033[0m")    
    print(
        f"{" ": <17}"
        f"{" ": <20}"
        f"{" ": <23}"
        f"\033[32m{products[ID]["current_stock"]: <16}\033[0m"
        f"{" ": <15}"
        f"{" ": <15}"
        f"{" ": <4}"
    )
    
    #še naredit izpis uspešno dodano (al pa ne?) in nadaljnjo izbiro , menu ali zapreti ... to gre izpod json.dump

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    while True:
            option = input("1 - meni, 0 - zapri: ")
            print()
            if option == "1":
                run()
                break
            elif option == "0":
                close_app()
                break
            else:
                print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")

def low_stock_products(): #on - final
    # 5. Prikaži artikle z nizko zalogo
    # ko je njegova zaloga manjša ali enaka njegovi minimalni zalogi
    # prikaže samo artikle z nizko zalogo - če takih artiklov ni, naj to tudi pove
    
    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    found = False

    for ID, item in products.items():
        name = item["name"]
        category = item["category"]
        current_stock = item["current_stock"]
        minimum_stock = item["minimum_stock"]
        unit = item["unit"]
        purchase_price = item["purchase_price"]
        
        if current_stock <= minimum_stock:
            found = True
            print(
                f"\033[1m{"Šifra artikla": <17}\033[0m"
                f"\033[1m{"Naziv artikla": <20}\033[0m"
                f"\033[1m{"Kategorija": <23}\033[0m"
                f"\033[1m{"Zaloga": <16}\033[0m"
                f"\033[1m{"Min. zaloga": <15}\033[0m"
                f"\033[1m{"Merska enota": <15}\033[0m"
                f"\033[1m{"Nabavna cena": <4}\033[0m"
            )  
            print(
                f"{ID: <17}"
                f"{name: <20}"
                f"{category: <23}"
                f"\033[31m\033[1m{current_stock: <16}\033[0m"
                f"{minimum_stock: <15}"
                f"{unit: <15}"
                f"{purchase_price: <4.2f} €"
            )
            print()  
            
    if not found:
        print("\033[32mTrenutno je vseh artiklov dovolj na zalogi.\033[0m")
        print()

    while True:
            option = input("1 - meni, 0 - zapri: ")
            print()
            if option == "1":
                run()
                break
            elif option == "0":
                close_app()
                break
            else:
                print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")

def search_products(): #on - final
    # 6. Išči artikel
    # iskati po šifri, nazivu ali kategoriji
    print("\033[1m6.1. Išči po šifri\033[0m")
    print("\033[1m6.2. Išči po nazivu\033[0m")
    print("\033[1m6.3. Išči po kategoriji\033[0m")

    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
       
    def search_by_ID(): #on - final
        #6.1. Išči po šifri
        print("\033[1mIskanje po šifri\033[0m")
        while True:
            search_ID = input("Vnesi šifro: ").upper()
            if search_ID in products:
                product = products[search_ID]
                
                print()
                print(f"\033[1m{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}{"Zaloga": <12}{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <15}")
                print("-\033[0m"*115)
                print(
                    f"{search_ID: <17}"
                    f"{product["name"]: <20}"
                    f"{product["category"]: <23}"
                    f"{product["current_stock"]: <12}"
                    f"{product["minimum_stock"]: <15}"
                    f"{product["unit"]: <15}"
                    f"{product["purchase_price"]: <4.2f} €"
                )
                break
            else:
                print("Error")
                continue
        print()

        while True:
            option = input("1 - meni, 0 - zapri: ")
            print()
            if option == "1":
                run()
                break
            elif option == "0":
                close_app()
                break
            else:
                print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")
                
    def search_by_name(): #on - final
        #6.2. Išči po nazivu 
        print("\033[1mIskanje po nazivu\033[0m")

        while True:
            search_name = input("Vnesi naziv: ").lower()
            if search_name == "0":
                run()
                break
            print()            

            found = True

            for ID, item in products.items():
                name = item["name"]
                category = item["category"]
                current_stock = item["current_stock"]
                minimum_stock = item["minimum_stock"]
                unit = item["unit"]
                purchase_price = item["purchase_price"]

                if search_name not in item["name"].lower():
                    continue                                             

                if found:
                    print(f"\033[1m{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}{"Zaloga": <12}{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <15}")
                    print("-\033[0m"*115)
                    found = False                                       

                print(
                f"{ID: <17}"
                f"{name: <20}"
                f"{category: <23}"
                f"{current_stock: <12}"
                f"{minimum_stock: <15}"
                f"{unit: <15}"
                f"{purchase_price: <4.2f} €"
                )            
                
            if not found: #ko najde artikel
                print()
                while True:
                    option = input("1 - meni, 0 - zapri: ")
                    print()
                    if option == "1":
                        run()
                        break
                    elif option == "0":
                        close_app()
                        break
                    else:
                        print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")
                break 
            if found: #če ne najde artikla
                print("\033[31mArtikla ni mogoče najti.[0m")           
                                       
    def search_by_category(): #on
        #6.3. Išči po kategoriji
        print("\033[1mIskanje po kategoriji\033[0m")
        while True:
            search_category = input("Vnesi kategorijo: ").lower()
            if search_category == "0":
                run()
                break
            print()        

            found = True

            for ID, item in products.items():
                name = item["name"]
                category = item["category"]
                current_stock = item["current_stock"]
                minimum_stock = item["minimum_stock"]
                unit = item["unit"]
                purchase_price = item["purchase_price"]

                if search_category not in item["category"].lower():
                    continue
                if found:
                    print(f"\033[1m{"Šifra artikla": <17}{"Naziv artikla": <20}{"Kategorija": <23}{"Zaloga": <12}{"Min. zaloga": <15}{"Merska enota": <15}{"Nabavna cena": <15}")
                    print("-\033[0m"*115)
                    found = False                    
                    
                print(
                    f"{ID: <17}"
                    f"{name: <20}"
                    f"{category: <23}"
                    f"{current_stock: <12}"
                    f"{minimum_stock: <15}"
                    f"{unit: <15}"
                    f"{purchase_price: <4.2f} €"
                )   

            if not found: #če najde kategorijo
                print()
                while True:
                    option = input("1 - meni, 0 - zapri: ")
                    print()
                    if option == "1":
                        run()
                        break
                    elif option == "0":
                        close_app()
                        break
                    else:
                        print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")
                break 
            if found: #če ne najde kategorije
                print("\033[31mKategorije ni mogoče najti.[0m")      
    
    while True: #izbira vrste iskanja
        print()
        option = input("Vnesi možnost: ")
        print()
        if option == "6.1":
            search_by_ID()
            break
        elif option == "6.2":
            search_by_name()
            break
        elif option == "6.3":
            search_by_category()
            break
        elif option == "0":
            break
        else:
            print("\033[31mNeveljavna možnost. Poskusi znova.\033[0m")
            continue   

def inventory_value(): #on - final
    # 7. Prikaži skupno vrednost zaloge
    # prikaz skupne vrednosti zaloge v evrih, zaokroženo na dve decimalki
    
    with open ("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    total = 0

    for ID, item in products.items():
        current_stock = item["current_stock"]
        purchase_price = item["purchase_price"]

        total = total + (current_stock * purchase_price)

    print(f"Skupna vrednost zaloge je \033[1m\033[21m{total:.2f} €\033[0m")
    print()

    while True:
                option = input("1 - meni, 0 - zapri: ")
                print()
                if option == "1":
                    run()
                    break
                elif option == "0":
                    close_app()
                    break
                else:
                    print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")

def rules(): #on - final
    print("\033[32m=\033[00m"*8)
    print("NAVODILA")
    print("\033[32m=\033[00m"*8)
    print()
    print("- V vsakem trenutku, ko je na voljo vnos, se ob vnosu '0' vrneš v menu, razen kjer je drugače navedeno.")
    print()
    print("\033[1m- Pravilne kategorije so:\033[0m") 
    print("    Embalaža")
    print("    Pisarniški material")
    print("    Zaščitna oprema")
    print("    Pritrdilni material")
    print("    Čistila in higiena")
    print("    Orodje")
    print("    Električni material")
    print()
    print("\033[1m- Pravilne merske enote so:\033[0m") 
    print("    'kos', 'rola', 'par', 'paket', 'kg', 'm', 'l'")
    print()
    print("- Pri vnosu zaloge, minimalne zaloge in nabavne cene so dovoljene le številke, ki morajo biti ločene z decimalno \033[1mpiko\033[0m in ne vejico")
    print()
    print("- Vnesene morajo biti pozitivne vrednosti")
    print()
    print("- Na velike in male črke ni potrebno biti pozoren, na presledke pa je.")
    print()

    while True:
        option = input("\033[34m1 - meni, 0 - zapri:\033[0m ")
        print()
        if option == "1":
            run()
            break
        elif option == "0":
            close_app()
            break
        else:
            print("\033[31mNeveljavna možnost. Izberi 1 ali 0.\033[0m")
    #v vsakem trenutku 0 greš nazaj v menu
    #pravilne kategorije
    #pravilne merske enote
    #samo številke in decimalna pika!
    #pozitivne vrednosti
    #velike male črke nimajo veze .. presledki ?
    
def close_app(): #on - final
    # 0. Zapri program
    # ko se program zapre, se zaloga ne sme izgubiti
    print("\033[32mProgram je shranjen.\033[0m")    
    
def menu(): #on - final
    print("\033[32m=\033[00m"*26)
    print("SISTEM ZA VODENJE ZALOGE")
    print("\033[32m=\033[00m"*26)
    print()
    print("1. Prikaži vse artikle")
    print("2. Dodaj nov artikel")
    print("3. Prevzem blaga")
    print("4. Izdaja blaga")
    print("5. Prikaži artikle z nizko zalogo")
    print("6. Išči artikel")
    print("7. Prikaži skupno vrednost zaloge")
    print("8. Navodila")
    print("0. Zapri program")
    print()
    print("-"*35)
        
def run():
    menu()
    print()
    while True:
        option = input("Izberi možnost: ")
        print()
        if option == "1":
            all_products()
            break
        elif option == "2":
            add_product()
            break
        elif option == "3":
            receive_stock()
            break
        elif option == "4":
            issue_stock()        
            break
        elif option == "5":
            low_stock_products()
            break
        elif option == "6":
            search_products()
            break
        elif option == "7":
            inventory_value()
            break
        elif option == "8":
            rules()
            break
        elif option == "0": 
            close_app()           
            break
        else:
            print("\033[31mNeveljavna možnost. Poskusi znova.\033[0m")
               
run()

