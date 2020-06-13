function v(){
    var forms = document.getElementById("search_form")
    forms.addEventListener("submit", f)
    function f() {
        var searchs = document.getElementById("search_form_text")
        q = true
        if(searchs.value.length == 0){
            q = false
            return q
        }
        else{
            q = true
            return q
        }
    }
}
v()