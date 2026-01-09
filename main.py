from pyscript import document

def information(event):
    club = document.getElementById("club").value
    info_box = document.getElementById("info")
    output = document.getElementById("clubinfo")

    info_box.style.display = "block"
    if club == "choose" or club == "":
        output.innerText = "filler"
    
    elif club == "club1":
        output.innerText = (
            "Debate Club\n"
            "A club where students practice public speaking, argumentation, and critical thinking by debating current events, ethical issues, and fun topics in a structured setting."

        )

    elif club == "club2":
        output.innerText = (
            "Science Club\n"
            "A hands-on club for students who enjoy experiments, science projects, and exploring how things work, often participating in competitions or school science fairs."

        )

    elif club == "club3":
        output.innerText = (
            "club3\n" 
            "filler"
        )
    elif club == "club4":
        output.innerText = (
            "club3\n" 
            "filler"
        )
    elif club == "club5":
        output.innerText = (
            "club3\n" 
            "filler"
        )

