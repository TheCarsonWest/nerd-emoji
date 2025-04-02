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
Make a AP Chemistry note page on ({name}) in markdown format:
- make use of headings
- use the LaTeX equation library format when writing equations.($$Two dollar signs for a block equation$$, $One dollar sign for an inline equation$
- For any topic that you believe needs its own independent explanation, enclose it in TWO brackets([[like this]]). The notes page for that will be generated solely off of its title, so make sure its specific enough.
- There are already many other notes pages that you can reference by doing the [[double brackets]]. Enclosing them in double brackets like this will create a link to the page with that title for the user. Here is a list of all of the other topic that have already been written about
	- Solubility,Planck constant,ICE Table Examples,Acid Dissociation Constant,Order of Reaction,hybridization,Covalent Bonds,Photoelectron Spectroscopy,Ionization Energy,ion concentration,ICE Tables,Deviations from Ideal Gas Behavior,Thermodynamics,Collision reaction theory,Reaction Quotient,Conjugate Acid-Base Pairs,Acids and Bases,AP CHEM solutions,Sigma bond,Effusion Rate,pH and pOH,Gibbs Free Energy,Equilibrium Constant Calculations,Thermodynamic Favorability,Combustion Reaction,Solution Concentration,Coulombs Constant,Entropy,Endothermic,octet,Alloys,Bond Enthalpies,Lattice Energy,Electronegativity,Brønsted-Lowry Theory,Titration,Equilibrium Concentrations,delta symbol,Ideal Gas Laws,Speed of light,Distillation,Equilibrium Calculations,Gas Solubility,Solubility Product Constant,Le Chateliers Principle Examples,bond angle,Electrical constant,units of reaction constant,Redox,molarity,Endothermic and Exothermic Reactions,Reaction Rates,Universal Gas Constant,Combined Gas Law,Raoults Law,Acid Strength and Conjugate Base Strength,Polyprotic Acids,Ionic product of water Kw,formal charge,Common Ion Effect,Aufbau Principle,Lewis structures,Base Strength and Conjugate Acid Strength,Magnetic Constant,RF Value,Double replacement reaction,dipole,Reaction Mechanisms,Electrical Conductivity of Molecules,London Dispersion,Chemical Bonds,K_p and K_c Relationship,Polarizability,Equilibrium,Heat of Vaporization,Particulate Diagrams of Solutions,APCHEM Gasses,Le Chateliers Principle,chemical reactions,Approximations in Equilibrium Calculations,AP CHEM Experiments,Heat,Heterogeneous Equilibria Examples,Henrys Law,Polarity,partial pressure,Buffer Solutions,Single Replacement reaction,Saturation,Solving Equilibrium Expressions,Hydrogen Bonds,Finding reaction order,Water Autoionization,vapor pressure,Chemistry Laws,Reactions Types,Atomic Radius,Water as an Acid and Base,Activation Energy,Chemistry Constants,Rate from Reaction mechanism,Base Dissociation Constant,Periodic Trends,Synthesis Reaction,Amphoteric Substances,Reaction Kinetics,Hess Law,AP Chem Labs,Ka and Kb Relationships,Azeotropes,Pi Bond,Coulombs Law,Resonance Structures,Approximation Techniques,Temperature,Salt Hydrolysis,Rate Laws,Beer-Lambert Law,Electrolyte,Factors affecting rate of reaction,Calorimetry,Solubility Rules,Dilution Calculations,Other important AP CHEM things,Exothermic,Enthalpy,Electron Affinity,Acid-Base Indicators,Absolute Entropy and Entropy Change,Chromatography,intermolecular forces,APCHEM Home,Maxwell-Boltzmann Distribution,Van der Waals Gas Equation,Laws of Conservation,Decomposition reaction
        
        
        """
        response = ai_text(prompt)

        # Write the generated text to the file
        with open("./result/"+file_name.split(" - ")[0], 'w') as file:
            file.write(response)
            print('created '+file_name.split(" - ")[0])
        sleep(1)
        i += 1

file_names = open("topics.txt", "r").read().splitlines()
file_extension = "md"  # Change to your desired file type

create_files(file_names, file_extension)

 