import os
from time import sleep
import google.generativeai as genai

genai.configure(api_key=open('api.txt','r').readline())
model = genai.GenerativeModel("gemini-2.0-flash")

def ai_text(p):
    try:
        return model.generate_content(p).text
    except:
        print('eror, waiting')
        sleep(5)
        return ai_text(p)

def create_files(file_names, file_extension):
    i = 1
    for name in file_names:
        # Construct the file name with the given extension
        file_name = f"{name}.{file_extension}"

        # Generate the prompt with clear instructions and context
        prompt = f"""
Create a notecard on the APUSH "Unit 8: Post WWII-1970s" topic {file_name}, using this following format:
WHEN: (exact date if possible, if not narrow it down to a specific time period...acts/laws, specific events, etc should have specific dates. AP exam questions are ALWAYS broken down into certain time frames; timelines will be very important)

WHO: (who is involved or who started the event or concept; if a person - who is the person, President, Doctor, lawyer, etc. that would be important to know) 

WHAT: (answer what the concept is or what the person did exactly or what happened specifically during an event 

IMPACT:Why is that significant? What did it lead to? What impact did the person or event or law have on the United States?

Here is a good example

## ID: Battle of Gettysburg

## When: July 1-3, 1863

## Who: 
* **Union:**  General George Meade and the Army of the Potomac
* **Confederate:** General Robert E. Lee and the Army of Northern [[Virginia]]

## What: 

A pivotal battle of the American Civil War fought in Gettysburg, [[Pennsylvania]]. It involved three days of intense fighting between Union and Confederate forces. The battle culminated in a decisive Union victory, marking a turning point in the war.

## Impact: Why Significant?: 
* **Turning Point:**  The Battle of Gettysburg marked the beginning of the end for the Confederacy. It crippled Lee's army and forced him to retreat back to [[Virginia]].
* **Union Momentum:** The victory boosted Union morale and strengthened the resolve to continue the war.
* **Increased Casualties:** Both sides suffered significant casualties, highlighting the immense human cost of the war.
* **Lincoln's [[Gettysburg Address]]:** Delivered on November 19, 1863, Lincoln's famous speech redefined the purpose of the war as a fight for freedom and equality, solidifying the importance of the Union victory.
* **Strategic Significance:** Gettysburg stopped Lee's invasion of the North, preventing a major victory for the Confederates and ultimately leading to the Union's success.

"""
 
        # Generate the text using the prompt
        
        prompt = f"""
Create an AP [[United States]] History rundown on {name}. Include events they were associated with, important legislation they signed, groups they were a part of, and their impact on the country.

- Make use of markdown formatting
- For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]]). The notes page for that will be generated solely off of its title, so make sure its specific enough.
- There are already many other notes pages that you can reference by doing the [[double brackets]]. Enclosing them in double brackets like this will create a link to the page with that title for the user. Here is a list of all of the other topic that have already been written about
PCUSA,IDS Unit 4,IDS Unit 5,APUSH Groups,APUSH Home,IDS Unit 8,APUSH people,ID Home,Republicans,IDs unit 2,IDS Unit 6,IDS Unit 7,IDS Unit 3,Harvard,United States,Civil War,Great Britain,France,Spain,Democrats,Speakeasies,Manhattan Project,Lend-Lease Act,Rugged Individualism,Non-Aggression Pact,Stock Market Crash of 1929,Fireside Chats,Harlem Renaissance,Battle of Midway,Model T,Holocaust,Axis Powers,Flapper,League of Nations,WPA,Rosie the Riveter,Battle of Stalingrad,Wagner Act,Treaty of Versailles,Great Depression,Return to Normalcy,D-Day,Bonus Army,Nazism,CCC,AAA,TVA,Executive Order 9066,Pearl Harbor Attack,Red Scare,Dust Bowl,Allied Powers,Roaring 20s,Bank Holiday,Fourteen Points,New Deal,Reconstruction Finance Corporation,Roosevelt Corollary (to Monroe Doctrine),Bull Moose Party,Booker T Washington,Sinking of the Lusitania,Teller Amendment,Old Immigration vs New Immigration,Open Door Policy,Atlanta Compromise,Tenement Housing,League of Nations,The Jungle,Urbanization,Spanish-American War,Central Powers,Treaty of Versailles,Sussex Pledge,Unrestricted Submarine Warfare,Platt Amendment,Triple Alliance,Plessy v Ferguson,Panama Canal,Pure Food and Drug Act,Great Chicago Fire,Bully Pulpit,Hull House,Chinese Exclusion Act,White Mans Burden,Teddy Roosevelt (as President),Sierra Club,Great White Fleet,Triple Entente,Ragtime Music,How the Other Half Lives,Election of 1912,White Man’s Burden,Social Gospel Movement,Progressivism,Wisconsin Idea (Robert LaFollete),Yellow Journalism,Imperialism 1890s-1950s,WEB Dubois,Zimmerman Telegram,Meat Inspection Act,Great Migration,Square Deal,Fourteen Points,Allied Powers WWII,Clayton Antitrust Act,Progressive Amendments (16-19).md,Great Society,Paris Accords,Energy Crisis 1973,New Frontier,Watergate Scandal,To Secure These Rights,Gulf of Tonkin Resolution,EPA,Vietnam War,Geneva Accords,Roe v Wade,Containment,Southern Christian Leadership Conference,Equal Rights Amendment,Marshall Plan,Montgomery Bus Boycott,Three Mile Island,NSC-68,National Highway Act,Medicare and Medicaid,Korean War,Cuban Missile Crisis,Moral Majority,Civil Rights Act of 1964,Brown v Board of Education,GI Bill,Taft-Hartley Act,Feminine Mystique,Greensboro Sit-ins,Camp David Accords,Baby Boom,McCarthyism,Civil Rights Movement,Truman’s Fair Deal,Levittown,NATO,Stagflation,Truman Doctrine,Tet Offensive,National Defense Education Act,Voting Rights Act of 1965,Cold War,Panic of 1819,Commonwealth System,Treaty of Ghent,Constitutional Convention,Second Great Awakening,McCulloch v Maryland,Worcester v Georgia,XYZ Affair,American Temperance Society,Election of 1800,Marbury vs Madison,Election of 1824,Naturalization Alien and Sedition Acts,Proclamation of Neutrality,Adams-Onis Treaty,Great Compromise,Era of Good Feelings,Embargo Act of 1807,Jays Treaty,Judiciary Act,Spoils System,Missouri Compromise,Treaty of Greenville,Utopian Societies,George Washingtons Farewell Address,Monroe Doctrine,Whiskey Rebellion,Nat Turner Rebellion,Tariff of Abominations,Report on the Public Credit,Bill of Rights,Nullification,Louisiana Purchase,Transcendentalism,Democracy in America,Republican Motherhood,Election of 1828,Capital Compromise,The American System,Report on Manufactures,VA and KY Resolutions,American Colonization Society,Scalawag,Uncle Toms Cabin,Anaconda Plan,Sharecroppers,Dred Scott v Sandford,Samuel Slater,Tenure of Office Act,Habaes Corpus civil war,sectionalism,Harpers Ferry Raid,Market Revolution,Battle of Gettsyburg,Gettysburg Address,Battle of Antietam,Fort Sumter,Compromise of 1850,Civil Rights Act of 1866,Radical Republicans,Election of 1860,Freeport Doctrine,15th amendment,Carpetbagger,Popular Sovereignty,New Republican Party 1850,Industrial Revolution,Bleeding Kansas,Jim Crow Laws,Black Codes,Free-soilers,13th amendment,Lincoln Douglas Debates,Compromise of 1877,Battle of Bull Run,Freedmans Bureau,Wilmot Proviso,14th amendment,Surrender at Appomattox Courthouse,Solid south,Shermans March to Sea,Fugitive Slave Act,The Assassination of Abraham Lincoln,Lowell Textile Mill,Cotton Gin,Emancipation Proclamation,Kansas-Nebraska Act,Reconstruction Act of 1867,Tenant Farming,Thomas Nast,Transcontinental Railroad,J.P. Morgan,Labor Unions,Populists,Presidential Election of 1896,Xenophobia,Political Machines,Lilliputians,Tammany Hall,Granger Laws,Dawes Severalty Act of 1887,Laissez-Faire Government,Gold Standard,Gilded Age,Cross of Gold Speech,Interstate Commerce Act 1887,John D. Rockefeller,Populist Party,Omaha Platform,Pendleton Act,Robber Barons,Andrew Carnegie,Bimetallism,Bessemer Process,House of Burgesses,Bacon’s Rebellion,Treaty of Paris 1776,Pequot War,Triangular Trade,Stono Rebellion,Battle of Yorktown,Proclamation of 1763,Mayflower Compact,Letters from a Farmer in Pennsylvania,Second Continental Congress,Headright System,French and Indian War,Indentured Servitude,Common Sense,Boston Massacre,Olive Branch Petition,The Wealth of Nations,Stamp Act,Puritans,Great Awakening,King Philip’s War,Battle of Saratoga,Sugar Act,Committees of Correspondence,First Continental Congress,Boston Tea Party,Tea Act,Intolerable Acts,Enlightenment,Lees Resolution,Townshend Act,Sons of Liberty,Battle of Bunker Hill,Albany Plan of Union,Salutary Neglect,Valley Forge,New Hampshire,Mississippi,Nebraska,Delaware,Texas,Minnesota,Nevada,Massachusetts,Alaska,New Mexico,Utah,Missouri,Iowa,South Dakota,Indiana,South Carolina,Virginia,Georgia,New York,North Carolina,Kentucky,Vermont,California,Pennsylvania,North Dakota,Arizona,Idaho,Colorado,Florida,States list,Maine,Wisconsin,Oregon,Wyoming,Washington,Illinois,Louisiana,Tennessee,West Virginia,Montana,Kansas,Oklahoma,Michigan,Connecticut,Hawaii,Ohio,Arkansas,Alabama,Maryland,Rhode Island,Philadelphia,New Jersey,William McKinley,Thomas Jefferson,Barack Obama,William Howard Taft,Benjamin Harrison,John Adams,Abraham Lincoln,Bill Clinton,John F. Kennedy,Millard Fillmore,James A. Garfield,Benjamin Franklin,James K. Polk,Harry S. Truman,Herbert Hoover,George W. Bush,Calvin Coolidge,George H. W. Bush,Alexander Hamilton,Grover Cleveland,Rutherford B. Hayes,Andrew Jackson,Dwight D. Eisenhower,Samuel Adams,William Henry Harrison,Henry David Thoreau,Zachary Taylor,James Monroe,John Tyler,Martin Van Buren,John Quincy Adams,Andrew Johnson,James Buchanan,Joe Biden,Ronald Reagan,Jimmy Carter,Warren G. Harding,Franklin Pierce,Franklin D. Roosevelt,Ulysses S. Grant,Chester A. Arthur,POTUS,Lyndon B. Johnson,John Hancock,Richard Nixon,James Madison,Theodore Roosevelt,Donald Trump,Gerald Ford,Woodrow Wilson,George Washington,Constitution of the United States,Declaration of Independence,Articles of Confederation,Federalist Papers,War of 1812,
        
        """
        response ="# [[POTUS]]\n"+ ai_text(prompt) 

        # Write the generated text to the file
        with open("./result/"+file_name.split(" - ")[0], 'w') as file:
            file.write(response)
            print('created '+file_name.split(" - ")[0])
        sleep(1)
        i += 1

file_names = open("topics.txt", "r").read().splitlines()
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 