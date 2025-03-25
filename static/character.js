text_area=document.getElementById("id_text")
text_area.addEventListener("keypress", (event) => {
    text=text_area.value.split(" ")
    if (text.length == 7){
        event.preventDefault()
    }
})