class makeTable {
    constructor() {
        this.tselector = {
            "bugs": [
                "description",
                "qs_id",
                "foundAtDate",
                "component_id",
                "category_id",
                "se_id",
                "solution",
                "solvedAtDate",
                "cause_id",
                "bugStatus"
            ],
            "projects": [
                "name",
                "description"
            ],
            "components": [
                "project_id",
                "title"
            ],
            "devs": [
                "name",
                "role"
            ],
            "swengineer": [
                "name",
                "role"
            ],
            "qsemployee": [
                "name",
                "role"
            ],
            "caterror": [
                "type"
            ],
            "catcause": [
                "type"
            ]
        };
        this.thead = {
            "bugs": [
                "ID",
                "Description", 
                "QS (ID)", 
                "Found at", 
                "Comp. (ID)", 
                "Cat. (ID)", 
                "SE (ID)", 
                "Solution", 
                "Solved at", 
                "Error Cause", 
                "Bug Status"
            ],
            "projects": [
                "ID",
                "Name", 
                "Description"
            ],
            "components": [
                "ID",
                "Project ID", 
                "Title"
            ],
            "devs": [
                "ID",
                "Name", 
                "Role"
            ],
            "swengineer": [
                "ID",
                "Name", 
                "Role"
            ],
            "qsemployee": [
                "ID",
                "Name", 
                "Role"
            ],
            "categories": [
                "ID",
                "Type"
            ],
            "caterror": [
                "ID",
                "Type"
            ],
            "catcause": [
                "ID",
                "Type"
            ]
        };
    }

    createTh(name) {
        return `<th>${name}</th>`;
    }

    createTd(data) {
        return `<td class="tableRow">${data}</td>`;
    }  

    createTbody(data, selector) {
        var total = "";
        
        for(var entry in data) {
            total += `
            <tr id="${entry}_${selector}">
                <td class="tableRow">${entry}</td>
            	${this.tselector[selector].map(inLab => this.createTd(data[entry][inLab])).join("")}
            </tr>
            `;
        }
        return total;
    }

    createTable(selector, data, addButton = true) {
        var button = `<div class="action-container" id="action-container-${selector}"><a id="toForm" href="${selector}" class="action-btn">Hinzfugen</a></div>`;
        if(addButton == false) {
            button = "";
        }
        return `
        <table id="tab" class='main-table' style='width: 90%'>
            <thead>
                ${this.thead[selector].map(inLab => this.createTh(inLab)).join("")}
            </thead>
            <tbody>
                ${this.createTbody(data, selector)}
            </tbody>
        </table>
        ${button}
        `;
    }

    auswertung1Template(selector, type, data) {
        if(!(Object.entries(data).length === 0 && data.constructor === Object)) {
            return `
            <h4>${type}</h4>
            ${this.createTable(selector, data, false)}
            `;
        }
        return "";
    }

    auswertung1(data) {
        var total = "";
        for(var project in data) {
            project = data[project];
            total += `
            <h2 style='color:white; margin: 50px 0 0 0; border-top: 2px solid white; border-bottom: 2px solid white; background-color:#0e9917;'>${project["project"]}</h2>
            `;
            for(var component in project["components"]) {
                component = project["components"][component];

                total += `
                <div class="content-wrapper">
                    <h3>${component["title"]}</h3>
                    ${this.auswertung1Template("bugs", "Bugs Detected", component["bugsDetected"])}
                    ${this.auswertung1Template("bugs", "Bugs Solved", component["bugsSolved"])}
                </div>
                `;
            }
        }
        return total; 
    }

    auswertung2(data) {
        console.log(data);

        var total = "";
        for(var category in data) {
            category = data[category];

            total += `
                <div class="content-wrapper">
                    <h3>${category["type"]}</h3>
                    ${this.auswertung1Template("bugs", "Bugs Detected", category["bugsDetected"])}
                    ${this.auswertung1Template("bugs", "Bugs Solved", category["bugsSolved"])}
                </div>
                `;
        }

        return total;
    }

    auswertung3(data) {
        var total = "";
        for(var project in data) {
            project = data[project];
            total += `
            <h2 style='color:white; margin: 50px 0 0 0; border-top: 2px solid white; border-bottom: 2px solid white; background-color:#0e9917;'>${project["project"]}</h2>
            `;
            for(var component in project["components"]) {
                component = project["components"][component];

                total += `
                <div class="content-wrapper">
                    <h3>${component["title"]}</h3>
                    ${this.auswertung1Template("bugs", "Sorted by timedifference:", component["bugsSolved"])}
                </div>
                `;
            }
        }
        return total; 
    }
}