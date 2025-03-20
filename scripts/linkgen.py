import webbrowser

def generate_html(links, output_file="open_links.html"):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Open Links</title>
        <script>
            function openAllLinks() {{
                const links = {links};
                links.forEach(link => {{
                    window.open("./title.html?title="+link+"", '_blank');
                }});
            }}
        </script>
    </head>
    <body>
        <button onclick="openAllLinks()">Open All Links</button>
    </body>
    </html>
    """
    with open(output_file, "w") as file:
        file.write(html_content)
    print(f"HTML file generated: {output_file}")

# Example usage
if __name__ == "__main__":
    links = ["incontrovertible : Not able to be denied or disputed."
"integrity : The quality of being honest and having strong moral principles; moral uprightness.",
"objectivity : The quality of being objective.",
"penitent : Feeling or showing sorrow and regret for having done wrong; repentant.",
"plausible : (of an argument or statement) seeming reasonable or probable.",
"substantiated : Provide evidence to support or prove the truth of.",
"vindicated : Clear (someone) of blame or suspicion.",
"condescending : Having or showing a feeling of patronizing superiority.",
"contemptuous : Showing contempt; scornful.",
"despotic : Of or typical of a despot; tyrannical.",
"dictatorial : Of or characteristic of a dictator.",
"disdain (n.) : The feeling that someone or something is unworthy of one's consideration or respect; contempt.",
"disdain (v.) : Consider to be unworthy of one's consideration.",
"haughty : Arrogantly superior and disdainful.",
"imperious : Assuming power or authority without justification; arrogant and domineering.",
"patronizing : Treat with an apparent kindness that betrays a feeling of superiority.",
"convoluted : (especially of an argument, story, or sentence) extremely complex and difficult to follow.",
"cryptic : Having a meaning that is mysterious or obscure.",
"futile : Incapable of producing any useful result; pointless.",
"impede : Delay or prevent (someone or something) by obstructing them; hinder.",
"obscure (adj.) : Not discovered or known about; uncertain.",
"obscure (v.) : Keep from being seen; conceal.",
"quandary : A state of perplexity or uncertainty over what to do in a difficult situation.",
"indolent : Wanting to avoid activity or exertion; lazy.",
"insipid : Lacking flavor; weak or tasteless.",
"listless : (of a person or their manner) lacking energy or enthusiasm.",
"torpor : A state of physical or mental inactivity; lethargy.",
"alienated : Cause (someone) to feel isolated or estranged.",
"alliance : A union or association formed for mutual benefit, especially between countries or organizations.",
"disparity : A great difference.",
"servile : Having or showing an excessive willingness to serve or please others.",
"suppressed : Forcibly put an end to.",
"embellish : Make (something) more attractive by the addition of decorative details or features.",
"florid : Using unusual words and complex constructions.",
"opulent : Ostentatiously rich and luxurious or lavish.",
"ornate : Made in an intricate shape or decorated with complex patterns.",
"ostentatious : Characterized by vulgar or pretentious display; designed to impress or attract notice.",
"poignant : Evoking a keen sense of sadness or regret.",
"ebullience : The quality of being cheerful and full of energy; exuberance.",
"effusive : Expressing feelings of gratitude, pleasure, or approval in an unrestrained or heartfelt manner.",
"egregious : Outstandingly bad; shocking.",
"flagrant : (of something considered wrong or immoral) conspicuously or obviously offensive.",
"frenetic : Fast and energetic in a rather wild and uncontrolled way.",
"gratuitous : Uncalled for; lacking good reason; unwarranted.",
"superfluous : Unnecessary, especially through being more than enough.",
"alleviate : Make (suffering, deficiency, or a problem) less severe.",
"asylum : The protection granted by a nation to someone who has left their native country as a political refugee.",
"auspicious : Conducive to success; favorable.",
"benevolent : Well meaning and kindly.",
"benign : Gentle; kindly.",
"mollify : Appease the anger or anxiety of (someone).",
"reclamation : The process of claiming something back or of reasserting a right.",
"sanction : A threatened penalty for disobeying a law or rule.",
"dubious : Hesitating or doubting.",
"fabricated : Invent or concoct (something), typically with deceitful intent.",
"hypocrisy : The practice of claiming to have moral standards or beliefs to which one's own behavior does not conform; pretense.",
"slander : The action or crime of making a false spoken statement damaging to a person's reputation.",
"spurious : Not being what it purports to be; false or fake.",
"astute : Having or showing an ability to accurately assess situations or people and turn this to one's advantage.",
"clandestine : Kept secret or done secretively, especially because illicit.",
"coup : A sudden, violent, and illegal seizure of power from a government.",
"disingenuous : Not candid or sincere, typically by pretending that one knows less about something than one really does.",
"ruse : An action intended to deceive someone; a trick.",
"stratagem : A plan or scheme, especially one used to outwit an opponent or achieve an end.",
"surreptitiously : In a way that attempts to avoid notice or attention; secretly.",
"wary : Feeling or showing caution about possible dangers or problems.",
"wily : Skilled at gaining an advantage, especially deceitfully.",
"ambiguous : Open to more than one interpretation; having a double meaning.",
"ambivalent : Having mixed feelings or contradictory ideas about something or someone.",
"apathetic : Having or showing little or no emotion; not interested or concerned; indifferent or unresponsive.",
"arbitrary : Based on random choice or personal whim, rather than any reason or system.",
"capricious : Given to sudden and unaccountable changes of mood or behavior.",
"equivocate : Use ambiguous language so as to conceal the truth or avoid committing oneself."]
    generate_html(links)