function redirect(){
open('http://localhost:10/', '_self', '', true)
}

setTimeout(redirect, 3000)

// document.addEventListener(this.onload, redirect, true)