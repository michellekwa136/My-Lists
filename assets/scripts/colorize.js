var style = {
  "and": "red",
  "design": "yellow",
  "computer": "purple",
}
var article = document.getElementsByClassName ('markdown-body') [0]
var text = article.innerHTML
Object.keys (style).forEach (function (key, i) {
  text = text.replace (new RegExp (key, "g"),
    "<span style='color: " + style [key] + "'>" + key + "</span>")
})
article.innerHTML = text
