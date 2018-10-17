/**
 * colorize.spaces.js
 * A script in the Colorize project bundle.
 * Created by Sam Yong in October 2018.
 * All rights reserved.
 *
 * This script replaces all occurences of some single characters
 * with a non-breaking space of specified background.
 * The background color is from Open Color.
 */

var base_color = '#ffa8a8'
var overlay_color = '#4263eb'
var max_depth = 30
var complete_regex_head = /\|\-/g
var complete_regex_tail = /\|\|/g
var incomplete_regex_head = /\|\s/g
var incomplete_regex_tail = /\|\|z/g
var wrapper_head = "<span style='border: 2px solid #dee2e6'>"
var wrapper_tail = "</span>"

var article = document.getElementsByClassName ('markdown-body') [0]
var text = article.innerHTML

text = text.replace (complete_regex_head, wrapper_head +
  "<span style='background-color: " + overlay_color + "'>&nbsp;|")
for (var i = 0; i < max_depth; i++)
  text = text.replace (complete_regex_head, '&nbsp;|')
text = text.replace (complete_regex_tail, "</span>" +
  "<span style='background-color: " + base_color + "'>&nbsp;|")
for (var i = 0; i < max_depth; i++)
  text = text.replace (incomplete_regex_head, '&nbsp;|')
text = text.replace (incomplete_regex_tail, "</span>" + wrapper_tail)

article.innerHTML = text
