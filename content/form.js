class makeForm {
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

        this.inputtypes = {
            "bugs": {
                "description": "text",
                "qs_id": "number",
                "foundAtDate": "date",
                "component_id": "number",
                "category_id": "number",
                "se_id": "number",
                "solution": "text",
                "solvedAtDate": "date",
                "cause_id": "number",
                "bugStatus": "number"
            },
            "projects": {
                "name": "text",
                "description": "text"
            },
            "components": {
                "project_id": "number",
                "title": "text"
            },
            "devs": {
                "name": "text",
                "role": "text"
            },
            "swengineer": {
                "name": "text",
                "role": "text"
            },
            "qsemployee": {
                "name": "text",
                "role": "text"
            },
            "caterror": {
                "type": "text"
            },
            "catcause": {
                "type": "text"
            }
        }
    }

    makeStandards(selectors) {
        var result = {};
        for(var selector in selectors) 
            result[selectors[selector]] = "";
        
        return result;
    }

    formTemplate(inLab, inputtypes, data ) {
        if(inLab=="role"){
            return `
            <div class='inputcontainer'>
                <label for='${inLab}'>${inLab}</label>
                <select name="role">
                   <option  value="SW-Entwickler">SW-Entwickler</option>
                   <option  value="QS-Mitarbeiter">QS-Mitarbeiter</option>
                </select>
            </div>  `
        }
        return `
        <div class='inputcontainer'>
            <label for='${inLab}'>${inLab}</label>
            <input type='${inputtypes}' name='${inLab}' value='${data[inLab]}' required />
        </div>
        `
    }
    createForm(selector, data = 0, elementID = "new") {
        if(data == 0) {
            var tdata = this.makeStandards(this.tselector[selector]);
            var buttonvalue = "Hinzufugen";
        }
        else {
            var tdata = data;
            var buttonvalue = "Speichern";
        }
        

        return `
        <form id="mainForm" action='${elementID}_${selector}' method='POST'>
            ${this.tselector[selector].map(inLab => this.formTemplate(inLab, this.inputtypes[selector][inLab], tdata)).join("")}
            <div class="action-container">
                <a class="action-btn-2" id="toDash" href="#">Abbrechen</a>
                <input type="submit" class="action-btn-3" id="save" value="${buttonvalue}"/>
            </div>
        </form>
        `;
        
    }
}