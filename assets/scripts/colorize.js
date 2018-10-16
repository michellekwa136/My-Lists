var style = {
  "and": "red",
  "design": "yellow",
  "computer": "purple",
}
var text = $(".markdown-body").innerHTML
Object.keys (style).forEach (function (key, i) {
  text = text.replace (new RegExp (key, "gi"),
    "<span style='color: " + style [key] + "'>" + key + "</span>")
})
$(".markdown-body").innerHTML = text
