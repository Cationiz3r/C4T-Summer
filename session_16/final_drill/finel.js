
console.log("------------------< 1 >------------------");
song_container = document.getElementById("song_container");
for (let i=0; i<song_container.childElementCount; ++i) {
    if (song_container.children[i].className == "song") // (Optional)
        console.log(song_container.children[i]); 
}

console.log("------------------< 2 >------------------");
songs = document.getElementsByClassName("song");
for (let i=0; i<songs.length; ++i) {
    let title, artist;
    let song = songs[i]
    for (let j=0; j<song.childElementCount; ++j) {
        if (song.children[j].className == "title")
            title = song.children[j].innerHTML; 
        else if (song.children[j].className == "artist")
            artist = song.children[j].innerHTML;         
    }
    
    console.log(artist, "-", title);
}

console.log("------------------< / >------------------");


function onload_delete() {
    var delete_buttons = document.getElementsByClassName("delete_button");
    for (var i=0; i<delete_buttons.length; ++i) {
        var delete_button = delete_buttons[i];
        delete_button.addEventListener("click", function(event) {
            //console.log(event);
            event.target.parentNode.remove();
        });
        // console.log(i);
    }
}
onload_delete();

function onload_edit() {
    var edit_buttons = document.getElementsByClassName("edit_button");
    for (var i=0; i<edit_buttons.length; ++i) {
        var edit_button = edit_buttons[i];
        edit_button.addEventListener("click", function(event) {
            // console.log(event);
            console.log(event.target.parentNode.attributes.song_id.nodeValue);
        });
    }
}
onload_edit();

function onload_more() {
    var more_buttons = document.getElementsByClassName("more_button");
    for (var i=0; i<more_buttons.length; ++i) {
        var more_button = more_buttons[i];
        more_button.addEventListener("click", function(event) {
            // console.log(event);
            // console.log(event.target.parentNode.children);

            let title, artist;
            let children = event.target.parentNode.children;
            for (let i=0; i<children.length; ++i) {
                if (children[i].className == "title")
                    title = children[i].innerHTML; 
                else if (children[i].className == "artist")
                    artist = children[i].innerHTML;         
            }
            
            console.log(artist, "-", title);
        });
    }
}
onload_more();

function appendContent(node, content) {
    node.appendChild(document.createTextNode(content));
}

var defaultButtonStyle = "background-color: black; font-family: Source Code Pro; color: white; border: 1px solid white";
var add_button = document.getElementById("add_button");
add_button.addEventListener("click", function(event) {
    let newSong = document.createElement("div");
    newSong.setAttribute("class", "song");
    newSong.setAttribute("song_id", "def1c3");

    let titleChild = document.createElement("h4");
    titleChild.setAttribute("class", "title");
    appendContent(titleChild, "Defice!");
    newSong.appendChild(titleChild);

    let artistChild = document.createElement("h5");
    artistChild.setAttribute("class", "artist");
    appendContent(artistChild, "StariX");
    newSong.appendChild(artistChild);

    let deleteButton = document.createElement("button");
    deleteButton.setAttribute("class", "delete_button");
    deleteButton.setAttribute("style", defaultButtonStyle);
    appendContent(deleteButton, "Delete");
    deleteButton.addEventListener("click", function(event) {
        //console.log(event);
        event.target.parentNode.remove();
    });
    newSong.appendChild(deleteButton);
    
    appendContent(newSong, "\u00A0");
    
    let editButton = document.createElement("button");
    editButton.setAttribute("class", "edit_button");
    editButton.setAttribute("style", defaultButtonStyle);
    appendContent(editButton, "Edit");
    editButton.addEventListener("click", function(event) {
        // console.log(event);
        console.log(event.target.parentNode.attributes.song_id.nodeValue);
    });
    newSong.appendChild(editButton);
    
    appendContent(newSong, "\u00A0");

    let moreButton = document.createElement("button");
    moreButton.setAttribute("class", "more_button");
    moreButton.setAttribute("style", defaultButtonStyle);
    appendContent(moreButton, "More");
    moreButton.addEventListener("click", function(event) {
        // console.log(event);
        // console.log(event.target.parentNode.children);

        let title, artist;
        let children = event.target.parentNode.children;
        for (let i=0; i<children.length; ++i) {
            if (children[i].className == "title")
                title = children[i].innerHTML; 
            else if (children[i].className == "artist")
                artist = children[i].innerHTML;         
        }
        
        console.log(artist, "-", title);
    });
    newSong.appendChild(moreButton);

    let page_break = document.createElement("hr");
    newSong.appendChild(page_break);

    song_container.appendChild(newSong);

    

    console.log(newSong);
})