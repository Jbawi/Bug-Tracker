class UserInterfaceEventHandler {
    constructor(actionWindowId) {
        this.actionWindow = document.getElementById(actionWindowId);
        this.form = new makeForm();

        // Load active table of starting dashboard 
        this.addTable(this.getActiveId());
    }

    //###PRIVATE####


    //##Async API Requestfunctions (Fetch Api)##

    async sendDataById(selector, inID, method, data) {
        var object = {};
        data.forEach((value, key) => {object[key] = value});
        var json = JSON.stringify(object);

        var uri = `./api/${selector}`;

        if(method == "PUT") {
            uri += `?_id=${inID}`;
        }

        let response = await fetch(uri, {
            method: method, 
            mode: 'cors', 
            cache: 'no-cache', 
            credentials: 'same-origin',
            headers: {
            'Content-Type': 'application/json'
            },
            redirect: 'follow', 
            referrer: 'no-referrer', 
            body: json 
        });
        let tdata = await response.json();
        alert(tdata);
        return tdata;
    }

    async fetchDataById(selector, inID, method) {
        let response = await fetch(`./api/${selector}?_id=${inID}`, {method: method});
        let data = await response.json();

        try { 
            data['selector'] = selector;
            data['id'] = inID; 
        }
        catch(error) { 
            data = {
                'selector': selector,
                'id': inID
            };
        }

        return data;
    }

    async fetchData(selector) {
        let response = await fetch(`./api/${selector}`, {method: "GET"});
        let data = await response.json()
        data['selector'] = selector
        return data;
    }

    
    //##Helper Functions to keep code short##

    getRequestId(event) {
        return event.target.getAttribute("href");
    }

    getActiveId() {
        var active = document.getElementsByClassName("nav-active");
        active = active[0].getAttribute("id");
        return active;
    }

    updateNavigation(event) {
        var activeElements = document.getElementsByClassName('nav-active');

        // Change active navigation Elements to inactive
        for(var x = 0; x < activeElements.length; x++) 
            activeElements[x].setAttribute('class', 'nav-inactive');

        // Change target navigation Element to active and set header of dashboard
        event.target.setAttribute('class', 'nav-active');
    }

    setDashHeader(event) {
        var dashHeader = document.getElementById('dash-header');
        dashHeader.innerHTML = event.target.innerHTML;
    }

    clearDashboard() {
        this.actionWindow.innerHTML = "";
    }

    addTable(activeID) {
        // Make Api Request to get table
        this.fetchData(activeID)
            .then((data) => {
                var table = new makeTable();
                var selector = data['selector'];
                delete data['selector'];
                var addButton = true;
                this.actionWindow.innerHTML += table.createTable(selector, data);
            });
    }

    getFormType(event) {
        var rowId = event.target.parentElement.parentElement.getAttribute("id"); 
        var splited = rowId.split("_");
        return splited[1];
    }

    //###PUBLIC###
    navigationSwitch(event) {
        this.updateNavigation(event);
        this.setDashHeader(event);
        
        this.toDash();
    }

    editElement(event) {
        var row = event.target.getAttribute("href");

        var splited = row.split("_");
        var activeID = splited[1];
        var elementID = splited[0];

        this.fetchDataById(activeID, elementID, "GET")
        .then((data) => {
            var newForm = new makeForm();
            var newSelector = data['selector'];
            var newId = data['id'];

            delete data['selector'];
            delete data['id'];

            this.actionWindow.innerHTML = newForm.createForm(newSelector, data, newId);
        });
    }

    deleteElement(event) {
        var row = event.target.getAttribute("href");

        var splited = row.split("_");
        var activeID = splited[1];
        var elementID = splited[0];

        this.fetchDataById(activeID, elementID, "DELETE")
            .then(() => {this.toDash()});
    }

    toForm(event) {
        this.clearDashboard();
        this.actionWindow.innerHTML = this.form.createForm(event.target.getAttribute("href"));
    }

    toDash() {
        this.clearDashboard();
        var activeID = this.getActiveId();
        if(activeID == "devs") {
            this.addTable("qsemployee");
            this.addTable("swengineer");
        }
        else if(activeID == "categories") {
            this.addTable("caterror");
            this.addTable("catcause");
        }
        else if(activeID == "prolist") {
            // Make Api Request to get table
            this.fetchData(activeID)
            .then((data) => {
                var table = new makeTable();
                delete data['selector'];
                this.actionWindow.innerHTML += table.auswertung1(data);
            });
        }
        else if(activeID == "catlist") {
            // Make Api Request to get table
            this.fetchData(activeID)
            .then((data) => {
                var table = new makeTable();
                delete data['selector'];
                this.actionWindow.innerHTML += table.auswertung2(data);
            });
        }
        else if(activeID == "timedif") {
            // Make Api Request to get table
            this.fetchData(activeID)
            .then((data) => {
                var table = new makeTable();
                delete data['selector'];
                this.actionWindow.innerHTML += table.auswertung3(data);
            });
        }
        else {
            this.addTable(activeID);
        }
    }

    save(event) {
        var value = event.target.getAttribute("value");
        var formData = new FormData(document.getElementById("mainForm"));
        var action = document.getElementById("mainForm").getAttribute("action").split("_");
        var elementID = action[0];
        var activeID = action[1];

        if(value == "Speichern") {
            this.sendDataById(activeID, elementID, "PUT", formData);
        }
        else if(value == "Hinzufugen") {
            this.sendDataById(activeID, elementID, "POST", formData).then(() => {this.toDash();});
        }
    }

    selectRow(event) {
        var row = event.target.parentElement.getAttribute("id");
        var rowElement = event.target.parentElement;

        var splited = row.split("_");
        var action = splited[1];

        var activeRows = document.getElementsByClassName("tableRow-active");
        if(activeRows.length != 0) {
            for(var active in activeRows) {
                activeRows[active].setAttribute("class", "tableRow"); 
                break;
            }
        }
        rowElement.setAttribute("class", "tableRow-active");

        if(action == "bugs") {
            var actionButtons = `<a href="${row}_edit" class="editElement">Bearbeiten</a>`;   
        }
        else {
            var actionButtons = `<a href="${row}_edit" class="editElement">Bearbeiten</a> <a class="deleteElement" href="${row}_delete">Löschen</a>`
        }

        console.log("action-container-" + action);
        var activeAction = document.getElementById("action-container-" + action);
        activeAction.innerHTML = actionButtons;        
    }
}