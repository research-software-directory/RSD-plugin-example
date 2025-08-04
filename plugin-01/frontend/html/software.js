
const dynamic = document.getElementById("dynamic-content")

if (dynamic){

  let myHtml ="Dynamic information is send by RSD using {slug} in the href property (see backend/main.py)."
  const urlParams = new URLSearchParams(window.location.search);
  for (const [key, value] of urlParams.entries()) {
    myHtml+= `<br/><b>${key}=${value}</b>`
  }
  if (urlParams){
    dynamic.innerHTML=myHtml
  }
}