import streamlit as st
from PIL import Image


def main():
    st.title("100 days Code Bootcamp Exercises")

    menu = ["Tip Calculator", "BMI", "Life Calendar",
            "Odd or Even", "Love Calculator", "Leap Year", "Treasure Island", "Banker Roulette", "Rock-Paper-Scisors", "Password Generator", "Hangman", "About"]
    choice = st.sidebar.selectbox('Selection Application', menu)
    ##"Tip Calculator"#################################################################################################
    if choice == "Tip Calculator":
        st.subheader('Shared Bill Tip Calculator')
        image = Image.open('images/tip.JPG')
        st.image(image, use_column_width=True)

        # print("Welcome to the tip Calculator.")
        st.markdown("""
        The Shared Bill Tip Calculator considers the cost of the service, number of people,
        and chosen tip percentage to calculate the tip per person, as well as the total
        cost per person.
        """)

        tot_bill = st.number_input("What was the total bill ? ")
        split_num = 1
        split_num = st.number_input(
            "How many people to split the bill ?")
        tip_perc = st.slider(
            "What percentage tip would you like to give ?", 5, 15, 10)
        st.write("Tip : ", tip_perc, "%")
        if st.button("Calculate"):
            result = (tot_bill+(tot_bill*(tip_perc/100)))/split_num

            st.write("Total Bill $", tot_bill)
            st.write("Tip %", tip_perc, "%")
            st.write("Number of People", split_num)

            st.success(f"Each person should pay :  ${round(result, 1)}")
        if st.checkbox("Learn more about tip around the world"):
            st.markdown("""
                A tip or gratuity is an extra sum of money paid to certain service workers for a
                provided service. Tip amounts, as well as acceptance, vary in different parts of
                the world. In some countries in East Asia such as Japan, tips are seen as insulting
                and can sometimes be interpreted as a bribe. In yet other countries such as the United
                States, tipping is widely expected, and in many cases, is even factored into a service
                worker's compensation towards satisfying the minimum wage requirement. This is important
                to note, since although tipping is entirely voluntary, many servers depend on tips to make
                a living in countries like the United States. As such, as a tourist, it can be helpful to
                research the tipping customs in the countries being visited. In the U.S. or any other country
                where tipping is expected, depending on the restaurant or the number of patrons at a table,
                gratuity may be automatically applied to the bill amount. As previously mentioned, tipping can
                be offensive in some countries, so although a citizen of the United States that is visiting
                another country may want to express their appreciation of the service provided, the gesture may
                in some cases result in the opposite effect.

                """)
            st.subheader(
                "map below  provides some information regarding whether or not a tip is expected, or how a tip may be received in certain regions, as well ")
            tip_map = Image.open('images/tip_map.JPG')
            st.image(tip_map, use_column_width=True)
            st.subheader(
                "table of typical tip amounts in the United States and Canada for different services.")
            tip_table = Image.open('images/tip_table.JPG')
            st.image(tip_table, use_column_width=True)

    ##"BMI"##################################################################################################
    if choice == "BMI":
        # https://www.calculator.net/bmi-calculator.html?ctype=standard&cage=33&csex=m&cheightfeet=65&cheightinch=10&cpound=160&cheightmeter=180&ckg=65&printit=0&x=64&y=23
        st.subheader('Body Mass Indice')
        image = Image.open('images/bmi.jpg')
        st.image(image, use_column_width=True)

        age = st.slider("Your Age :", 2, 120, 2)
        gender = st.radio("Your Gender : ", ('Male', 'Female'))

        height = st.number_input("Enter your Height in m : ")
        weight = st.number_input("Enter your Weight in Kg : ")

        if st.button("Calculate"):
            result = weight/(height*height)
            st.write("Your Height is : ", weight, " m")
            st.write("Your Weight is : ", height, " Kg")
            result = round(result, 0)
            if result < 18.5:
                st.error(f"your BMI is : {result}, You are underweight")
            elif result < 25:
                st.success(
                    f"your BMI is : {result}, You have a normal weight")
            elif result < 30:
                st.warning(
                    f" your BMI is : {result}, You  are slightly overweight ")
            elif result < 35:
                st.error(f"your BMI is : {result}, You  are obese")
            else:
                st.error(
                    f"your BMI is : {result}, You  have a Clinically Problem")
            ibm_fig = Image.open('images/bmi_fig.jpg')
            st.image(ibm_fig, use_column_width=True)
            st.text("Source : https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36")

    ##"Life Calendar"#####################################################################################
    if choice == "Life Calendar":
        # https://waitbutwhy.com/2014/05/life-weeks.html
        st.header('Life Calendar')
        st.markdown("""Supose you have 90 years to live according to your actual age
        how many days, weeks, months, years left ?""")
        st.subheader("Let check !!!")
        age = st.slider(
            "Select your age ?", 1, 90, 10)
        years = 90-int(age)
        month = years * 12
        weeks = years * 52
        days = years * 365
        st.write(age, "years old is your current age")
        st.write(
            "you have", days, "days", weeks, "Weeks", month, "Months", years, "Years  left")
        st.success("Life is very short be WISE")
        if st.checkbox("Learn more"):
            st.text("https://waitbutwhy.com/2014/05/life-weeks.html")

    ##"Odd or Even"#####################################################################################
    if choice == "Odd or Even":
        st.header('Odd or Even')
        num = st.number_input("Enter any Number")

        if st.button("Odd or Even"):
            if num % 2 == 0:
                st.write(num, " is a Even number")
            else:
                st.write(num, " is a Odd number")

    ##"Love Calculator"##################################################################################
    if choice == "Love Calculator":
        st.header("Love Calculator")
        image = Image.open('images/love_cal.jpg')
        st.image(image, use_column_width=True)
        print("Welcome to the Love Calculator!")

        name1 = st.text_input("What is your name? \n")
        name2 = st.text_input("What is their name? \n")
        # 🚨 Don't change the code above 👆
        name1 = name1.lower()
        name2 = name2.lower()
        two_names = name1 + name2
        true = str(two_names.count("t")+two_names.count("r") +
                   two_names.count("u")+two_names.count("e"))
        love = str(two_names.count("l")+two_names.count("0") +
                   two_names.count("v")+two_names.count("e"))
        score = int(true + love)
        if st.button("Calculate"):
            if score < 10 or score > 90:
                st.success(
                    f"Your score is {score}, you go together like coke and mentos")
            elif score >= 40 and score <= 50:
                st.success(f"Your score is {score}, you are alright together")
            else:
                st.warning(f"Your score is {score}.")
    ##"Leap Year"########################################################################################
    if choice == "Leap Year":
        from datetime import datetime
        today = datetime.today()
        datem = datetime(today.year, today.month, today.day)

        currentSecond = datetime.now().second
        currentMinute = datetime.now().minute
        currentHour = datetime.now().hour

        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        "Leap Year"
        st.header("Leap Year")
        st.write("Date & Time : ", currentDay, "-", currentMonth, "-",
                 currentYear, "<>", currentHour, ":", currentMinute, ":", currentSecond)
        image = Image.open('images/leap_y.jpg')
        st.image(image, use_column_width=True)

        year = st.number_input("Which year do you want to check ? ")
        year = int(year)

        if st.button("Check"):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        if year == currentYear:
                            st.success(f"{year} Is a leap year")
                        elif year < currentYear:
                            st.success(f"{year} Was a leap year")
                        else:
                            st.success(f"{year} Will be a leap year")

                    else:
                        if year == currentYear:
                            st.success(f"{year} Is not a leap year")
                        elif year < currentYear:
                            st.success(f"{year} Was not a leap year")
                        else:
                            st.success(f"{year} Will not be a leap year")
                else:
                    if year == currentYear:
                        st.success(f"{year} Is a leap year")
                    elif year < currentYear:
                        st.success(f"{year} Was a leap year")
                    else:
                        st.success(f"{year} Will be a leap year")
            else:
                if year == currentYear:
                    st.success(f"{year} Is not a leap year")
                elif year < currentYear:
                    st.success(f"{year} Was not a leap year")
                else:
                    st.success(f"{year} Will not be a leap year")
    ##"Treasure Island"##################################################################################
    if choice == "Treasure Island":
        st.header("Treasure Island")
        image = Image.open('images/treasure.jfif')
        st.image(image, use_column_width=True)

        st.markdown("# Your mission is to find the treasure.")

        direction = st.radio(
            "You're at across road. Choose the direction", ("left", "right"))
        direction.lower()
        if direction == "left":
            st.subheader(
                "You're to a lake. There is an island in the middle of the lake")
            whattodo = st.radio(
                "Type 'Wait' to wait for a boat or type 'Swim' to swim across : ", ("wait", "swim"))
            whattodo.lower()
            if whattodo == "wait":
                st.subheader(
                    "You arrive at the island unharmed. There is a house with 3 doors")
                which_door = st.radio(
                    "One red, one yellow, one blue. Which colour do you choose :  ", ("blue", "yellow", "red"))

                which_door.lower()
                if which_door == "red":
                    st.error("Barned by fire GAMEOVER")
                elif which_door == "blue":
                    st.error("Eaten by beast GAME OVER")
                elif which_door == "yellow":
                    st.success("YOU WIN !!!!")
                else:
                    st.error("GAME OVER")
            else:
                st.error("Attacked by trout GAME OVER")
        else:
            st.error("Fall into a hole GAME OVER")
    ##"Banker Roulette"##################################################################################
    if choice == "Banker Roulette":
        st.header("Banker Roulette")
        image = Image.open('images/diner.jpg')
        st.image(image, use_column_width=True)
        # Split string method
        import time
        names_string = st.text_input(
            "Type everybody's names, separated by a comma. ")
        st.text(
            "NB: notice that there is a space between the comma and the next name. ")
        names = names_string.split(", ")
        if st.checkbox("We are "):
            st.write(names)
        if st.button("Who will pay the bill today ? "):

            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                progress_bar.progress(percent_complete+1)

            with st.spinner('wait a moment ....'):
                time.sleep(5)
            # 🚨 Don't change the code above 👆

            # Write your code below this line 👇
            import random
            rando = random.randint(0, len(names))
            name = str(names[rando]).upper()
            st.success(f"{name} is going to buy the meal today")
            st.balloons()
        ############################"Banker Roulette"##############################################
    ##"Rock-Paper-Scisors"##############################################################################
    if choice == "Rock-Paper-Scisors":
        st.header("Rock-Paper-Scisors")
        image = Image.open('images/rock_paper_scisor.jpg')
        st.image(image, use_column_width=True)

        import random

        select = st.radio("Select either Rock or Paper or Scisors",
                          ("Rock", "Paper", "Scisors"))
        machine = ["Rock", "Paper", "Scisors"]
        rando = random.randint(0, len(machine)+1)

        if st.button("Play"):

            if select == "Rock":
                if machine[rando] == "Rock":
                    st.warning("It's a draw")

                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.warning("It's a draw")

            if select == "Rock":
                if machine[rando] == "Paper":
                    st.error("machine WIN")

                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.error("machine WIN")

            if select == "Rock":
                if machine[rando] == "Scisors":
                    st.success("You WIN")
                    st.write("You play : Rock")
                    rock = Image.open('images/h_rock.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.success("You WIN")
                    st.balloons()

            if select == "Paper":
                if machine[rando] == "Rock":
                    st.success("You WIN")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.success("You WIN")
                    st.balloons()

            if select == "Paper":
                if machine[rando] == "Paper":
                    st.warning("It's a draw")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.warning("It's a draw")

            if select == "Paper":
                if machine[rando] == "Scisors":
                    st.error("Machine WIN")

                    st.write("You play : Paper")
                    rock = Image.open('images/h_paper.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.error("Machine WIN")

            ###################################
            if select == "Scisors":
                if machine[rando] == "Rock":
                    st.error("Machine WIN")

                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Rock")
                    rock = Image.open('images/m_rock.jpg')
                    st.image(rock, use_column_width=True)
                    st.error("Machine WIN")

            if select == "Scisors":
                if machine[rando] == "Paper":
                    st.success("You WIN")
                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Paper")
                    paper = Image.open('images/m_paper.jpg')
                    st.image(paper, use_column_width=True)

                    st.success("You WIN")
                    st.balloons()

            if select == "Scisors":
                if machine[rando] == "Scisors":
                    st.warning("It's a draw")

                    st.write("You play : Scisors")
                    rock = Image.open('images/h_scisor.jpg')
                    st.image(rock, use_column_width=True)

                    st.write("Machine play : Scisors")
                    scisor = Image.open('images/m_scisor.jpg')
                    st.image(scisor, use_column_width=True)
                    st.warning("It's a draw")


if __name__ == "__main__":
    main()
