'use strict';

window.onload = function () {
    var eventHandler = new UserInterfaceEventHandler("window");

    // Handler for all click events
    document.addEventListener('click',function(e) {
        var eventClass = e.target.getAttribute('class');
        var eventId = e.target.getAttribute('id');
        
        if(eventClass == "nav-inactive") {
            eventHandler.navigationSwitch(e);
        }
        else if(eventClass == "editElement") {
            e.preventDefault();
            eventHandler.editElement(e);
        }
        else if(eventClass == "deleteElement") {
            e.preventDefault();
            eventHandler.deleteElement(e);
        }
        else if(eventClass == "tableRow") {
            eventHandler.selectRow(e);
        }
        else if(eventId == "toForm") {
            e.preventDefault();
            eventHandler.toForm(e);
        }
        else if(eventId == "toDash") {
            eventHandler.toDash();
        }
        else if(eventId == "save") {
            e.preventDefault();
            eventHandler.save(e);
        }
    });
}