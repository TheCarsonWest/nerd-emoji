implement this following code:
```python

def generate_relay_combinations(data):
    combinations = []
    for x in range(len(data)):
        for y in range(len(data)):
            for z in range(len(data)):
                for a in range(len(data)):
                    if len({x, y, z, a}) == 4:  # Ensuring no repetition of individuals
                        combination = [
                            (data[x][0], data[x][2]/2),
                            (data[y][0], data[y][3]/2),
                            (data[z][0], data[z][4]/2),
                            (data[a][0], data[a][1]/2)
                        ]
                        total_time = sum(time for (_, time) in combination)
                        combinations.append((combination, total_time))

    combinations.sort(key=lambda x: x[1])  # Sort combinations by total time
    return combinations

relay_combinations = generate_relay_combinations(data)
csv_filename = 'relay_combinations_f.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Total Time', 'Position 1 Name', 'Position 2 Name', 'Position 3 Name', 'Position 4 Name', 'Position 1 Time', 'Position 2 Time', 'Position 3 Time', 'Position 4 Time'])
    for index, (combination, total_time) in enumerate(relay_combinations, start=1):
        row = [
            total_time,
            combination[0][0], combination[1][0], combination[2][0], combination[3][0],
            combination[0][1], combination[1][1], combination[2][1], combination[3][1]
        ]
        csv_writer.writerow(row)

print(f"Successfully written relay combinations to {csv_filename}")
end = datetime.now()

td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")
```

to work with these classes and methods

```python


import json
import requests
import random
from relay import *
from openpyxl import load_workbook

def string_to_time(str): # mm:ss.ss -> Float point in fractions of a day
    
      f = 0
      if ":" in str:
        f += int(str.split(":")[0])*60
        f += int(str.split(":")[1].split(".")[0])
        f += int(str.split(".")[1])/100
      else:
            f+= int(str.split(".")[0])
            f+= int(str.split(".")[1])/100
      return f/86400

def time_to_string(fraction_of_day): # Day Fraction float point -> mm:ss.ss
    # Convert fraction_of_day to total seconds
    total_seconds = fraction_of_day * 86400

    # Calculate minutes and seconds
    minutes, seconds = divmod(total_seconds, 60)

    # Format the result as mm:ss.00
    result = f"{int(minutes):02}:{int(seconds):02}.{int((seconds % 1) * 100):02}"
    
    return result

def remove_last_word(sentence):
    words = sentence.rsplit(' ', 1)
    if len(words) > 1:
        return words[0]
    else:
        return ''


class Team: # Team Class, contains the name of the team, and a list of Swimmer objects who are on the team. Usage: team = Team("<url of home page>")
    def __init__(self, url = "b",u = "l",s = False):
        if u == 'j': # Json team loader
            t = json.loads(open(url,"r").read())
            self.name = t[0][0]
            self.url = t[0][1]

            self.team_m = []
            self.team_f = []
            for x in t[1]:
                self.team_m.append(Swimmer(x,"l"))

            for x in t[2]:
                self.team_f.append(Swimmer(x,"l"))

        elif url == "b": # Blank team loader
            self.team_m = []
            self.team_f = []
            self.url = "Blank"
            self.name = "Unnamed"
        else: # url loader
            print('Url detected, finding data')
            self.url = url # for safekeeping the future
            
            html_m = requests.get(url+"roster/?page=1&gender=M&season_id=27&sort=perf").text.split("<tbody>")[1].split("</tbody>")[0].split("<tr \n          >\n") # Cuts down the HTML page to just the roster
            html_f = requests.get(url+"roster/?page=1&gender=F&season_id=27&sort=perf").text.split("<tbody>")[1].split("</tbody>")[0].split("<tr \n          >\n")
            
            html_m.pop(0)
            html_f.pop(0)
            
            self.name = requests.get(url+"roster/?page=1&gender=M&season_id=27&sort=perf").text.split('<meta property="og:title" content="')[1].split('"')[0]
            
            self.team_m = []
            self.team_f = []
            for x in html_m:
                for x in html_m:
                    if 'href' not in x.split('            <td class="u-text-end">')[1]:
                        break
                    self.team_m.append(Swimmer("https://www.swimcloud.com" + x.split("</td>")[1].split("href=\"")[1].split("\">")[0]))
                    print(f"Added {self.team_m[-1].name}")
                    if s:
                        self.save()
                for x in html_f:
                    if 'href' not in x.split('            <td class="u-text-end">')[1]: ###
                        break
                    self.team_f.append(Swimmer("https://www.swimcloud.com" + x.split("</td>")[1].split("href=\"")[1].split("\">")[0]))
                    print(f"Added {self.team_f[-1].name}")
                    if s:
                        self.save()

    def __str__(self): # to string(very long)
        f = ''
        f += f"{self.name}\n{self.url}\n\nMen:\n"
        for x in self.team_m:
            f += str(x)
            f += '\n'
        f += "\n\nWomen:\n"
        for x in self.team_f:
            f += str(x)
            f += '\n'
        return f
    def save(self): # Saves file to json
        f = f'[ [\n"{self.name}",\n"{self.url}"\n],\n\t[\n'
        for x in self.team_m:
            f += x.save()
        f = f[0:len(f)-2]
        f += '\n\t],\n\t['
        for x in self.team_f:
            f += x.save()
        f = f[0:len(f)-2] # Gets rid of the last comma
        f += '\n\t]\n]'
        file = open(f"{self.name.replace(' ','_')}.json",'w')
        
        file.write(f)
    def add(self,player,gender="m"): # Adds Swimmer() to team_m or team_f
        if gender=="m":
            self.team_m.append(player)
        if gender=="f":
            self.team_f.append(player)
    def remove(self,player): # removes player by name
        for t in [self.team_m,self.team_f]:
            for p in range(len(t)):
                if t[p].name == player:
                    print("removed "+ t.pop(p))
    def refresh(self,person = -1):
        if person == -1:
            self = Team(self.url)

    def save_to_workbook(self, template_file = './template.xlsx'):
        # Load the template Excel file
        template_wb = load_workbook(template_file)
        
        # Get the desired sheet from the template file to combine data
        time_sheet = template_wb['Time Sheet']  # Assuming the sheet is named "Time Sheet"
        
        importer = []
        l = 2  # Starting row index
        
        for swimmer in self.team_m + self.team_f:
            s_name = swimmer.name
            for event, details in swimmer.times.items():
                r = [s_name]
                r.append(event)
                r.append(details[1])
                r.append("")  # Placeholder for the third column
                r.append(details[1])  # Assuming the same time
                r.append("")  # Placeholder for the sixth column
                r.append(details[0])  # String to time conversion (assuming it's the same format)
                r.append(swimmer in self.team_m)  # True for male, False for female
                r.append(f"=G{l}<HLOOKUP(B{l},Table7[#All],IF('Time Sheet'!H{l},3,2),FALSE)")
                importer.append(r)
                l += 1
        
        # Write data to the template sheet
        for row_data in importer:
            time_sheet.append(row_data)
        print("Time Sheet Created")
        
        # Add names to Boys and Girls sheets
        sheet_m = template_wb['Boys']
        sheet_f = template_wb['Girls']
        
        i = 2
        for swimmer in self.team_m:
            sheet_m[f"A{i}"] = swimmer.name
            i += 1
        
        i = 2
        for swimmer in self.team_f:
            sheet_f[f"A{i}"] = swimmer.name
            i += 1
        
        print('Names put in the sheet')
        
        # Save the workbook
        csv_filename = f"{self.name.replace(' ', '_')}.xlsx"
        template_wb.save(csv_filename)
        print(f"Workbook Saved as {csv_filename}")

    
class Swimmer:
    def __init__(self, url, u = "u"):
        if u == "l": # Loads from list(what a json load will do)
            
            self.name = url[0]
            self.url = url[1]
            self.times = url[2]

        else: # otherwise loads from url
            self.url = url
            html = requests.get(url).text.split("<body")[1].split('<span class="u-mr-">')[1]
            self.name = html.split('</span>')[0] # Scraping name from top of page
            self.times = {}
            table = html.split("<tbody>")[2].split("</tbody>")[0].split("</tr>")
            table.pop(-1)
            for x in table:
                
                td = x.split("</td>") # Scraping the times table
                self.times[td[0].split('<td class="u-text-truncate">')[1].split('class="js-event-link">')[1].split("</")[0]] = [string_to_time(td[1].split("</a>")[0].split('">')[2]),td[1].split("</a>")[0].split('">')[2]]
    def __str__(self):
        f = '' # Prints name an times
        f += f'{self.name}\n{self.url}\n'
        for x in self.times:
            f += str(x)+':  ' + self.times[x][1]
            f +='\n'
        return f
    def save(self): # formats to conform with Team() json
        f = f'\t\t[\n\t\t\t"{self.name}", "{self.url}",\n\t\t\t'+'{'
        for x in self.times:             
            f += f'\n\t\t\t\t"{str(x)}" : {self.times[x]},'.replace("'",'"')
        f = f[0:len(f)-1]
        f += '\n\t\t\t}\n\t\t],\n'
        return f

"""
Entries: {"Event" : [Swimmer, ...], ...}
Name: String
Date: Excel Format(Days since 1/1/1900) **NOT UNIX** 

"""
class Entry():
    def __init__(self, entries = {}, name = "Untitled team"): 
        self.entries = entries
        self.name = name



def get_ranks(team, event, num, s = True): # Returns the *num* fastest times in [name, time] format
    t = []
    f = []
    if s:
        for x in team.team_m:
            if event in x.times:
                t.append([x.name,x.times[event][0]])
            
        t = sorted(t, key=lambda x: x[1])
        for x in range(num):
            f.append(t[x])
        return f
        
    else: # Shot myself in the foot with these data structures, only way i know of doing this   
        for x in team.team_f:
            if event in x.times:
                t.append([x.name,x.times[event][0]])
            
        t = sorted(t, key=lambda x: x[1])
        for x in range(num):
            f.append(t[x])
        return f
    

def get_rank_obj(team, event, num, s=True):
  """Returns a sorted list of Swimmer objects with the fastest times for an event.

  Args:
      team: Team object containing swimmer data.
      event: Event name (e.g., "100 Free").
      num: Number of fastest times to return.
      s: Flag indicating men's (True) or women's (False) swimmers.

  Returns:
      A list of Swimmer objects sorted by their time in the specified event.
  """

  swimmers = []
  if s:
    for swimmer in team.team_m:
      if event in swimmer.times:
        swimmers.append(swimmer)
  else:
    for swimmer in team.team_f:
      if event in swimmer.times:
        swimmers.append(swimmer)

  # Sort swimmers by their time in the specified event
  swimmers.sort(key=lambda swimmer: swimmer.times[event][0])

  return swimmers[:num]




"""
Things to do add some point
make exportable to .hy3

"""

#events_order = ['200 Y Medley Relay Women','200 Y Medley Relay Men','200 Y Free Women','200 Y Free Men','200 Y IM Women','200 Y IM Men','50 Y Free Women','50 Y Free Men','100 Y Fly Women','100 Y Fly Men','100 Y Free Women','100 Y Free Men','500 Y Free Women','500 Y Free Men','200 Y Free Relay Women','200 Y Free Relay Men','100 Y Back Women','100 Y Back Men','100 Y Breast Women','100 Y Breast Men','400 Y Free Relay Women','400 Y Free Relay Men']
events_order = ['200 Y Free Women','200 Y Free Men','200 Y IM Women','200 Y IM Men','50 Y Free Women','50 Y Free Men','100 Y Fly Women','100 Y Fly Men','100 Y Free Women','100 Y Free Men','500 Y Free Women','500 Y Free Men','100 Y Back Women','100 Y Back Men','100 Y Breast Women','100 Y Breast Men']

"""
t : [Entry class, ...]
Point Scale: Default is the standard high school point scale
Point Swimmers: Most high school meets only allow 4 swimmers to compete for points

Divergence: [Lower, upper] The Random variability in times, how much percent can be added and dropped(scaled to wr) WIP
Fatigue: [Enabled, Decrease, Wear-off] WIP
 - Whether or not this feature is enabled
 - If fatigue is enabled, how much will it slow a swimmer down while doing consecutive events?
 - How many events will it take for fatigue to wear off(or how much time?)
"""


def hs_meet(t, point_swimmers = 4 ,divergence = [0,0], fatigue = [False,0,0],point_scale = [20,17,16,15,14,13,12,11,9,7,6,5,4,3,2,1]):
    s = [0] * len(t) # Scores for each team
    for event in events_order:
        psych_sheet = []
        for team in range(len(t)): # For every team in teams
            for swimmer in t[team].entries[event]: # For every swimmer in the team
                psych_sheet.append([swimmer,s[team]]) # Append [swimmer, score reference]
        psych_sheet.sort(key=lambda x: min(x[0].times[event]))
        

  





def best_entries(team, count): # Cheats and simply assigns the <count> best swimmers to each event, genetic algorithms relays
    # Made for testing purposes
    # Not legal event entries
    events = {}
    for x in events_order:
        if x not in ["200 Y Medley Relay Men","200 Y Free Relay Men","400 Y Free Relay Men","200 Y Medley Relay Women","200 Y Free Relay Women","400 Y Free Relay Women"]:
            events[x] = get_rank_obj(team,remove_last_word(x),count,"Men" in x)
    """
    best_relays = genetic_algorithm(team,10000,0,0)
    events["200 Y Medley Relay Men"] = best_relays[0]
    events["200 Y Free Relay Men"] = best_relays[1]
    events["400 Y Free Relay Men"] = best_relays[2]

    best_relays = genetic_algorithm(team,10000,0,0,False)
    events["200 Y Medley Relay Women"] = best_relays[0]
    events["200 Y Free Relay Women"] = best_relays[1]
    events["400 Y Free Relay Women"] = best_relays[2]

    """

    return Entry(events,team.name)

def genetic_entries(team): # Genetic algorithms entries WIP
    pass








```

```python
import csv
from datetime import datetime
import json
import requests
import random
from openpyxl import load_workbook

# ... (Existing code from your provided classes and methods)

def generate_relay_combinations(data, relay_type):
    """Generates relay combinations based on relay type."""
    combinations = []
    n = len(data)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                for a in range(n):
                    if len({x, y, z, a}) == 4:
                        if relay_type == "medley":
                            combination = [
                                (data[x].name, data[x].times.get('100 Y Back', [float('inf'), ''])[0] / 2),  # Use get with default for missing events
                                (data[y].name, data[y].times.get('100 Y Breast', [float('inf'), ''])[0] / 2),
                                (data[z].name, data[z].times.get('100 Y Fly', [float('inf'), ''])[0] / 2),
                                (data[a].name, data[a].times.get('100 Y Free', [float('inf'), ''])[0] / 2)
                            ]
                        elif relay_type == "free":
                            combination = [
                                (data[x].name, data[x].times.get('100 Y Free', [float('inf'), ''])[0] / 2),
                                (data[y].name, data[y].times.get('100 Y Free', [float('inf'), ''])[0] / 2),
                                (data[z].name, data[z].times.get('100 Y Free', [float('inf'), ''])[0] / 2),
                                (data[a].name, data[a].times.get('100 Y Free', [float('inf'), ''])[0] / 2)
                            ]
                        else:
                            raise ValueError("Invalid relay_type. Must be 'medley' or 'free'.")


                        if any(time == float('inf') for _, time in combination):
                            continue  # Skip combinations with missing times

                        total_time = sum(time for _, time in combination)
                        combinations.append((combination, total_time))

    combinations.sort(key=lambda x: x[1])
    return combinations


def write_relay_combinations_to_csv(combinations, csv_filename):
    """Writes relay combinations to a CSV file."""
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Total Time', 'Position 1 Name', 'Position 2 Name', 'Position 3 Name', 'Position 4 Name',
                             'Position 1 Time', 'Position 2 Time', 'Position 3 Time', 'Position 4 Time'])
        for index, (combination, total_time) in enumerate(combinations, start=1):
            row = [
                total_time,
                combination[0][0], combination[1][0], combination[2][0], combination[3][0],
                combination[0][1], combination[1][1], combination[2][1], combination[3][1]
            ]
            csv_writer.writerow(row)

    print(f"Successfully written relay combinations to {csv_filename}")



# Example usage:
start = datetime.now()
team = Team("<your_team_url>")  # Replace with your team's SwimCloud URL

relay_combinations_free = generate_relay_combinations(team.team_m, "free") # Example for men's free relay
write_relay_combinations_to_csv(relay_combinations_free, 'relay_combinations_free_men.csv')

relay_combinations_medley = generate_relay_combinations(team.team_f, "medley") # Example for women's medley relay
write_relay_combinations_to_csv(relay_combinations_medley, 'relay_combinations_medley_women.csv')


end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is :