# odyssey-translation-compendium
DSAM 3000 semester project, fall 2025: an odyssey translation compendium. 

# Overview

this is the beginnings of the creation of a tool that would align the Greek text of "The Odyssey" alongside translations of the Greek. as of the Fall 2025 semester, the selected translations are that of Richmond Lattimore, and the newer translation offered by Emily Wilson. during this exploratory phase, focusing on the first point of inquiry below, the first stanza of Book 1 (approx. lines 1-10) will be worked with. for future tool-building, sections relevant to the second question below, involving monsters, would be aligned. 

# Points of Inquiry 

* during tool development: how does computation help or hinder the learning process when working with translations & variations across texts?
* following tool development: how do different translations of the odyssey portray and refer to monsters? 

The main question I investigated this term, using myself as the main "guinea pig," was about the ways in which computation affects the learning process when working with translations of texts. In short, I believe that computation absolutely helped my learning process by allowing me to access materials and put them alongside one another in a way that I could not easily execute without it. The feeling of unlimited possibility or overwhelm of choice when it came to computational methods, though, could feel a bit paralyzing. That is more of a hindrance that comes from my own thoughts and feelings in relation to computation, though, so I don't want folks to have the wrong idea when I posit that. 

In comparison to my past translation work (by hand, in the context of translating classical music repertoire with the help of opera scores + credible libretto translations + dictionaries), my thought process surrounding langauge when working through this project was noticeably different. Trying to focus on the alignment of words made me more acutely aware of different languages' grammatical conventions and structures. I also paid more care and attention to differing choices across translations, which is natural considering the structure of the project, but feels important to note. If I hadn't done this work, I could see myself having more general takeaways about the different choices made by Lattimore and Wilson in their translations. Having to focus line-by-line for this project, though, I am now more aware of the multitude of choices that would come up as someone translates a text. _How much or how little context do I add for a reader through the translation? Should poetic tone be the focus, or literal word meaning? If translations exist as precedent surrounding a particular text, what would comparative or contrasting choices say in response to those pre-existing translations?_

# Points of Access

* GitHub Repository: displays the ReadMe markdown file documenting an overview of the project, and houses the relevant coding files for the project. in the spirit of this tool's development serving as a means of investigation in the learning process around translation work and the digital, test files will also be stored here to document trial (and, inevitably, a hell of a lot of error.)
* [Zotero Library](https://www.zotero.org/groups/6259732/odyssey_variorum): provides access to sources and points of inspiration for the project. 
* Notion Workspace (private): home to my personal Mindful Practice Journal, or what i've affectionately been calling my Captain's Log. also home to brainstorming documents, and other course materials related to DSAM 3000. 
* [Cargo Website](https://odyssey-variorum.cargo.site/edit/Y0061314437): displays a curated version of the aforementioned Captain's Log, as a means of documenting the learning process. will eventually house the compendium tool.  (Note: This link will not work if you do not have admin. account access - more on that in the Lessons Learned section)

# Brief File Directory

Files in this GitHub repository are organized by the three Odyssey-related text sources: the Greek text, the translation by Richmond Lattimore of the text from 1965, and the recent Emily Wilson translation published in 2017. There are three main subcategories of these files: 

* Plain text files of the first stanza of the text (Book 1, lines 1-10, -- or 1-11, depending on translation)
* Files that aim to "flatten" said text in XML, adding milestone markers or idicators to break up the text in ways that may be useful to a user interacting with a translation compendium tool 
* Files that, when linked together with a Python script, produce an HTML table aligning the translations with one another


# Where Things Stand (or Don't) - Lessons Learned

As of the end of the semester, not much of an actual tool was created, aside from a series of prototypes and basic tables (through the use of XML, XSLT, and Python to create an HTML file as output). A lack of a functional tool expected from jump, due to the fact that the projects that this endeavor (odyssey?) was based on were created by teams with funding and other resources; however, there is still much to be gained from what was explored during this stretch of work: 

* The importance of scope setting in any project, but especially in the realm of the digital. My textual focus of this project, The Odyssey, is not known for its brevity, so when I was met with the suggestion of focusing in on what felt like a very, very small section of it, it didn't feel like I would have a lot to work with; however, that was very much not the case. I'm thankful that such a scope was defined at the start of the term, as the problems that I ran into when it came to coding the project would have only exponentially increased, if more of the text had been at play. 
* Understanding that even "tools" have arguments. Argument development and exploration was a key part of iteration 3 of the project, as per the class's structure, and I found it very difficult to tease out an argument from my own work and thoughts, despite how much I had thrown myself into the work, and the difficulty of aligning texts across language. Through the help of instructor office hours and class exploration of other Digital Humanities projects, and how arguments can manifest in various layers of these projects (content of the project, the way that content is displayed, what is or isn't included, etc.), this idea is much more evident to me now. I feel more confident in my ability to look at my own work, and others', and identifying various arguments present in choices that were made throughout the course of a project. 
* The distinction of being able to conceptually understand what one wants to execute through code, and what one can actually accomplish. My disconnect in this area proved to be a major source of frustration for me, even when accepting that I needed to have realistic expectations of what I could and couldn't learn throughout the course of the term. 
* The importance of documentation. I leaned heavily on the documentation of others' projects (such as the Frankenstein Variorum) to have even half of a clue as to what I should do, computationally, to try and move forward with this project. I also relied on documentation provided for markup languages, such as XML, to understand concepts and syntax. 
* What feels like "basic" computation is still computation, and can still provide insights and lessons. At the end of the term, when it became especially obvious to me that my coding skills would not be strong enugh to produce something more than a table, I pivoted to prototyping. Even if this felt like a step backwards, computationally, prototype work still presented value in regards to thinking about the user experience with the tool, and paired nicely with the class's readings and discussions on data visualization choice.
* How crucial it is to ensure that your work can be fully public, in the way that you expect. I was embarrassed to see that the word I had put into my Cargo site would not be able to be fully shared at the end of this term, due to my misunderstanding of their premium/paywall. I'm thankful to have had access to a Cargo site account, and chose this platform because of my previous work with it as a collaborator on other sites (mainly a site for a reading group that I co-facilitate, hosted on another person's account), but I could have pivoted to another website platform if I had taken the time to better understand how the website publication part of their platform works. To make up for this, I have embedded a few screenshots below of the Cargo site, and made a point to expand this ReadMe file in more detail to provide contextual information that the site would have hosted on its sidebars and subpages. 
* The value of learning alongside others, and learning by doing, even if that "doing" is messy. Even though my individual work on this project provided a lot of insight for me (albeit in frustrating ways, at times), I think that I learned the most from my fellow classmates, and by seeing their own projects progress throughout the term. Learning as a cohort was a great experience, and I look forward to continuing to learn this way through the Digital Studies course sequence. 
* Finally, the importance of knowing when it's time to pivot to something else, or to let a project be. Because of a want (and need) to shift my scholarly focus back to archives, my inclination now is to let this project stand where it does (or doesn't), and pivot to something new -- I believe that I described this to Ben with the statement, "I want (academically) to go home!" at one point. Similar to what other classmates mentioned in their final presentations, I believe that my work on this project solidified what I'm interested in academically (adaptation, multidisciplinarity, how information is shared and displayed), and what is fascinating to me, but not something I want to dig into with the same depth (linguistics, computation as a means for textual alignment, etc.). As Alison mentioned following my final presentation, this project made it clearer to me what my role potentially would be as a part of a team working towards a larger Digital Humanities project, and what that role's scope would or would not include. 

No matter how much or how little I succeeded, or how the end result of this semester shaped up in comparison to what I imagined at the start of the term, I am incredibly grateful to have been a part of this class, and in a cohort that was so supportive and generative. Looking forward to what Practicum brings in the Spring term! 

-Scylla 

(Additional progress notes and images below...)

# Prototyping Efforts

After realizing that I would not be able to execute a decent mock-up of the tool computationally (on my own), I decided to shift gears and work towards prototyping. This started off in a very basic form: 

<img width="498" height="245" alt="image" src="https://github.com/user-attachments/assets/5ea1c0a1-a37a-436a-8210-f72a379fd09c" />

<img width="542" height="277" alt="image" src="https://github.com/user-attachments/assets/6196638d-ef1b-433a-a0af-ec6dd019c2fd" />

I established with these basic prototypes a few key things: 
* As demonstrated in other data visualizations discussed in class, as well as other variora & translation-based DH projects, (Project Alpheios's tool involving one translation and the original Greek is a good example), color would play an important part in mapping out word meaning and alignment across texts.
* Similarly, if color is going to be a factor, that means that I would need to keep accessibility in mind to account for things like color-blindness.
* Decisions would need to be made about how the texts are displayed against one another. Should they be side-by-side, as I was able to create in VS Code? Should it operate as more of a pop-up system, depending on the text the user is highlighting/clicking on/interacting with? Does the actual position of the texts in relation to each other, if they're side-by-side, matter to a user?

Considering these points, below is a more complicated mock-up/prototype of the tool, which I designed using Canva: 

<img width="898" height="581" alt="image" src="https://github.com/user-attachments/assets/b299ddec-7dbf-4fc3-9001-99c50747571b" />

With this prototype, a left-hand sidebar allows a user to customize their experience through the selection of which texts are visible (as well as their alignment in relation to one another), selection of automatically highlighted text emphasis if desired, and accessibility settings if needed. Three main text panels (since all three texts are selected in this hypothetical example) are present, and an example of corresponding highlighting across texts is displayed. The header of the site would contain the title that returns to a home page, and links to subpages (About, Contact, Resources). There is also a search bar that would allow for searching through the text. 

There are many back-end complexities that would go into making this prototype a reality that are way beyond my computational skills. For example, if parts of speech is a way for the text to be emphasized, words would need to be labeled by their parts of speech on the back-end. I found joy in creating this prototype because of being able to set aside my limits computationally, though, and it allowed me to focus on the user experience. 


# Cargo site screengrabs (rip)

<img width="1179" height="739" alt="image" src="https://github.com/user-attachments/assets/117af04f-d224-424c-a8b9-ef711310b8e1" />

<img width="1470" height="811" alt="image" src="https://github.com/user-attachments/assets/4de7e419-4d7f-48ed-91d6-0303b8cebaed" />

<img width="1470" height="811" alt="image" src="https://github.com/user-attachments/assets/c027d6b0-ac76-48d3-8f0d-14550f249b2a" />








